"""Owned real TCP/Uvicorn harness around original analyst.app; workers/models are fixtures."""
from contextlib import contextmanager, ExitStack
import io
import os
from pathlib import Path
import shutil
import socket
import struct
import sys
import tempfile
import threading
import wave
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[2]
IMPORT_STATE=tempfile.TemporaryDirectory(prefix='input-http-import-')
os.environ.setdefault('QTTS_STATE',IMPORT_STATE.name)
os.environ.setdefault('QTTS_MOCK','1');os.environ.setdefault('QTTS_NO_RUST','1')
sys.path.insert(0,str(ROOT/'kaggle/source/py'))
import analyst
import httpx
import uvicorn
from qtts_common import read_json,write_json_atomic
from resource_limits import HeavyAdmission
from voice_binding import reference_binding

class TCPFixture:
    def __init__(self,root):
        self.root=Path(root);self.root.mkdir(parents=True,exist_ok=True);self.profiles=self.root/'profiles';self.profiles.mkdir(exist_ok=True);self.reloads=[];self.rows=[]
        self.heavy=HeavyAdmission(2)
    def profile(self,trained=False):
        directory=self.profiles/'voice';directory.mkdir(exist_ok=True)
        for n in (0,1):
            raw=io.BytesIO()
            with wave.open(raw,'wb') as f:
                f.setnchannels(1);f.setsampwidth(2);f.setframerate(24000);f.writeframes(struct.pack('<h',1000+n)*36000)
            (directory/f'cand{n}.wav').write_bytes(raw.getvalue())
        shutil.copy(directory/'cand0.wav',directory/'anchor_0.wav')
        data={'id':'voice','anchor':'anchor_0.wav','anchor_candidate':0,'ref_text':'fixture zero', 'language':'Chinese',
            'candidates':[{'file':'cand0.wav','text':'fixture zero'},{'file':'cand1.wav','text':'fixture one'}]}
        if trained:data['trained_adapter']={'test_only':True}
        write_json_atomic(directory/'profile.json',data);return directory,data
    def reload(self,pid):
        self.reloads.append(pid);return [{'ok':True},{'ok':True}]
    def post(self,path,raw):
        response=self.client.post(path,content=raw,headers={'Content-Type':'application/json'})
        record={'path':path,'request_utf8':raw.decode('utf-8') if isinstance(raw,bytes) else raw,'status':response.status_code,'response_text':response.text}
        self.rows.append(record);return response
    @contextmanager
    def serve(self):
        ready=threading.Event();failures=[];owner=self
        class Server(uvicorn.Server):
            async def startup(self,sockets=None):
                try:await super().startup(sockets=sockets)
                finally:ready.set()
        sock=socket.socket();sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1);sock.bind(('127.0.0.1',0));sock.listen(32)
        server=Server(uvicorn.Config(analyst.app,log_config=None,log_level='critical',access_log=False,lifespan='off',timeout_graceful_shutdown=2))
        def run():
            try:server.run(sockets=[sock])
            except BaseException as e:failures.append(type(e).__name__);ready.set()
        thread=threading.Thread(target=run,name='owned-input-http-uvicorn')
        with ExitStack() as stack:
            stack.enter_context(patch.object(analyst,'PROFILES_DIR',self.profiles))
            stack.enter_context(patch.object(analyst,'profile_dir',side_effect=lambda pid:self.profiles/pid))
            stack.enter_context(patch.object(analyst,'load_profile',side_effect=lambda pid:read_json(self.profiles/pid/'profile.json')))
            stack.enter_context(patch.object(analyst,'HEAVY',self.heavy))
            stack.enter_context(patch.object(analyst,'load_on_workers',side_effect=self.reload))
            thread.start()
            try:
                assert ready.wait(5),'TCP fixture startup deadline';assert server.started and not failures,failures
                with httpx.Client(base_url=f'http://127.0.0.1:{sock.getsockname()[1]}',timeout=5,trust_env=False) as self.client:yield owner
            finally:
                server.should_exit=True;thread.join(timeout=5);sock.close()
                assert not thread.is_alive(),'owned TCP server failed to stop';assert not failures,failures
        # Private loopback port only; not a user-facing preview or actual Go proxy.
