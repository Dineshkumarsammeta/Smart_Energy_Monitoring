"""
Replay script for Smart Energy Monitoring.
Reads from a sample CSV and plots energy data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

def replay_log(file_path="metrics/snapshot.csv", output_dir="output"):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Read CSV
    df = pd.read_csv(file_path)
    print("Loaded snapshot data:")
    print(df.head())

    # Save a copy of the CSV to output folder
    output_csv = os.path.join(output_dir, "snapshot_copy.csv")
    df.to_csv(output_csv, index=False)
    print(f"CSV saved to: {output_csv}")

    # Quick plot
    df.plot(x="timestamp", y=["Power", "HVAC"], kind="line", marker="o")
    plt.title("Smart Energy Monitoring – Replay Demo")
    plt.xlabel("Time")
    plt.ylabel("Consumption (W)")
    plt.grid(True)

    # Save plot as PNG
    output_png = os.path.join(output_dir, "energy_plot.png")
    plt.savefig(output_png)
    print(f"Plot saved to: {output_png}")
    plt.show()

if __name__ == "__main__":
    replay_log()

