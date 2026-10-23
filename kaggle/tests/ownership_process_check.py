#!/usr/bin/env python3
"""Real supervisor/pass_fds/stop protocol x3, with CPU model-role stand-ins ONLY."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time

ROOT=Path(__file__).resolve().parents[1]/'source'
sys.path.insert(0,str(ROOT/'py'))
from gpu_ownership import status
TOOL=ROOT/'tools/resource_control.py'

HELPER="""import os,sys,threading
from pathlib import Path
sys.path.insert(0,sys.argv[1])
from gpu_ownership import inference_guard,FD_ENV,NONCE_ENV
name=sys.argv[3]
if name=='gateway':
    assert FD_ENV not in os.environ and NONCE_ENV not in os.environ
    lease=None
else:lease=inference_guard(mock=False)
(Path(sys.argv[2])/(name+'.ready')).write_text('cpu-stand-in-not-gpu')
threading.Event().wait(60)
"""
CONTROL="""import os,sys
from pathlib import Path
sys.path.insert(0,sys.argv[1])
import supervisor as s
s.MOCK=False
state=Path(sys.argv[2])
helper=sys.argv[3]
def build():
    return [s.Proc(name,[sys.executable,'-c',helper,sys.argv[1],str(state),name],{}) for name in ['worker0','worker1','analyst','gateway']]
def watch(procs):
    (state/'controller.ready').write_text('protocol-only')
    s.STOP.wait(60)
s.build_procs=build
s.watch=watch
raise SystemExit(s.main())
"""


def main():
    if status()['busy']:raise RuntimeError('existing holder present; do not disrupt it')
    with tempfile.TemporaryDirectory(prefix='qtts-owner-process-') as temporary:
        for index in range(1,4):
            state=Path(temporary)/str(index);state.mkdir()
            env={**os.environ,'QTTS_ROOT':str(ROOT),'QTTS_STATE':str(state),'QTTS_MOCK':'0'}
            for key in ('QTTS_GPU_LEASE_FD','QTTS_GPU_LEASE_NONCE'):env.pop(key,None)
            process=subprocess.Popen([sys.executable,'-c',CONTROL,str(ROOT/'py'),str(state),HELPER],env=env,
                                     stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            try:
                deadline=time.monotonic()+10
                files=[state/(name+'.ready') for name in ('worker0','worker1','analyst','gateway','controller')]
                while not all(p.exists() for p in files) and process.poll() is None and time.monotonic()<deadline:time.sleep(.02)
                assert all(p.exists() for p in files),'controlled CPU-role startup failed'
                assert status()['busy']
                denied=subprocess.run([sys.executable,str(TOOL),'reserve','--seconds','1'],capture_output=True,text=True,timeout=5)
                assert denied.returncode==2 and json.loads(denied.stdout)['code']==409
                process.terminate();process.wait(10)
                assert process.returncode==0 and not status()['busy']
                assert not (state/'supervisor.pid').exists()
                reserved=subprocess.run([sys.executable,str(TOOL),'reserve','--seconds','1'],capture_output=True,text=True,timeout=5)
                assert reserved.returncode==0 and not status()['busy']
                print(json.dumps({'round':index,'real_supervisor_fd_lifecycle_passed':True,'model_roles':'CPU stand-ins only',
                      'workers':2,'analyst_inherited':True,'gateway_unleased':True,'offline_busy_409':True,
                      'stop_then_reserve_passed':True,'gpu_verified':False,'training_verified':False}),flush=True)
            finally:
                if process.poll() is None:process.terminate();process.wait(10)
    print('OWNERSHIP PROCESS: 3/3 protocol rounds. NO real GPU/model/VRAM/training evidence.')


if __name__=='__main__':main()
