import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
AutoMinorLocator)
import numpy as np
from scipy import interpolate
#библиотеки

#реализация выбора
print("1 - Вывести график на экран")
print("2 - Сохранить график на рабочий стол")
proverca = int(input())

V_a1 = [1.18, 19.70, 76.50, 115.8, 175.1, 194.58, 195.50, 191.50, 187.3, 181.02, 175.8, 165.2, 153.7, 145.6, 135.1, 129.8, 124.4, 119.4, 114.5, 111.6, 107.8, 104.8, 102.8, 100.1, 97.3, 94.4, 88.8, 85.25, 81.5, 78.01, 74.50, 72.58, 71.12, 70.27, 68.95, 67.5, 66.62, 66.17, 66.32, 65.86, 65.88, 65.81, 66.50, 67.36, 68.50, 70.38, 73.48, 76, 77.85, 80.67, 82.9, 84.58, 87.96, 93.72, 104.04, 111.4, 116.50, 118.65, 119.8]
V_k1 = [0.582, 0.853, 1.086, 1.212, 1.467, 1.665, 1.779, 1.890, 1.965, 2.054, 2.112, 2.250, 2.403, 2.515, 2.681, 2.774, 2.876, 2.977, 3.092, 3.157, 3.264, 3.352, 3.413, 3.508, 3.607, 3.705, 3.944, 4.135, 4.338, 4.598, 4.875, 5.090, 5.266, 5.421, 5.664, 5.872, 6.063, 6.268, 6.640, 6.875, 7.075, 7.248, 7.491, 7.650, 7.832, 8.024, 8.263, 8.485, 8.649, 8.862, 9.090, 9.257, 9.462, 9.650, 9.877, 10.068, 10.260, 10.468, 10.660]

V_a2 = [0.43, 2.44, 8.06, 22.97, 43.89, 70.39, 81.7, 112.8, 132.1, 144.1, 164.2, 173.6, 180.80, 182.19, 178.18, 172.22, 164.6, 156.7, 150.71, 133.5, 109.5, 98.55, 86.08, 74.94, 65.06, 57.30, 52.92, 47.97, 45.19, 42.13, 39.78, 38.02, 36.07, 35.05, 33.95, 33.44, 32.63, 32.32, 31.75, 31.35, 31.29, 31.05, 30.90, 30.91, 31.07, 31.35, 32.15, 32.87, 33.57, 34.39, 35.57, 36.92, 38.1, 39, 40.32, 44.2, 48.35, 54.73, 55.64, 56.43, 57.13, 59.05, 64.4, 74.8]
V_k2 = [0.6, 0.75, 0.858, 0.971, 1.009, 1.168, 1.205, 1.317, 1.388, 1.439, 1.545, 1.62, 1.721, 1.822, 1.925, 2.014, 2.101, 2.178, 2.233, 2.392, 2.668, 2.811, 2.999, 3.201, 3.435, 3.674, 3.818, 4.031, 4.204, 4.419, 4.66, 4.844, 5.067, 5.267, 5.503, 5.623, 5.880, 6.003, 6.248, 6.465, 6.672, 6.861, 7.061, 7.214, 7.478, 7.652, 7.801, 8.033, 8.232, 8.433, 8.635, 8.850, 9.022, 9.208, 9.44, 9.665, 9.815, 10.185, 10.26, 10.509, 10.634, 10.825, 11.077, 11.550]

r = 110 #кОм
I_a1 = [v / r for v in V_a1]
I_a2 = [v / r for v in V_a2]

I0 = 1.777
w = [- np.log(i / I0) / 5.3 for i in I_a1]
w2 = [- np.log(i / I0) / 6.3 for i in I_a2]
w_eror = [0.1/r * pow(1 / i**2 + 1 / I0, 0.5) / 5.3 for i in I_a1]
w_eror2 = [0.1/r * pow(1 / i**2 + 1 / I0, 0.5) / 6.3 for i in I_a2]

h = 6.62e-34  #Дж * с
m = 9.1e-31 #кг
e = 1.6e-19   #Кл

E1 = 2 #1.7   #2.5
E2 = 6.5 #7.2   #6
Eproboy = 10 #12
U0 = 2.5

l1 = 0.5 * (h / pow(2 * m * (E1 + U0) * e, 0.5))
l2 = 0.75 * (h / pow(2 * m * (E2 + U0) * e, 0.5))
l = (h * np.sqrt(5)/ pow(32 * m * (E2 - E1) * e, 0.5))
U = 0.8 * E2 - 1.8 * E1
print(l1, l2, l, U)

print(max(I_a1), max(I_a2))
print(min(I_a1[20:-1]), min((I_a2[20:-1])))

I_a1_eror = np.empty(len(I_a1))
I_a1_eror.fill(0.1 / r)

V_k1_eror = np.empty(len(V_k1))
V_k1_eror.fill(0.001)

I_a2_eror = np.empty(len(I_a2))
I_a2_eror.fill(0.1 / r)

V_k2_eror = np.empty(len(V_k2))
V_k2_eror.fill(0.001)

# x1 = 2.51, 2.58, 2.67, 2.78, 2.87, 2.94, 3.03, 3.12, 3.23, 3.32, 3.41, 3.48, 3.57, 3.68, 3.75, 3.86, 3.93, 4.02, 4.13, 4.22, 4.31, 4.38, 4.47, 4.56, 4.67, 4.74, 4.85, 4.92, 5.01, 5.12, 5.21
# y1 = 50.2, 50.97, 51.75, 55.15, 56.17, 52.81, 56.08, 56.95, 58.06, 59.39, 60.32, 63.7, 60.89, 66.29, 65.13, 66.79, 65.88, 71.38, 68.32, 71.89, 75.27, 76.48, 76.32, 75.79, 76.88, 82.41, 81.96, 83.55, 87.16, 89.21, 88.89

#x2 = 206.06928,	397.01424,	579.65056,	745.15392,	884.7,	989.46448,	1044.576039
#y2 = 4.5, 9, 16.5, 21, 27, 28.5, 30

#x3 = 206.06928,	397.01424,	579.65056,	745.15392,	884.7,	989.46448,	1044.576039
#y3 = 9, 16.5, 27, 34.5, 40.5, 45, 46.5

#x4 = 206.06928,	397.01424,	579.65056,	745.15392,	884.7,	989.46448,	1044.576039
#y4 = 10.5, 21, 33, 45, 52.5, 57, 60

#x5 = 206.06928,	397.01424,	579.65056,	745.15392,	884.7,	989.46448,	1044.576039
#y5 = 12, 28.5, 43.5, 57, 66, 73.5, 78

#x6 = 206.06928,	397.01424,	579.65056,	745.15392,	884.7,	989.46448,	1044.576039
#y6 = 13.5, 33, 49.5, 66, 78, 88.5, 91.5



#xerr1=np.array([3.09104, 5.95521, 8.69476, 11.1773, 13.2705, 14.842])
#yerr1=np.array([1.5, 1.5, 1.5, 1.5, 1.5, 1.5])

#xerr2=np.array([3.09104, 5.95521, 8.69476, 11.1773, 13.2705, 14.842, 15.6686])
#yerr2=np.array([1.5,	1.5,	1.5,	1.5,	1.5,	1.5,	1.5])

#xerr3=np.array([3.09104, 5.95521, 8.69476, 11.1773, 13.2705, 14.842, 15.6686])
#yerr3=np.array([1.5,	1.5,	1.5,	1.5,	1.5,	1.5,	1.5])

#xerr4=np.array([3.09104, 5.95521, 8.69476, 11.1773, 13.2705, 14.842, 15.6686])
#yerr4=np.array([1.5,	1.5,	1.5,	1.5,	1.5,	1.5,	1.5])

#xerr5=np.array([3.09104, 5.95521, 8.69476, 11.1773, 13.2705, 14.842, 15.6686])
#yerr5=np.array([1.5,	1.5,	1.5,	1.5,	1.5,	1.5,	1.5])

#xerr6=np.array([3.09104, 5.95521, 8.69476, 11.1773, 13.2705, 14.842, 15.6686])
#yerr6=np.array([1.5,	1.5,	1.5,	1.5,	1.5,	1.5,	1.5])




# tochki1 = np.linspace(Ua_4[0], Ua_4[-1], 10000)
#tochki2 = np.linspace(x2[0], x2[-1], 10000)
#tochki3 = np.linspace(x3[0], x3[-1], 10000)
#tochki4 = np.linspace(x4[0], x4[-1], 10000)
#tochki5 = np.linspace(x5[0], x5[-1], 10000)
#tochki6 = np.linspace(x6[0], x6[-1], 10000)


# z1 = np.polyfit(Ua_4, Ik_4, 2)
# p1 = np.poly1d(z1)

#z2 = np.polyfit(x2, y2, 1)
#p2 = np.poly1d(z2)

#z3 = np.polyfit(x3, y3, 1)
#p3 = np.poly1d(z3)

#z4 = np.polyfit(x4, y4, 1)
#p4 = np.poly1d(z4)

#z5 = np.polyfit(x5, y5, 1)
#p5 = np.poly1d(z5)

#z6 = np.polyfit(x6, y6, 1)
#p6 = np.poly1d(z6)

L = V_k1[0]
R = V_k1[-1]
xh = np.linspace(L, R, 10000)
cubic = interpolate.interp1d(V_k1, I_a1, kind="cubic")
y_cubic = cubic(xh)

cubic_w = interpolate.interp1d(V_k1, w, kind="cubic")
y_cubic_w = cubic_w(xh)



L2 = V_k2[0]
R2 = V_k2[-1]
xh2 = np.linspace(L2, R2, 10000)
cubic2 = interpolate.interp1d(V_k2, I_a2, kind="cubic")
y_cubic2 = cubic2(xh2)

cubic_w2 = interpolate.interp1d(V_k2, w2, kind="cubic")
y_cubic_w2 = cubic_w2(xh2)


#fig, ax = plt.subplots(figsize=(10, 7))
if proverca == 1:
    fig, ax = plt.subplots(figsize=(10, 7))
else:
    fig, ax = plt.subplots(figsize=(10, 7), dpi = 600)
#для корректоного вывода на экан, не трогать


#plt.axis([16,32,0,4.6])
##обрезка координат


#ax.set_title("Зависимость остмотического давления от концентрации K4Fe(CN)6 в воде", fontsize=16)                    #название графика
ax.set_xlabel("$V_\\text{к-с}, В$", fontsize=14)                        #название оси х
ax.set_ylabel("$I_\\text{анод}, мА$", fontsize=14)     #название оси у

# ax.set_xlabel("$V_\\text{к-с}, В$", fontsize=14)                        #название оси х
# ax.set_ylabel("$w$", fontsize=14)     #название оси у
#названия и имена



#ax.set_yscale('log')
#логарифмический масштаб для оси Y



ax.grid(which="major", linewidth=1.3)                               #мажорная сетка
ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5) #минорная сетка
#создаём сетку для графика


ax.plot(V_k1, I_a1,"r.", markersize=1, label = '$V_\\text{накал} = 2.774В$')
ax.plot(xh, y_cubic,"b", markersize=1, label = 'Кубическая интерполяция')
ax.plot(V_k2, I_a2,"g.", markersize=1, label = '$V_\\text{накал} = 2.516В$')
ax.plot(xh2, y_cubic2,"y", markersize=1, label = 'Кубическая интерполяция')
ax.plot([1.75, 1.75], [0, 1.77],"b", markersize=8)
ax.plot([1.85, 1.85], [0, 1.65],"y", markersize=8)
ax.plot([7.1, 7.1], [0, 0.59],"b", markersize=8)
ax.plot([7.2, 7.2], [0, 0.28],"y", markersize=8)
# ax.plot(V_k1, w,"m.", markersize=1, label = 'вероятность рассеяния' )
# ax.plot(xh, y_cubic_w,"m", markersize=1, label = 'Кубическая интерполяция')
#
# ax.plot(V_k2, w2,"g.", markersize=1, label = 'вероятность рассеяния' )
# ax.plot(xh2, y_cubic_w2,"g", markersize=1, label = 'Кубическая интерполяция')

#строительство графика на рисунке
# ax.plot(tochki1, p1(tochki1), 'b--', label = '')
#ax.plot(tochki2, p2(tochki2), 'b--', label = '')
#ax.plot(tochki3, p3(tochki3), 'g--', label = '')
#ax.plot(tochki4, p4(tochki4), 'y--', label = '')
#ax.plot(tochki5, p5(tochki5), 'k--', label = '')
#ax.plot(tochki6, p6(tochki6), 'm--', label = '')


#ax.plot(x2, p2(x2), 'g--', label = 'Максимальный наклон кривой')
#ax.plot(x3, p3(x3), 'b--')
#в скобказ указываем точки графика для которого сторим линию тренда и функцию полинома
#строительство линии тренда
#ax.set_xticks(numpy.arange(0, 1000, 10))
#ax.set_yticks(numpy.arange(0, 1., 0.1))
ax.legend()
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(which='major', length=10, width=1)
ax.tick_params(which='minor', length=5, width=1)
#строительство минорной и мажорной сетки

ax.errorbar(V_k1, I_a1,
xerr=V_k1_eror,
yerr=I_a1_eror,
fmt='+', color='red', markersize=5)

ax.errorbar(V_k2, I_a2,
xerr=V_k2_eror,
yerr=I_a2_eror,
fmt='+', color='green', markersize=5)

# ax.errorbar(V_k1, w,
# xerr=V_k1_eror,
# yerr=w_eror,
# fmt='+', color='r', markersize=5)
#
# ax.errorbar(V_k2, w2,
# xerr=V_k2_eror,
# yerr=w_eror2,
# fmt='+', color='r', markersize=5)

#ax.errorbar(x4, y4,
#xerr=xerr4,
#yerr=yerr4,
#fmt='.', color='yellow', markersize=5)

#ax.errorbar(x5, y5,
#xerr=xerr5,
#yerr=yerr5,
#fmt='.', color='black', markersize=5)

#ax.errorbar(x6, y6,
#xerr=xerr6,
#yerr=yerr6,
#fmt='.', color='purple', markersize=5)






if proverca == 1:
    plt.show()
else:
    plt.savefig("I(V)")
