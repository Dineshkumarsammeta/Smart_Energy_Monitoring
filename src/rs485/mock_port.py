# Minimal RS-485 mock for CI-friendly tests (no hardware required).
# Generates frames like: "V=234.12;I=0.456;P=0.107;ts=1694232000.123"
import time
from typing import Iterator, Optional

class MockSerial:
    def __init__(self, fps: float = 10.0, frames: int = 50, seed: Optional[int] = 42):
        self.fps = max(1e-3, float(fps))
        self.frames = int(frames)
        self._interval = 1.0 / self.fps
        self._rng = self._lcg(seed or 42)

    def _lcg(self, seed: int):
        a, c, m = 1664525, 1013904223, 2**32
        x = seed & 0xFFFFFFFF
        while True:
            x = (a * x + c) % m
            yield x / m

    def frames_iter(self) -> Iterator[bytes]:
        now = time.time()
        for i in range(self.frames):
            r1 = next(self._rng); r2 = next(self._rng)
            voltage = 200 + 60 * r1        # 200..260 V
            current = 0.1 + 1.9 * r2       # 0.1..2.0 A
            power_kw = (voltage * current) / 1000.0
            ts = now + i * self._interval
            payload = f"V={voltage:.2f};I={current:.3f};P={power_kw:.3f};ts={ts:.3f}\n"
            yield payload.encode("utf-8")
            time.sleep(0)  # cooperative
