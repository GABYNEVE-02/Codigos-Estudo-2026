import os
from math import pi

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pasta = os.path.dirname(os.path.abspath(__file__))
caminho = os.path.join(pasta, "datasets", "bike.csv")

df = pd.read_csv(caminho)

temp_mean = np.mean(df["temp"])
wind_mean = np.mean(df["windspeed"])
hum_mean = np.mean(df["hum"])
cnt_mean = np.mean(df["cnt"])

temp_std = np.std(df["temp"])
wind_std = np.std(df["windspeed"])
hum_std = np.std(df["hum"])
cnt_std = np.std(df["cnt"])

X = []
Y = []
xb = 0
step = 10000 / 500

for i in range(500):
    X.append(xb)
    Y.append(
        (1 / (cnt_std * np.sqrt(2 * pi)))
        * np.exp(-((xb - cnt_mean) ** 2) / (2 * cnt_std**2))
    )
    xb += step

plt.figure(figsize=(12, 8))
plt.hist(
    df["cnt"],
    bins=30,
    alpha=0.5,
    label="Count",
    color="blue",
    edgecolor="black",
    density=True,
)
plt.axvline(
    cnt_mean,
    color="red",
    linestyle="dashed",
    linewidth=1,
    label=f"Mean: {cnt_mean:.2f}",
)
plt.plot(X, Y, color="green", label="Normal Distribution Fit")
plt.title(f"Count Distribution (Mean: {cnt_mean:.2f}, Std: {cnt_std:.2f})")
plt.xlabel("Count")
plt.ylabel("Frequency")
plt.legend()
plt.show()
