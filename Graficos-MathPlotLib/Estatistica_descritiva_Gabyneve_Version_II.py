import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(pasta_atual, "datasets", "bike.csv")
df = pd.read_csv(caminho_csv)


def Regressao_Linear_Grafico(a, x, y):
    A, B, r, p, re = stats.linregress(x, y)

    xmin = min(x)
    xmax = max(x)

    axes[a].plot([xmin, xmax], [A * xmin + B, A * xmax + B], color="red")


Temperatura_Media = np.mean(df["temp"])
Velocidade_Do_Vento_Media = np.mean(df["windspeed"])
Humidade_Relativa_Media = np.mean(df["hum"])
Numero_De_Bikes_Media = np.mean(df["cnt"])

# Histogramas
figure, axes = plt.subplots(2, 2)

axes[0, 0].hist(
    df["temp"], bins=30, alpha=0.5, label="Temperatura", color="blue", edgecolor="black"
)
axes[0, 0].axvline(
    Temperatura_Media,
    color="red",
    linestyle="--",
    label=f"Média: {Temperatura_Media:.2f}",
)
axes[0, 0].legend()
axes[0, 0].set_title("Histograma da Temperatura")

axes[0, 1].hist(
    df["windspeed"],
    bins=30,
    alpha=0.5,
    label="Velocidade do vento",
    color="blue",
    edgecolor="black",
)
axes[0, 1].axvline(
    Velocidade_Do_Vento_Media,
    color="red",
    linestyle="--",
    label=f"Média: {Velocidade_Do_Vento_Media:.2f}",
)
axes[0, 1].legend()
axes[0, 1].set_title("Histograma da Velocidade do vento")

axes[1, 0].hist(
    df["hum"], bins=30, alpha=0.5, label="Umidade", color="blue", edgecolor="black"
)
axes[1, 0].axvline(
    Humidade_Relativa_Media,
    color="red",
    linestyle="--",
    label=f"Média: {Humidade_Relativa_Media:.2f}",
)
axes[1, 0].legend()
axes[1, 0].set_title("Histograma da Umidade")

axes[1, 1].hist(
    df["cnt"],
    bins=30,
    alpha=0.5,
    label="Número de Bikes",
    color="blue",
    edgecolor="black",
)
axes[1, 1].axvline(
    Numero_De_Bikes_Media,
    color="red",
    linestyle="--",
    label=f"Média: {Numero_De_Bikes_Media:.2f}",
)
axes[1, 1].legend()
axes[1, 1].set_title("Histograma do Número de Bikes")

# Scatter Plots

figure, axes = plt.subplots(1, 3)

axes[0].scatter(
    df["temp"],
    df["cnt"],
    color="blue",
    alpha=0.5,
    s=50,
    label="Temperatura x Número de Bikes",
)
axes[0].set_xlabel("Temperatura")
axes[0].set_ylabel("Número de Bikes")
axes[0].set_title("Temperatura x Número de Bikes")
Regressao_Linear_Grafico(0, df["temp"], df["cnt"])

axes[1].scatter(
    df["hum"],
    df["cnt"],
    color="blue",
    alpha=0.5,
    s=50,
    label="Umidade x Número de Bikes",
)
axes[1].set_xlabel("Umidade")
axes[1].set_ylabel("Número de Bikes")
axes[1].set_title("Umidade x Número de Bikes")
Regressao_Linear_Grafico(1, df["hum"], df["cnt"])

axes[2].scatter(
    df["windspeed"],
    df["cnt"],
    color="blue",
    alpha=0.5,
    s=50,
    label="windspeed x Número de Bikes",
)
axes[2].set_xlabel("windspeed")
axes[2].set_ylabel("Número de Bikes")
axes[2].set_title("windspeed x Número de Bikes")
Regressao_Linear_Grafico(2, df["windspeed"], df["cnt"])

plt.show()
