"""Isolated18 causal NumPy DSP. No PCM buffering and no native backend selection.

This repairs partition dependence; it is NOT acoustic or Rust-equivalence proof.
State uses Python float64 arithmetic, float32 inputs, ties-to-even int16 rounding.
"""
from __future__ import annotations

import math
import operator

import numpy as np

BACKEND = "numpy-causal-v1"


def _f32(x) -> np.ndarray:
    return np.ascontiguousarray(np.asarray(x, dtype=np.float32).reshape(-1))


def rms_dbfs(x) -> float:
    a = _f32(x)
    if not a.size:
        return -90.0
    return float(20 * np.log10(max(float(np.sqrt(np.mean(a.astype(np.float64) ** 2))), 1e-9)))


def peak(x) -> float:
    a = _f32(x)
    return float(np.max(np.abs(a))) if a.size else 0.0


def f32_to_i16(x) -> np.ndarray:
    return np.round(np.clip(_f32(x), -1.0, 1.0) * 32767.0).astype(np.int16)


def _length(value, name: str) -> int:
    if isinstance(value, (bool, np.bool_)):
        raise ValueError(f"{name} must be a nonnegative integer")
    try:
        n = operator.index(value)
    except TypeError as exc:
        raise ValueError(f"{name} must be a nonnegative integer") from exc
    if n < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return n


def _bounded(value, name: str, low: float, high: float) -> float:
    if isinstance(value, (bool, np.bool_)):
        raise ValueError(f"{name} must be finite within [{low}, {high}]")
    value = float(value)
    if not math.isfinite(value) or not low <= value <= high:
        raise ValueError(f"{name} must be finite within [{low}, {high}]")
    return value


class Leveler:
    """Causal DC blocker -> gated RMS AGC -> segment fade -> soft limiter.

    process emits one sample per input immediately, including incomplete RMS windows.
    start_segment only restarts the fade, never DC/RMS/gain. Positive flush emits an
    explicit tail and resets DC/last only; it is not a hidden RMS-window finalizer.
    """

    def __init__(self, sr: int, target_dbfs: float = -21.0,
                 max_gain_db: float = 9.0, min_gain_db: float = -9.0):
        self._closed = True
        self.sr = _length(sr, "sample rate")
        if not 8000 <= self.sr <= 384000:
            raise ValueError("sample rate must be within [8000, 384000]")
        self.target_dbfs = _bounded(target_dbfs, "target_dbfs", -40, -6)
        self._target = 10 ** (self.target_dbfs / 20)
        self._max = 10 ** (_bounded(max_gain_db, "max_gain_db", 0, 18) / 20)
        self._min = 10 ** (_bounded(min_gain_db, "min_gain_db", -24, 0) / 20)
        self._env = self._target
        self._gain = self._want = 1.0
        self._seen = 0
        self._last = self._prev_x = self._prev_y = 0.0
        self._fade_total = self._fade_left = 0
        # Positive half-up grid length, not Python's ties-to-even duration rounding.
        self._blk_len = max(32, int(self.sr * .01 + .5))
        self._blk_n = 0
        self._blk_sum = 0.0
        self._dc_r = 1.0 - 2.0 * math.pi * 20.0 / self.sr
        self._att = 1.0 - math.exp(-1.0 / (self.sr * .030))
        self._rel = 1.0 - math.exp(-1.0 / (self.sr * .600))
        self._gate = 10 ** (-46.0 / 20.0)
        self._closed = False

    def _open(self):
        if self._closed:
            raise RuntimeError("leveler is closed")

    def close(self):
        self._closed = True

    def start_segment(self, fade_samples: int | None = None):
        self._open()
        n = max(8, int(self.sr * .004)) if fade_samples is None else _length(fade_samples, "fade_samples")
        self._fade_total = self._fade_left = n

    def process(self, x) -> np.ndarray:
        self._open()
        a = _f32(x)
        out = np.empty(a.size, dtype=np.int16)
        if not a.size:
            return out
        px, py = self._prev_x, self._prev_y
        total, left = self._fade_total, self._fade_left
        count, power = self._blk_n, self._blk_sum
        env, gain, want, seen = self._env, self._gain, self._want, self._seen
        dc, block, gate = self._dc_r, self._blk_len, self._gate
        att, rel, target, low, high = self._att, self._rel, self._target, self._min, self._max
        finite, sqrt, cos, tanh, pi = math.isfinite, math.sqrt, math.cos, math.tanh, math.pi
        for i, sample in enumerate(a):
            value = float(sample)
            if not finite(value):
                value = 0.0
            y = value - px + dc * py
            px, py = value, y
            power += y * y
            count += 1
            if count == block:
                rms = sqrt(power / count)
                count, power = 0, 0.0
                if rms > gate:
                    env += (rms - env) * (.08 if seen < 60 else .012)
                    seen += 1
                    want = min(high, max(low, target / max(env, 1e-4)))
            gain += (want - gain) * (att if want < gain else rel)
            v = y * gain
            if left:
                v *= .5 - .5 * cos(pi * (total - left) / total)
                left -= 1
            magnitude = abs(v)
            if magnitude > .89:
                v = math.copysign(.89 + .1 * tanh((magnitude - .89) / .1), v)
            out[i] = round(v * 32767.0)
        self._prev_x, self._prev_y = px, py
        self._fade_left = left
        self._blk_n, self._blk_sum = count, power
        self._env, self._gain, self._want, self._seen = env, gain, want, seen
        self._last = v
        return out

    def flush(self, n: int = 192) -> np.ndarray:
        self._open()
        n = _length(n, "tail length")
        out = np.empty(n, dtype=np.int16)
        if not n:
            return out
        last = self._last
        for i in range(n):
            out[i] = round(last * (.5 + .5 * math.cos(math.pi * (i + 1) / n)) * 32767.0)
        self._last = self._prev_x = self._prev_y = 0.0
        return out

    @property
    def gain_db(self) -> float:
        self._open()
        return 20 * math.log10(max(self._gain, 1e-6))

    @property
    def env_dbfs(self) -> float:
        self._open()
        return 20 * math.log10(max(self._env, 1e-6))
