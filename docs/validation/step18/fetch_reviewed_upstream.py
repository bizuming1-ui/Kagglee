"""Materialize the two reviewed wheels for AST probes; never install them or download weights."""
from pathlib import Path, PurePosixPath
import hashlib,json,urllib.request,zipfile
R=Path(__file__).resolve().parents[3];H=Path(__file__).resolve().parent
provenance=json.loads((H/'upstream-round2-provenance.json').read_text())
for row in provenance['inspected_wheels']:
    target={'faster-qwen3-tts':'upstream','qwen-tts-hf':'upstream-hf'}.get(row['project'])
    if target is None:continue  # old qwen-tts was comparison only; do not install/mix namespaces
    url=row['wheel_url'];assert url.startswith('https://files.pythonhosted.org/')
    wheel=R/'.cache/step18/wheels'/url.rsplit('/',1)[-1]
    wheel.parent.mkdir(parents=True,exist_ok=True)
    if wheel.exists():data=wheel.read_bytes()
    else:
        data=urllib.request.urlopen(url,timeout=60).read(2*1024*1024+1)
        assert len(data)<=2*1024*1024
    assert hashlib.sha256(data).hexdigest()==row['wheel_sha256'],row['project']
    wheel.write_bytes(data)
    with zipfile.ZipFile(wheel) as z:
        for item in z.infolist():
            name=PurePosixPath(item.filename)
            assert not name.is_absolute() and '..' not in name.parts and '\\' not in item.filename
            assert (item.external_attr>>16)&0o170000 != 0o120000
        z.extractall(R/'.cache/step18'/target)
    print(row['project'],row['version'],'SHA256 verified; source extraction only')
