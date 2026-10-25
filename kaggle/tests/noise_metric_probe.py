"""Q27 synthetic counterexamples: energy contrast is not ground-truth SNR.

Executes actual stage17 metric/normalization functions via AST. No denoiser,
trained voice, real microphone, GPU or acoustic acceptance is exercised.
"""
from pathlib import Path
import argparse,ast,copy,hashlib,json
import numpy as np
R=Path(__file__).resolve().parents[2];source=R/'kaggle/source/py/analyst.py'
tree=ast.parse(source.read_bytes())
names={'frame_rms_db','estimate_snr','speech_rms_dbfs','normalize_speech'}
nodes=[copy.deepcopy(n) for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]
assert len(nodes)==4
ns={'np':np,'TARGET_DBFS':-21.0};exec(compile(ast.fix_missing_locations(ast.Module(body=nodes,type_ignores=[])),str(source),'exec'),ns)
estimate=ns['estimate_snr'];normalize=ns['normalize_speech']

def db_power(x):return float(10*np.log10(max(float(np.mean(np.asarray(x,dtype=np.float64)**2)),1e-30)))
def snr(signal,noise):return db_power(signal)-db_power(noise)

def main():
    p=argparse.ArgumentParser();p.add_argument('--round',type=int,required=True);args=p.parse_args()
    sr=24000;block=np.arange(480)/sr;clean_block=.03*np.sin(2*np.pi*500*block)
    rng=np.random.default_rng(2718);noise_block=rng.standard_normal(480);noise_block/=np.sqrt(np.mean(noise_block**2))
    clean=np.tile(clean_block,50).astype(np.float32);cases=[]
    cases.append({'case':'steady-clean-energy-contrast','reported_estimate_db':estimate(clean,sr),'ground_truth_noise_present':False})
    assert abs(cases[-1]['reported_estimate_db'])<1e-6
    for scale in [.001,.02]:
        noise=np.tile(noise_block*scale,50).astype(np.float32);y=clean+noise
        score=estimate(y,sr);assert abs(score)<1e-6
        cases.append({'case':'repeated-stationary-noise-block','noise_rms':scale,'reported_estimate_db':score,
            'oracle_snr_db':snr(clean,noise),'note':'Repeated synthetic block isolates equal frame RMS; not real-world noise statistics.'})
    assert cases[1]['oracle_snr_db']-cases[2]['oracle_snr_db']>25
    dynamic=(clean.reshape(50,480)*np.linspace(.1,1.,50)[:,None]).reshape(-1).astype(np.float32)
    assert estimate(dynamic,sr)>10
    cases.append({'case':'clean-amplitude-dynamics','reported_estimate_db':estimate(dynamic,sr),'ground_truth_noise_present':False})
    noise=np.tile(noise_block*.003,50).astype(np.float32);y=clean+noise;gain=.1
    assert abs(snr(clean,noise)-snr(clean*gain,noise*gain))<1e-5
    cases.append({'case':'uniform-attenuation-is-not-denoising','signal_change_db':db_power(clean*gain)-db_power(clean),
        'noise_change_db':db_power(noise*gain)-db_power(noise),'oracle_snr_before_db':snr(clean,noise),'oracle_snr_after_db':snr(clean*gain,noise*gain)})
    quiet=(y*.01).astype(np.float32);out=normalize(quiet,sr)
    inferred_gain=float(np.dot(quiet.astype(np.float64),out)/np.dot(quiet.astype(np.float64),quiet))
    assert len(out)==len(quiet) and np.isfinite(out).all() and np.max(np.abs(out-quiet*inferred_gain))<1e-8
    before=snr(clean*.01,noise*.01);after=snr(clean*.01*inferred_gain,noise*.01*inferred_gain)
    assert abs(after-before)<1e-5
    cases.append({'case':'actual-normalize-speech','measured_uniform_gain_db':float(20*np.log10(inferred_gain)),
        'oracle_snr_before_db':before,'oracle_snr_after_db':after,'sample_count_preserved':True,'denoiser_executed':False})
    zero=np.zeros_like(y)
    cases.append({'case':'erase-all-output','remaining_noise_power':float(np.mean(zero**2)),
        'remaining_signal_power':float(np.mean(zero**2)),'oracle_snr_db':None,'accept_as_quality_success':False})
    t=np.arange(sr)/sr;wanted_low=.03*np.sin(2*np.pi*500*t);wanted_high=.01*np.sin(2*np.pi*6000*t);wanted=wanted_low+wanted_high
    noise=rng.standard_normal(sr)*.002
    freq=np.fft.rfftfreq(sr,1/sr);noise=np.fft.irfft(np.fft.rfft(noise)*(freq>4500),n=sr)
    observed=wanted+noise;lowpass=lambda x:np.fft.irfft(np.fft.rfft(x)*(freq<=3000),n=sr)
    filtered=lowpass(observed);filtered_noise=lowpass(noise)
    before_error=db_power(observed-wanted);after_error=db_power(filtered-wanted)
    assert db_power(filtered_noise)<db_power(noise)-100 and after_error>before_error
    cases.append({'case':'ideal-lowpass-information-loss-counterexample','remaining_noise_change_db':db_power(filtered_noise)-db_power(noise),
        'error_relative_to_known_clean_before_dbfs':before_error,'error_relative_to_known_clean_after_dbfs':after_error,
        'useful_6khz_component_removed':True,'accept_as_quality_success':False,
        'note':'Ideal FFT mask is a synthetic counterexample, not the production denoiser or a real fricative test.'})
    assert len(cases)==8
    print(json.dumps({'round':args.round,'experiment_completed':True,'cases':cases,
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'method':'AST-extracted actual energy metrics/normalization plus known-component synthetic counterexamples; fixed RNG',
        'numpy_version':np.__version__,'product_modified':False,'real_audio_available':False,'full_model_executed':False,
        'gpu_executed':False,'voice_quality_verified':False,'user_hiss_root_cause_proven':False},indent=2))
if __name__=='__main__':main()
