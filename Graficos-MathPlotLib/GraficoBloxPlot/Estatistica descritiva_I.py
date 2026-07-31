import os
from math import pi

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(pasta_atual, "seeds.csv")
df = pd.read_csv(caminho_csv)

media = np.mean(df.length)
mediana = np.median(df.length)
moda = stats.mode(df.length)
desvio = np.std(df.length)

X = []
Y = []
xb = 4.85
step = 1.9 / 50

for i in range(50):
    X.append(xb)
    Y.append(
        (1 / (desvio * np.sqrt(2 * pi)))
        * np.exp(-((xb - media) ** 2) / (2 * desvio**2))
    )
    xb += step


plt.figure()
plt.hist(df.length, edgecolor="black", density=True)
plt.plot(X, Y)
plt.axvline(media, color="red", linestyle="--", linewidth=2)
plt.title("Length x Density")
plt.xlabel("Length")
plt.ylabel("Density")

plt.figure()
plt.boxplot(df.length)
plt.title("Length Boxplot")
plt.ylabel("Length Distribution")

plt.show()
