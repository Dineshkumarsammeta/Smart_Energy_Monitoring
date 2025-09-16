# Hardware-safe CI test: parses a short RS-485-like stream, computes metrics,
# and writes metrics/metrics.csv for recruiters to verify.
import os, re, csv
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from energy.rs485.mock_port import MockSerial

FRAME_RE = re.compile(r"V=(?P<V>[0-9.]+);I=(?P<I>[0-9.]+);P=(?P<P>[0-9.]+);ts=(?P<ts>[0-9.]+)")

def parse_frame(bline: bytes):
    m = FRAME_RE.search(bline.decode('utf-8').strip())
    assert m, f"Bad frame: {bline!r}"
    return {"V": float(m['V']), "I": float(m['I']), "P": float(m['P']), "ts": float(m['ts'])}

def median(vals):
    vals = sorted(vals); n = len(vals)
    return (vals[n//2-1] + vals[n//2]) / 2.0 if n % 2 == 0 else vals[n//2]

def test_mock_rs485_stream_and_metrics(tmp_path: Path):
    port = MockSerial(fps=20.0, frames=40, seed=123)
    parsed, ts = [], []
    for b in port.frames_iter():
        row = parse_frame(b); parsed.append(row); ts.append(row["ts"])
    assert len(parsed) == 40

    mean_power_kw = sum(p["P"] for p in parsed)/len(parsed)
    peak_kw = max(p["P"] for p in parsed)
    deltas = [j - i for i, j in zip(ts[:-1], ts[1:])]
    p50_ms = median(deltas) * 1000.0

    assert 0.0 < mean_power_kw < 1.0
    assert 0.0 < peak_kw < 1.5
    assert 0.0 < p50_ms < 200.0  # ~50 ms at 20 FPS

    metrics_dir = Path("metrics"); metrics_dir.mkdir(parents=True, exist_ok=True)
    out = metrics_dir / "metrics.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["metric","value"])
        w.writerow(["samples_total", len(parsed)])
        w.writerow(["mean_power_kw", round(mean_power_kw, 3)])
        w.writerow(["peak_kw", round(peak_kw, 3)])
        w.writerow(["interval_p50_ms", round(p50_ms, 1)])
        w.writerow(["data_completeness_pct", 100.0])
    assert out.exists()
