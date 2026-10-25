"""G0 read-only boundary witnesses. Local HTTP/NumPy/ASR fixtures, NOT voice acceptance.
Observed tests intentionally assert frozen defects; passing does not mean fixed.
"""
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import struct
import threading
import unittest
from types import SimpleNamespace
from unittest.mock import patch
import numpy as np
import test_reliability  # Established isolated state/mock setup; no model loading.
import analyst
import audio_rt
from reference_segments import prepare_segments

OBSERVATIONS = []


def frame(kind, payload):
    return struct.pack('<BI', kind, len(payload)) + payload


@contextmanager
def worker_http(body, status=200, fragmented=False):
    """Actual requests/TCP, finite local worker fixture; never starts a model."""
    received = []
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_args):
            pass
        def do_POST(self):
            received.append({'path': self.path, 'body': json.loads(self.rfile.read(int(self.headers['Content-Length'])))})
            self.send_response(status)
            if fragmented:
                self.send_header('Transfer-Encoding', 'chunked')
            else:
                self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            if fragmented:
                for i in range(0, len(body), 3):
                    part = body[i:i+3]
                    self.wfile.write(f'{len(part):x}\r\n'.encode() + part + b'\r\n')
                self.wfile.write(b'0\r\n\r\n')
            else:
                self.wfile.write(body)
            self.wfile.flush()
    server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
    thread = threading.Thread(target=lambda: server.serve_forever(poll_interval=.01))
    thread.start()
    try:
        with patch.object(analyst, 'WORKERS', [f'http://127.0.0.1:{server.server_port}']):
            yield received
    finally:
        server.shutdown()
        thread.join(timeout=3)
        server.server_close()
        if thread.is_alive():
            raise AssertionError('local worker fixture did not stop')


def window_case(words):
    y = np.full(32*16000, .03, np.float32)
    original = [{'start': 0., 'end': 32., 'text': 'UNALIGNED ORIGINAL', 'words': []}]
    def transcribe(audio, language):
        return 'zh', [{'start': 0., 'end': len(audio)/16000, 'text': '窗口', 'words': words}]
    return prepare_segments(y, original, '', transcribe)


class AnalysisBoundaryTests(unittest.TestCase):
    def test_observed_short_numpy_breath_length_and_broadcast(self):
        cases = []
        with patch.object(audio_rt, '_LIB', None):
            for n in range(1, 7):
                try:
                    out = audio_rt.breath(n, 24000, 7, -38.)
                    cases.append({'requested': n, 'returned': len(out)})
                except ValueError as error:
                    cases.append({'requested': n, 'exception': type(error).__name__})
        self.assertEqual(cases[0], {'requested': 1, 'returned': 6})
        self.assertTrue(all(row.get('exception') == 'ValueError' for row in cases[1:5]))
        self.assertEqual(cases[5], {'requested': 6, 'returned': 6})
        OBSERVATIONS.append({'id': 'F10', 'cases': cases, 'fixed': False,
                             'reference_pcm_played': False, 'user_hiss_root_cause_proven': False})

    def test_observed_retranscribed_optional_words_not_sanitized(self):
        malformed = [(0., .4, '窗', 'EXTRA')]
        with self.assertRaises(ValueError):
            window_case(malformed)
        _, segments, _ = window_case([(0., .4, None), (.6, .9, '口')])
        self.assertIsNone(segments[0]['words'][0][2])
        # Compare the existing short-segment branch with identical optional metadata.
        short = [{'start': 0., 'end': 2., 'text': '窗口', 'words': malformed}]
        _, cleaned, _ = prepare_segments(np.zeros(2*16000, np.float32), short, 'zh', lambda *_: self.fail('unexpected ASR'))
        self.assertEqual(cleaned[0]['words'], [])
        OBSERVATIONS.append({'id': 'F11', 'malformed_tuple_exception': 'ValueError',
                             'non_string_word_retained': True, 'short_branch_sanitizes_same_metadata': True,
                             'actual_whisper_executed': False, 'fixed': False})

    def test_observed_synth_full_accepts_http_failure_and_incomplete_stream(self):
        pcm = frame(1, np.asarray([1000, -1000], dtype='<i2').tobytes())
        cases = [('http-503', 503, pcm + frame(2, b'{}')),
                 ('partial-header', 200, pcm + b'\x02\x05'),
                 ('partial-payload', 200, pcm + struct.pack('<BI', 2, 20) + b'{'),
                 ('failed-stats', 200, pcm + frame(2, b'{"failed":true}')),
                 ('empty-success', 200, b'')]
        observed = []
        for name, status, body in cases:
            with self.subTest(case=name), worker_http(body, status) as received:
                y, stats = analyst.synth_full(0, 'fixture', '目标')
                self.assertEqual(len(y), 0 if name == 'empty-success' else 2)
                self.assertEqual(len(received), 1)
                if name == 'failed-stats':
                    self.assertIs(stats['failed'], True)
                observed.append({'case': name, 'http_status': status, 'returned_samples': len(y),
                                 'stats': stats, 'exception_raised': False})
        OBSERVATIONS.append({'id': 'F12', 'cases': observed, 'actual_local_http': True,
                             'actual_worker_model_executed': False, 'fixed': False})

    def test_protect_normal_breath_deterministic_finite_exact_length(self):
        with patch.object(audio_rt, '_LIB', None):
            for n in (6, 64, 1920, 24000):
                a = audio_rt.breath(n, 24000, 31, -38.)
                b = audio_rt.breath(n, 24000, 31, -38.)
                np.testing.assert_array_equal(a, b)
                self.assertEqual((len(a), a.dtype), (n, np.dtype('float32')))
                self.assertTrue(np.isfinite(a).all())
                self.assertLessEqual(float(np.max(np.abs(a))), .980001)

    def test_protect_pcm_conversion_layout_clipping_and_empty_meters(self):
        with patch.object(audio_rt, '_LIB', None):
            a = audio_rt._f32(np.arange(12).reshape(3, 4)[:, ::2])
            self.assertTrue(a.flags.c_contiguous)
            self.assertEqual(a.shape, (6,))
            self.assertEqual(audio_rt.rms_dbfs([]), -90.)
            self.assertEqual(audio_rt.peak([]), 0.)
            np.testing.assert_array_equal(audio_rt.f32_to_i16([-2, -1, 0, 1, 2]), [-32767, -32767, 0, 32767, 32767])

    def test_protect_leveler_empty_nonfinite_and_idempotent_close(self):
        with patch.object(audio_rt, '_LIB', None):
            lev = audio_rt.Leveler(24000, max_gain_db=6.)
            try:
                lev.start_segment()
                self.assertEqual(lev.process([]).dtype, np.dtype('int16'))
                out = lev.process([np.nan, np.inf, -np.inf, .1]*40)
                self.assertEqual(len(out), 160)
                self.assertTrue(np.isfinite(out).all())
                self.assertTrue(np.isfinite([lev.gain_db, lev.env_dbfs]).all())
                tail = lev.flush()
                self.assertEqual((len(tail), int(tail[-1])), (192, 0))
                np.testing.assert_array_equal(lev.flush(), np.zeros(192, np.int16))
            finally:
                lev.close()
                lev.close()

    def test_protect_leveler_hot_signal_length_and_saturation_bounds(self):
        with patch.object(audio_rt, '_LIB', None):
            lev = audio_rt.Leveler(24000, -18., max_gain_db=6.)
            try:
                lev.start_segment()
                y = lev.process(np.tile(np.array([4., -4.], np.float32), 2000))
                self.assertEqual((len(y), int(y[0])), (4000, 0))
                self.assertLessEqual(int(np.max(np.abs(y.astype(np.int32)))), 32441)
            finally:
                lev.close()

    def test_protect_retranscription_uses_window_audio_and_local_timestamps(self):
        seen = []
        def transcribe(y, _language):
            seen.append(len(y))
            return 'zh', [{'start': .1, 'end': 1., 'text': '窗', 'words': [(.1, .5, '窗')]}]
        language, segments, report = prepare_segments(np.full(32*16000, .02, np.float32),
            [{'start': 0., 'end': 32., 'text': 'DO NOT SLICE ORIGINAL', 'words': []}], '', transcribe)
        self.assertEqual(seen, [16*16000]*2)
        self.assertEqual(language, 'zh')
        self.assertEqual([s['text'] for s in segments], ['窗', '窗'])
        self.assertEqual(segments[1]['words'], [(16.1, 16.5, '窗')])
        self.assertEqual((report['asr_windows'], report['output_segments']), (2, 2))
        self.assertTrue(report['text_is_asr_not_human_verified'])

    def test_protect_short_tail_is_explicit_not_paired_with_original_text(self):
        seen = []
        def transcribe(y, _language):
            seen.append(len(y))
            return 'zh', [{'start': 0., 'end': 16., 'text': '窗口', 'words': []}]
        _, segments, report = prepare_segments(np.full(17*16000, .02, np.float32),
            [{'start': 0., 'end': 17., 'text': 'ORIGINAL FULL TEXT', 'words': []}], 'zh', transcribe)
        self.assertEqual(seen, [16*16000])
        self.assertEqual(report['short_tail_s'], 1.)
        self.assertEqual([s['text'] for s in segments], ['窗口'])

    def test_protect_explicit_worker_error_frame_raises(self):
        payload = json.dumps({'error': '显式错误'}, ensure_ascii=False).encode()
        with worker_http(frame(3, payload), fragmented=True):
            with self.assertRaisesRegex(RuntimeError, '显式错误'):
                analyst.synth_full(0, 'fixture', '目标')

    def test_protect_complete_fragmented_http_pcm_and_unicode_stats(self):
        pcm = np.asarray([1000, -1000, 32767, -32768], dtype='<i2')
        stats = {'text': '中文完成', 'failed': False}
        body = frame(1, pcm.tobytes()) + frame(2, json.dumps(stats, ensure_ascii=False).encode())
        with worker_http(body, fragmented=True) as received:
            y, got = analyst.synth_full(0, 'fixture', '目标', seed=71)
            np.testing.assert_array_equal(y, pcm.astype(np.float32)/32768.)
            self.assertEqual(got, stats)
            self.assertEqual(received[0]['body']['seed'], 71)
            self.assertEqual(received[0]['body']['text'], '目标')

    def test_protect_embedding_cache_canonical_input_and_copy_isolation(self):
        calls = []
        def embed(y):
            calls.append(y.copy())
            return np.asarray([1., 0.], np.float32)
        cache = analyst.BuildEmbeddingCache(SimpleNamespace(embed=embed))
        first = cache.embed(np.arange(8, dtype=np.float64)[::2])
        first[:] = -10
        hit = cache.embed(np.asarray([0, 2, 4, 6], np.float32))
        np.testing.assert_array_equal(hit, [1., 0.])
        hit[:] = -20
        np.testing.assert_array_equal(cache.embed(np.asarray([0, 2, 4, 6], np.float32)), [1., 0.])
        self.assertEqual((len(calls), cache.calls, cache.hits), (1, 1, 2))
        self.assertEqual(cache.report()['scope'], 'this-profile-build-only')


if __name__ == '__main__':
    unittest.main()
