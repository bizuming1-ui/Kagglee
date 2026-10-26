"""Read existing local worker health only: no install, model load, token or writes."""
import json,urllib.request
class NoRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,*args,**kwargs):return None

def collect(ports=(7001,7002)):
 if len(ports)!=2 or len(set(ports))!=2 or any(type(p) is not int or not 1<=p<=65535 for p in ports):raise ValueError('two distinct valid worker ports required')
 opener=urllib.request.build_opener(urllib.request.ProxyHandler({}),NoRedirect());rows=[]
 for port in ports:
  try:
   with opener.open(f'http://127.0.0.1:{port}/health',timeout=5) as response:
    raw=response.read(65537)
    if len(raw)>65536:raise ValueError('health_byte_budget')
    h=json.loads(raw)
    if not isinstance(h,dict):raise ValueError('health_object_required')
   rows.append({'port':port,'reachable':True,'gpu':h.get('gpu') if type(h.get('gpu')) is int else None,'ready':h.get('ready') is True,'engine':h.get('engine') if isinstance(h.get('engine'),str) else None,'model_loaded':h.get('model_loaded') is True,'dtype':h.get('dtype') if isinstance(h.get('dtype'),str) else None,'rt':h.get('rt') if isinstance(h.get('rt'),str) else None,'error_present':bool(h.get('error')),'fatal_error':h.get('fatal_error') is True})
  except Exception as exc:rows.append({'port':port,'reachable':False,'error_type':type(exc).__name__})
 loaded=all(r.get('reachable') and r.get('ready') and r.get('model_loaded') and r.get('engine')=='faster-qwen3-tts' and not r.get('error_present') and not r.get('fatal_error') for r in rows) and {r.get('gpu') for r in rows}=={0,1}
 return {'read_only':True,'workers':rows,'both_workers_report_real_model_loaded':loaded,'real_inference_verified':False,'training_verified':False,'quality_or_speed_verified':False}
if __name__=='__main__':print(json.dumps(collect(),ensure_ascii=False,indent=2))
