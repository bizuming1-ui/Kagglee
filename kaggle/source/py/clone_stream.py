"""Faster0.5.4 generation adapter: ICL conditioning, GENERATED-ONLY codec decode.

No reference codes/PCM enter the codec. Fixed Qwen 12.5Hz contract: 16 codebooks,
24kHz, 1920 samples/frame. Fail closed if the actual tokenizer differs.
CPU fixture experiments are not trained-model quality/T4 performance evidence.
"""
from __future__ import annotations
import os
import time
import numpy as np


def conditioning(prof: dict) -> tuple[str, bool]:
    mode = os.environ.get('QTTS_CLONE_MODE', 'icl').strip().lower()
    if mode not in ('icl', 'xvector'):
        raise ValueError('QTTS_CLONE_MODE must be icl or xvector')
    if mode == 'xvector':
        return '', True
    text = str(prof.get('ref_text') or '').strip()
    if not text:
        raise ValueError('ICL requires a transcript matching the reference; edit reference text or explicitly select QTTS_CLONE_MODE=xvector')
    return text, False


def codec_lookahead_frames():
    try:
        value = int(os.environ.get('QTTS_CODEC_LOOKAHEAD_FRAMES', '0'))
    except ValueError as error:
        raise ValueError('QTTS_CODEC_LOOKAHEAD_FRAMES must be 0..2') from error
    if not 0 <= value <= 2:
        raise ValueError('QTTS_CODEC_LOOKAHEAD_FRAMES must be 0..2')
    return value


class GeneratedCodecWindow:
    """25-frame left context; optional right lookahead. No repeated committed PCM."""
    def __init__(self, tokenizer, context=25, lookahead=0):
        if not 1 <= context <= 64 or not 0 <= lookahead <= 8:
            raise ValueError('invalid codec window')
        self.tokenizer, self.context, self.lookahead = tokenizer, context, lookahead
        self.codes = None
        self.start = self.total = self.committed = self.peak_frames = 0
        self.pending = np.zeros(0, np.float32)
        self.closed = False

    def push(self, chunk):
        import torch
        if self.closed:
            raise RuntimeError('codec window already finished')
        if chunk.ndim != 2 or chunk.shape[1] != 16 or not 1 <= chunk.shape[0] <= 16:
            raise RuntimeError('expected 1..16 GENERATED frames with 16 codebooks')
        window = chunk if self.codes is None else torch.cat((self.codes, chunk), dim=0)
        self.total += int(chunk.shape[0])
        self.peak_frames = max(self.peak_frames, int(window.shape[0]))
        if window.shape[0] > self.context + self.lookahead + 16:
            raise RuntimeError('codec window exceeded bounded context')
        audio_list, sr = self.tokenizer.decode({'audio_codes': window.unsqueeze(0)})
        audio = audio_list[0]
        if hasattr(audio, 'detach'):
            audio = audio.detach().float().cpu().numpy()
        audio = np.asarray(audio, dtype=np.float32).reshape(-1)
        if int(sr) != 24000 or len(audio) != window.shape[0] * 1920 or not np.isfinite(audio).all():
            raise RuntimeError('codec must return finite 24kHz PCM, exactly 1920 samples per generated frame')
        end = max(self.committed, self.total - self.lookahead)
        lo = (self.committed - self.start) * 1920
        hi = (end - self.start) * 1920
        out = audio[lo:hi].copy()
        self.pending = audio[hi:].copy()
        self.committed = end
        retain_from = max(0, end - self.context)
        self.codes = window[retain_from - self.start:].clone()
        self.start = retain_from
        return out

    def finish(self, cancelled=False):
        if self.closed:
            return np.zeros(0, np.float32)
        self.closed = True
        out = np.zeros(0, np.float32) if cancelled else self.pending
        self.pending = np.zeros(0, np.float32)
        self.codes = None
        return out


def generated_only_stream(model, *, text, language, ref_audio, ref_text, xvec_only,
                          chunk_size, max_new_tokens, temperature, top_k, top_p,
                          repetition_penalty, cancel, append_silence=False, voice_clone_prompt=None):
    """Local adapter, not a global monkeypatch. Retains Faster's real CUDA graphs."""
    import torch
    from faster_qwen3_tts.streaming import fast_generate_streaming
    if append_silence:
        raise ValueError('reference silence augmentation disabled')
    with torch.inference_mode():
        t0 = time.perf_counter()
        m, talker, config, tie, tam, tth, tpe, _reference_codes = model._prepare_generation(
            text=text, language=language, ref_audio=ref_audio, ref_text=ref_text,
            xvec_only=xvec_only, non_streaming_mode=False, append_silence=False,
            voice_clone_prompt=voice_clone_prompt, instruct=None)
        # _reference_codes are exclusively talker conditioning. Never passed to decode.
        window = GeneratedCodecWindow(m.speech_tokenizer, lookahead=codec_lookahead_frames())
        it = fast_generate_streaming(
            talker=talker, talker_input_embeds=tie, attention_mask=tam,
            trailing_text_hiddens=tth, tts_pad_embed=tpe, config=config,
            predictor_graph=model.predictor_graph, talker_graph=model.talker_graph,
            max_new_tokens=max_new_tokens, min_new_tokens=2, temperature=temperature,
            top_k=top_k, top_p=top_p, do_sample=True,
            repetition_penalty=repetition_penalty, chunk_size=chunk_size)
        prepare_ms = (time.perf_counter() - t0) * 1000
        try:
            for codes, timing in it:
                if cancel.is_set():
                    break
                t1 = time.perf_counter()
                audio = window.push(codes)
                report = dict(timing, prepare_ms=prepare_ms, codec_ms=(time.perf_counter()-t1)*1000,
                              codec_window_frames=window.peak_frames, lookahead_frames=window.lookahead,
                              reference_codes_decoded=0)
                if audio.size:
                    yield audio, 24000, report
            tail = window.finish(cancelled=cancel.is_set())
            if tail.size:
                yield tail, 24000, {'codec_ms': 0, 'reference_codes_decoded': 0,
                                    'codec_window_frames': window.peak_frames, 'is_final': True}
        finally:
            it.close()
            window.finish(cancelled=True)
