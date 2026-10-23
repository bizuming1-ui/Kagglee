#!/usr/bin/env python3
"""3 actual CPU/Gloo joint-loss runs. Tiny test network, NOT Qwen/T4."""
import argparse
import json
from pathlib import Path
import tempfile
import torch.multiprocessing as mp
from test_tts_training import gloo_worker


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    results=[]
    for round in range(1,4):
        with tempfile.TemporaryDirectory(prefix='qtts-real-tensors-') as temporary:
            mp.spawn(gloo_worker,args=((Path(temporary)/'store').as_uri(),temporary),nprocs=2,join=True)
            reports=[json.loads((Path(temporary)/f'{rank}.json').read_text()) for rank in (0,1)]
            assert reports[0]['before']==reports[1]['before'] and reports[0]['after']==reports[1]['after']
            assert reports[0]['before']!=reports[0]['after']
            for epoch in range(2):
                assert set(sum([r['reports'][epoch]['seen_indices'] for r in reports],[]))=={0,1,2}
                assert all(r['reports'][epoch]['optimizer_steps']==1 for r in reports)
            results.append({'round':round,'network':'tiny-test-network-not-Qwen','device':'CPU','backend':'gloo',
                            'two_processes':True,'parameters_changed':True,'ranks_final_identical':True,'rank_reports':reports,
                            'qwen_executed':False,'cuda_executed':False,'quality_verified':False})
    args.output.write_text(json.dumps(results,indent=2)+'\n');print('3/3 actual tiny tensor/DDP/optimizer runs; NOT Qwen/CUDA/T4 evidence.')


if __name__=='__main__':main()
