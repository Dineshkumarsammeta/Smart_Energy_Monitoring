import csv
import os
from pathlib import Path

SYNTHETIC_CSV = os.getenv("SYNTHETIC_CSV", "data/sample.csv")
REPLAY_LOG = "plots/replay_plot.csv"

os.makedirs("plots", exist_ok=True)

def replay_csv(csv_path=SYNTHETIC_CSV, output_path=REPLAY_LOG):
    with open(csv_path) as f_in, open(output_path, 'w', newline='') as f_out:
        reader = csv.reader(f_in)
        writer = csv.writer(f_out)
        header = next(reader)
        writer.writerow(header + ["status"])
        for row in reader:
            writer.writerow(row + ["OK"])
    print(f"Replay done: {output_path}")

if __name__ == "__main__":
    replay_csv()
