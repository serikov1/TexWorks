import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
AutoMinorLocator)
# import math
# import array
import numpy as np
# from scipy.interpolate import interp1d

#реализация выбора
print("1 - Вывести график на экран")
print("2 - Сохранить график на рабочий стол")
proverca = int(input())


N_fon = 385
N_open_15 = 116041
N_open_16 = 118414

N_0 = N_open_15 - N_fon

n1 = [1521 / 4, 1476 / 4, 1549 / 4, 1604 / 4, 1553 / 4] # измерение фона
n2 = [119286, 117668, 115375, 114351, 113526] # открытый каллиматор

n3 = [63341, 63249, 62866, 62804, 62988] # d = 4.5мм
n4 = [35296, 35328, 34727, 34980, 35192] # d = 9.5мм
n5 = [20833, 21217, 21028, 21237, 20855] # d = 14.0мм
n6 = [13159, 12879, 13223, 12799, 12901] # d = 19.0мм
n7 = [7409, 7414, 7568, 7594, 7324] # d = 24.0мм
n8 = [4114, 4210, 4182, 4104, 4173] # d = 29.0мм

n9 = [60490, 60496, 60721, 60821, 60765] # d = 10.3мм
n10 = [34326, 34083, 34643, 34649, 34601] # d = 20.5мм
n11 = [20032, 20017, 20216, 19920, 20224] # d = 30.5мм
n12 = [11627, 11747, 11814, 11738, 11826] # d = 40.6мм
n13 = [6812, 6807, 6865, 6921, 6819] # d = 50.8мм
n14 = [4089, 4143, 4137, 4322, 4073] # d = 61.2мм

n15 = [73609, 73753, 73311, 72419, 72784] # d = 20.2мм
n16 = [47980, 48101, 48151, 47688, 48021] # d = 40.1мм
n17 = [32223, 32937, 33051, 31711, 31897] # d = 60.2мм
n18 = [21359, 21585, 21423, 21572, 21698] # d = 80.3мм
n19 = [14755, 14832, 14976, 14733, 14855] # d = 100.5мм

n20 = [112080, 109474, 109393, 109608, 109132] # d = 24.7мм
n21 = [105602, 106388, 105002, 106197, 105960] # d = 44.4мм
n22 = [103133, 103245, 102893, 103591, 102547] # d = 64.4мм
n23 = [100900, 101702, 102039, 101577, 101004] # d = 83.7мм


l_pb = [4.5, 9.5, 14, 19, 24, 29]  #есть еще 190мм
N_pb = [63050, 35105, 21052, 12992, 7462, 4157, 360]
nu_pb = [0.1348204, 0.1255028, 0.1216874, 0.1161366, 0.1148789, 0.1146836, 0.0303803]
ln_pb = [11.04, 10.45, 9.93, 9.44, 8.86, 8.23]
print('pb = ',[i * 10 for i in nu_pb])


l_fe = [10.3, 20.5, 30.5, 40.6, 50.8, 61.2]
N_fe = [60659, 34460, 20081, 11750, 6844, 4153]
nu_fe = [0, 0, 0, 0, 0, 0]
ln_fe = [0, 0, 0, 0, 0, 0]
for l, n, i in zip(l_fe, N_fe, range(6)):
    nu_fe[i] = 10/l * np.log((N_open_15 - N_fon)/(n - N_fon))
    ln_fe[i] = np.log((n - N_fon))
print('fe = ',nu_fe)

l_al = [20.2, 40.1, 60.2, 80.3, 100.5]
N_al = [73175, 47988, 32163, 21527, 14830]
nu_al = [0, 0, 0, 0, 0]
ln_al = [0, 0, 0, 0, 0]

for l, n, i in zip(l_al, N_al, range(5)):
    nu_al[i] = 10/l * np.log((N_open_15 - N_fon)/(n - N_fon))
    ln_al[i] = np.log((n - N_fon))
print('al = ',nu_al)

l_tr = [24.7, 44.4, 64.4, 83.7]
N_tr = [109937, 105829, 103081, 101440]
nu_tr = [0, 0, 0, 0]
ln_tr = [0, 0, 0, 0]

for l, n, i in zip(l_tr, N_tr, range(4)):
    nu_tr[i] = 10/l * np.log((N_open_15 - N_fon)/(n - N_fon))
    ln_tr[i] = np.log((n - N_fon))
print('tr = ',nu_tr)


# погрешность среднего
delta = 0
def calculate_delta_medium(x, x_medium, N):
    a = 0
    for i in range(N):
        a += (x_medium - x[i])**2
    return pow(a / pow(N * (N - 1), 0.5), 0.5)

d1 =calculate_delta_medium(n1, N_0, 5)
d2 =calculate_delta_medium(n2, N_open_15, 5)
d3 =calculate_delta_medium(n3, N_pb[0], 5)
d4 =calculate_delta_medium(n4, N_pb[1], 5)
d5 =calculate_delta_medium(n5, N_pb[2], 5)
d6 =calculate_delta_medium(n6, N_pb[3], 5)
d7 =calculate_delta_medium(n7, N_pb[4], 5)
d8 =calculate_delta_medium(n8, N_pb[5], 5)

d9 =calculate_delta_medium(n9, N_fe[0], 5)
d10 =calculate_delta_medium(n10, N_fe[1], 5)
d11 =calculate_delta_medium(n11, N_fe[2], 5)
d12 =calculate_delta_medium(n12, N_fe[3], 5)
d13 =calculate_delta_medium(n13, N_fe[4], 5)
d14 =calculate_delta_medium(n14, N_fe[5], 5)

d15 =calculate_delta_medium(n15, N_al[0], 5)
d16 =calculate_delta_medium(n16, N_al[1], 5)
d17 =calculate_delta_medium(n17, N_al[2], 5)
d18 =calculate_delta_medium(n18, N_al[3], 5)
d19 =calculate_delta_medium(n19, N_al[4], 5)

d20 =calculate_delta_medium(n20, N_tr[0], 5)
d21 =calculate_delta_medium(n21, N_tr[1], 5)
d22 =calculate_delta_medium(n22, N_tr[2], 5)
d23 =calculate_delta_medium(n23, N_tr[3], 5)

xerr1=np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
yerr1=np.array([d3 / N_pb[0], d4 / N_pb[1], d5 / N_pb[2], d6 / N_pb[3], d7 / N_pb[4], d8 / N_pb[5]])

xerr2=np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
yerr2=np.array([d9 / N_fe[0], d10 / N_fe[1], d11 / N_fe[2], d12 / N_fe[3], d13 / N_fe[4], d14 / N_fe[5]])

xerr3=np.array([0.1, 0.1, 0.1, 0.1, 0.1])
yerr3=np.array([d15 / N_al[0], d16 / N_al[1], d17 / N_al[2], d18 / N_al[3], d19 / N_al[4]])

xerr4=np.array([0.1, 0.1, 0.1, 0.1])
yerr4=np.array([d20 / N_tr[0], d21 / N_tr[1], d22 / N_tr[2], d23 / N_tr[3]])

tochki1 = np.linspace(l_pb[0], l_pb[-1], 10000)
tochki2 = np.linspace(l_fe[0], l_fe[-1], 10000)
tochki3 = np.linspace(l_al[0], l_al[-1], 10000)
tochki4 = np.linspace(l_tr[0], l_tr[-1], 10000)

z1 = np.polyfit(l_pb, ln_pb, 1)
p1 = np.poly1d(z1)
print('z1',z1)

z2 = np.polyfit(l_fe, ln_fe, 1)
p2 = np.poly1d(z2)
print('z2',z2)

z3 = np.polyfit(l_al, ln_al, 1)
p3 = np.poly1d(z3)
print('z3',z3)

z4 = np.polyfit(l_tr, ln_tr, 1)
p4 = np.poly1d(z4)
print('z4',z4)

if proverca == 1:
    fig, ax = plt.subplots(figsize=(10, 7))
else:
    fig, ax = plt.subplots(figsize=(10, 7), dpi = 600)
#для корректоного вывода на экан, не трогать

#ax.set_title("Зависимость логарифма считанных частиц от толщины пластин", fontsize=16)                    #название графика
ax.set_xlabel("$l$, мм", fontsize=14)                        #название оси х
ax.set_ylabel("$ln(N_0 - N_{фон})$", fontsize=14)     #название оси у


ax.grid(which="major", linewidth=1.3)                               #мажорная сетка
# ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5) #минорная сетка
#создаём сетку для графика
ax.plot(l_pb, ln_pb,"r.", markersize=8, label = 'Свинец: $\\mu = 1,13 \\pm 0,01 см^-1$')
ax.plot(l_fe, ln_fe,"b.", markersize=8, label = 'Железо: $\\mu = 0,545 \\pm 0,004 см^-1$' )
ax.plot(l_al, ln_al,"g.", markersize=8, label = 'Аллюминий: $\\mu = 0,201 \\pm 0,003 см^-1$' )
ax.plot(l_tr, ln_tr,"y.", markersize=8, label = 'Пробка: $\\mu = 0,013 \\pm 0,001 см^-1$')

ax.legend()
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(which='major', length=10, width=1)
ax.tick_params(which='minor', length=5, width=1)
#строительство минорной и мажорной сетки



ax.plot(tochki1, p1(tochki1), 'r--', label = '')
ax.plot(tochki2, p2(tochki2), 'b--', label = '')
ax.plot(tochki3, p3(tochki3), 'g--', label = '')
ax.plot(tochki4, p4(tochki4), 'y--', label = '')

ax.errorbar(l_pb, ln_pb,
xerr=xerr1,
yerr=yerr1,
fmt='.', color='red', markersize=5)

ax.errorbar(l_fe, ln_fe,
xerr=xerr2,
yerr=yerr2,
fmt='.', color='blue', markersize=5)

ax.errorbar(l_al, ln_al,
xerr=xerr3,
yerr=yerr3,
fmt='.', color='green', markersize=5)

ax.errorbar(l_tr, ln_tr,
xerr=xerr4,
yerr=yerr4,
fmt='.', color='yellow', markersize=5)

plt.savefig("graph")

if proverca == 1:
    plt.show()
else:
    plt.savefig("C:/Users/Keys/Desktop/Image.png")

