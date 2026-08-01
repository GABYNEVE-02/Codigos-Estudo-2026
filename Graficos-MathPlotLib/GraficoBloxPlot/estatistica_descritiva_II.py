import os
from math import pi

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

pasta = os.path.dirname(os.path.abspath(__file__))
caminho = os.path.join(pasta, "datasets", "bike.csv")

df = pd.read_csv(caminho)

while True:
    config = input(
        "Enter configuration (correlação(1), histograma(2), boxplot(3)): "
    ).lower()

    if config == "1" or config == "correlação":
        c_eixox = input("Enter x-axis variable (temp, windspeed, hum, cnt): ").lower()
        c_eixoy = input("Enter y-axis variable (temp, windspeed, hum, cnt): ").lower()

        A, B, r, p, se = stats.linregress(df[c_eixox], df[c_eixoy])

        plt.figure(figsize=(12, 8))
        plt.scatter(
            df[c_eixox],
            df[c_eixoy],
            alpha=0.5,
            label="Data Points",
            color="blue",
            s=50,
        )
        plt.plot(
            df[c_eixox],
            A * df[c_eixox] + B,
            color="red",
            label=f"Regression Line (r={r:.2f})",
        )
        plt.title(
            f"{c_eixox.capitalize()} vs {c_eixoy.capitalize()} (Correlation: {r:.2f})"
        )
        plt.xlabel(c_eixox.capitalize())
        plt.ylabel(c_eixoy.capitalize())
        plt.legend()
        plt.show()

        break

    elif config == "2" or config == "histograma":
        while True:
            h_eixo = input(
                "Enter variable for histogram (temp, windspeed, hum, cnt): "
            ).lower()
            if h_eixo in df.columns:
                mean = np.mean(df[h_eixo])
                std = np.std(df[h_eixo])
                break

            else:
                print("Invalid variable. Please choose from temp, windspeed, hum, cnt.")

        X = []
        Y = []
        xb = 0

        if h_eixo == "cnt":
            step = 10000 / 500
            for i in range(500):
                X.append(xb)
                Y.append(
                    (1 / (std * np.sqrt(2 * pi)))
                    * np.exp(-((xb - mean) ** 2) / (2 * std**2))
                )
                xb += step
        elif h_eixo == "hum":
            step = 100 / 70
            for i in range(70):
                X.append(xb)
                Y.append(
                    (1 / (std * np.sqrt(2 * pi)))
                    * np.exp(-((xb - mean) ** 2) / (2 * std**2))
                )
                xb += step

        else:
            step = 50 / 70
            for i in range(70):
                X.append(xb)
                Y.append(
                    (1 / (std * np.sqrt(2 * pi)))
                    * np.exp(-((xb - mean) ** 2) / (2 * std**2))
                )
                xb += step

        plt.figure(figsize=(12, 8))
        plt.hist(
            df[h_eixo],
            bins=30,
            alpha=0.5,
            label="Count",
            color="blue",
            edgecolor="black",
            density=True,
        )
        plt.axvline(
            df[h_eixo].mean(),
            color="red",
            linestyle="dashed",
            linewidth=1,
            label=f"Mean: {df[h_eixo].mean():.2f}",
        )
        plt.plot(X, Y, color="green", label="Normal Distribution Fit")
        plt.title(
            f"Count Distribution (Mean: {df[h_eixo].mean():.2f}, Std: {df[h_eixo].std():.2f})"
        )
        plt.xlabel(h_eixo.capitalize())
        plt.ylabel("Frequency")
        plt.legend()
        plt.show()
        break

    elif config == "3" or config == "boxplot":
        while True:
            b_eixo = input(
                "Enter variable for boxplot (temp, windspeed, hum, cnt): "
            ).lower()
            if b_eixo in df.columns:
                mean = np.mean(df[b_eixo])
                std = np.std(df[b_eixo])
                median = np.median(df[b_eixo])
                break
            else:
                print("Invalid variable. Please choose from temp, windspeed, hum, cnt.")

        plt.figure(figsize=(12, 8))
        plt.boxplot(df[b_eixo])
        plt.title(
            f"Boxplot of {b_eixo.capitalize()} (Mean: {mean:.2f}, Std: {std:.2f}, Median: {median:.2f})"
        )
        plt.ylabel(f"{b_eixo.capitalize()} Distribution")
        plt.show()

        break
