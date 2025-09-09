"""
Replay script for Smart Energy Monitoring.
Reads from a sample CSV and plots energy data.
"""

import pandas as pd
import matplotlib.pyplot as plt

def replay_log(file_path="metrics/snapshot.csv"):
    df = pd.read_csv(file_path)
    print("Loaded snapshot data:")
    print(df.head())

    # Quick plot
    df.plot(x="timestamp", y=["Power", "HVAC"], kind="line", marker="o")
    plt.title("Smart Energy Monitoring – Replay Demo")
    plt.xlabel("Time")
    plt.ylabel("Consumption (W)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    replay_log()
