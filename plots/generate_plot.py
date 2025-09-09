import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("plots", exist_ok=True)

df = pd.read_csv("data/sample.csv")
plt.figure(figsize=(8,4))
plt.plot(pd.to_datetime(df['timestamp']), df['load_kW'], marker='o', linestyle='-')
plt.title("Synthetic Hospital Load (kW) Over Time")
plt.xlabel("Time")
plt.ylabel("Load (kW)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/load_chart.png")
plt.close()
print("Plot saved: plots/load_chart.png")
