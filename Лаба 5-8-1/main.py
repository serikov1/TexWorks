import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import numpy as np

# import pandas as pd
# библиотеки

# реализация выбора
print("1 - Вывести график на экран")
print("2 - Сохранить график на рабочий стол")
proverca = int(input())

# V = [1.52, 1.69, 2.05, 2.49, 2.93, 3.42, 4.18, 5.26, 5.88, 6.85, 7.97, 8.98]
# I = [0.449, 0.474, 0.515, 0.565, 0.611, 0.661, 0.728, 0.82, 0.869, 0.942, 1.021, 1.087]
# T = [910, 1020, 1130, 1240, 1350, 1455, 1560, 1665, 1770, 1875, 1980, 2085]

V = [22.7, 34.14, 45.4, 58.97, 70.15, 75.64, 83.76, 104.01, 116.31, 132.94]
I = [0.733, 0.852, 0.926, 1.059, 1.162, 1.245, 1.311, 1.346, 1.451, 1.535]
T = [930, 1130, 1200, 1360, 1500, 1650, 1760, 1900, 2010, 2100]
T = [t + 273 for t in T]
print(T)

W = [(v * i) for v, i in zip(V, I)]
lnW = [np.log(v * i) for v, i in zip(V, I)]
lnT = [np.log(t) for t in T]

tochki1 = np.linspace(lnT[0], lnT[-1], 10000)

z1 = np.polyfit(lnT, lnW, 1)
p1 = np.poly1d(z1)

# print(z1)
n = format(z1[0], ".3f")


def E(t):
    # if t == T[-1]: return 0.43
    # if t == T[-2]: return 0.436
    # if t == T[-3]: return 0.438
    # if t == T[-4]: return 0.44

    if t == T[-1]: return 0.43
    if t == T[-2]: return 0.432
    if t == T[-3]: return 0.434
    if t == T[-4]: return 0.436
    if t == T[-5]: return 0.437
    if t == T[-6]: return 0.439


def sigma(t):
    if t == T[-1]: return W[-1] / (E(t) * t ** 4 * 0.36)
    if t == T[-2]: return W[-2] / (E(t) * t ** 4 * 0.36)
    if t == T[-3]: return W[-3] / (E(t) * t ** 4 * 0.36)
    if t == T[-4]: return W[-4] / (E(t) * t ** 4 * 0.36)
    if t == T[-5]: return W[-5] / (E(t) * t ** 4 * 0.36)
    if t == T[-6]: return W[-6] / (E(t) * t ** 4 * 0.36)
    # if t == T[-4]: return W[-4] / (E(t) * t**4 * 0.36)


kb = 1.38 * 1e-23
c = 3 * 1e10


def h(T):
    return (2 * np.pi ** 5 * kb ** 4 / (15 * c ** 2 * sigma(T))) ** (1 / 3)


# print("h(T = 2085K) = ", h(T[-1]), "sigma = ", sigma(T[-1]))
# print("h(T = 1980K) = ", h(T[-2]), "sigma = ", sigma(T[-2]))
# print("h(T = 1875K) = ", h(T[-3]), "sigma = ", sigma(T[-3]))
# print("h(T = 1770K) = ", h(T[-4]), "sigma = ", sigma(T[-4]))
print("h(T = 2373K) = ", h(T[-1]), "sigma = ", sigma(T[-1]))
print("h(T = 2283K) = ", h(T[-2]), "sigma = ", sigma(T[-2]))
print("h(T = 2173K) = ", h(T[-3]), "sigma = ", sigma(T[-3]))
print("h(T = 2033K) = ", h(T[-4]), "sigma = ", sigma(T[-4]))
print("h(T = 1923K) = ", h(T[-5]), "sigma = ", sigma(T[-5]))
print("h(T = 1773K) = ", h(T[-6]), "sigma = ", sigma(T[-6]))

xerr1 = [0.001 * t for t in lnT]
yerr1 = [abs(2 / w) for w in W]

# fig, ax = plt.subplots(figsize=(10, 7))
if proverca == 1:
    fig, ax = plt.subplots(figsize=(10, 7))
else:
    fig, ax = plt.subplots(figsize=(10, 7), dpi=600)
# для корректоного вывода на экан, не трогать


# plt.axis([16,32,0,4.6])
##обрезка координат


# ax.set_title("Зависимость остмотического давления от концентрации K4Fe(CN)6 в воде", fontsize=16)                    #название графика
ax.set_xlabel("$\\ln(T)$", fontsize=14)  # название оси х
ax.set_ylabel("$\\ln(W)$", fontsize=14)  # название оси у
# названия и имена


# ax.set_yscale('log')
# логарифмический масштаб для оси Y


ax.grid(which="major", linewidth=1.3)  # мажорная сетка
ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)  # минорная сетка
# создаём сетку для графика


ax.plot(lnT, lnW, "r.", markersize=8, label='n$\\alpha$ = {}'.format(n))
# строительство графика на рисунке
ax.plot(tochki1, p1(tochki1), 'b--', label='')

ax.legend()
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(which='major', length=10, width=1)
ax.tick_params(which='minor', length=5, width=1)
# строительство минорной и мажорной сетки

ax.errorbar(lnT, lnW,
            xerr=xerr1,
            yerr=yerr1,
            fmt='.', color='red', markersize=5)

if proverca == 1:
    plt.show()
else:
    plt.savefig("W.png")
