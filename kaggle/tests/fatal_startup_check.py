#!/usr/bin/env python3
"""Real supervisor + CPU fatal-health stand-in; no GPU/model execution."""
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time
ROOT=Path(__file__).resolve().parents[1]/'source'
TEMP=tempfile.TemporaryDirectory(prefix='qtts-fatal-start-')
os.environ['QTTS_ROOT']=str(ROOT);os.environ['QTTS_STATE']=TEMP.name;os.environ['QTTS_MOCK']='1'
sys.path.insert(0,str(ROOT/'py'))
import bootstrap


def main():
    worker_script=Path(TEMP.name)/'fatal_worker.py'
    worker_script.write_text('''import json,sys,os
from http.server import HTTPServer,BaseHTTPRequestHandler
class Handler(BaseHTTPRequestHandler):
 def log_message(self,*_):pass
 def do_GET(self):
  self.send_response(200);self.send_header('Content-Type','application/json');self.end_headers()
  self.wfile.write(json.dumps({'fatal_error':True,'ready':False,'error':'CPU injected MimiConfig rope_theta failure'}).encode())
open(sys.argv[2],'w').write(str(os.getpid()))
HTTPServer(('127.0.0.1',int(sys.argv[1])),Handler).serve_forever()
''')
    for round_id in range(1,4):
        with socket.socket() as stream:stream.bind(('127.0.0.1',0));port=stream.getsockname()[1]
        state=Path(TEMP.name)/str(round_id);state.mkdir();pidfile=state/'worker.pid'
        env={**os.environ,'QTTS_STATE':str(state),'QTTS_STARTUP_ID':bootstrap.STARTUP_ID,'PYTHONPATH':str(ROOT/'py')}
        script=f"import supervisor;supervisor.build_procs=lambda:[supervisor.Proc('worker0',[{sys.executable!r},{str(worker_script)!r},{str(port)!r},{str(pidfile)!r}],{{}},'http://127.0.0.1:{port}/health')];supervisor.main()"
        with open(state/'services.txt','w') as logs:
            process=subprocess.Popen([sys.executable,'-c',script],env=env,stdout=logs,stderr=subprocess.STDOUT,start_new_session=True)
            previous=bootstrap.STATE;bootstrap.STATE=state
            try:
                assert bootstrap.wait_ready(1,timeout_s=18,supervisor_process=process) is False
                receipt=json.loads((state/'startup-failure.json').read_text());assert receipt['startup_id']==bootstrap.STARTUP_ID and receipt['kind']=='fatal_configuration'
                bootstrap.stop_created_supervisor(process);assert process.poll() is not None
                assert not (state/'supervisor.pid').exists()
                child=int(pidfile.read_text())
                assert not Path(f'/proc/{child}').exists(),'fatal CPU worker still alive'
                print(json.dumps({'round':round_id,'passed':True,'real_supervisor_fatal_receipt':True,'current_nonce_checked':True,'owned_supervisor_shutdown':True,'worker_exited':True,'gpu_executed':False,'model_loaded':False}),flush=True)
            except BaseException:
                logs.flush();print((state/"services.txt").read_text(),file=sys.stderr);raise
            finally:
                bootstrap.STATE=previous
                if process.poll() is None:bootstrap.stop_created_supervisor(process)
    TEMP.cleanup()


if __name__=='__main__':main()
