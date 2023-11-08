import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
AutoMinorLocator)
import numpy as np
# import pandas as pd
#библиотеки

#реализация выбора
print("1 - Вывести график на экран")
print("2 - Сохранить график на рабочий стол")
proverca = int(input())

N = [937, 877, 852, 777, 731, 588, 543, 477, 436, 394, 358, 333, 310]
O = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

y = [1 / k - 1 / 937 for k in N]
x = [1 - np.cos(o * 3.1415 / 180) for o in O]

m = 9.1e-31
c = 3e8
e = 1.6e-19

E = 0.661660 * 1 / (N[0] - N[9]) * N[9]
print(E)
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




tochki1 = np.linspace(x[0], x[-1], 10000)
#tochki2 = np.linspace(x2[0], x2[-1], 10000)
#tochki3 = np.linspace(x3[0], x3[-1], 10000)
#tochki4 = np.linspace(x4[0], x4[-1], 10000)
#tochki5 = np.linspace(x5[0], x5[-1], 10000)
#tochki6 = np.linspace(x6[0], x6[-1], 10000)


z1 = np.polyfit(x, y, 1)
p1 = np.poly1d(z1)
# print(z1)

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




#fig, ax = plt.subplots(figsize=(10, 7))
if proverca == 1:
    fig, ax = plt.subplots(figsize=(10, 7))
else:
    fig, ax = plt.subplots(figsize=(10, 7), dpi = 600)
#для корректоного вывода на экан, не трогать


#plt.axis([16,32,0,4.6])
##обрезка координат


#ax.set_title("Зависимость остмотического давления от концентрации K4Fe(CN)6 в воде", fontsize=16)                    #название графика
ax.set_xlabel("$1 - cos(\\theta)$", fontsize=14)                        #название оси х
ax.set_ylabel("$\\frac{1}{N(\\theta)} - \\frac{1}{N(0)}$", fontsize=14)     #название оси у
#названия и имена



#ax.set_yscale('log')
#логарифмический масштаб для оси Y



ax.grid(which="major", linewidth=1.3)                               #мажорная сетка
ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5) #минорная сетка
#создаём сетку для графика


ax.plot(x, y,"r.", markersize=8, label = 'Экспериментальные точки')
#ax.plot(x2, y2,"b.", markersize=8, label = 'Ток на образце 0.4 А' )
#ax.plot(x3, y3,"g.", markersize=8, label = 'Ток на образце 0.6 А' )
#ax.plot(x4, y4,"y.", markersize=8, label = 'Ток на образце 0.8 А')
#ax.plot(x5, y5,"k.", markersize=8, label = 'Ток на образце 1.0 А' )
#ax.plot(x6, y6,"m.", markersize=8, label = 'Ток на образце 1.2 А' )
#строительство графика на рисунке
ax.plot(tochki1, p1(tochki1), 'b', label = '$k = 1.431 \\cdot 10^{-3}$')
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

#ax.errorbar(x1, y1,
#xerr=xerr1,
#yerr=yerr1,
#fmt='.', color='red', markersize=5)

#ax.errorbar(x2, y2,
#xerr=xerr2,
#yerr=yerr2,
#fmt='.', color='blue', markersize=5)

#ax.errorbar(x3, y3,
#xerr=xerr3,
#yerr=yerr3,
#fmt='.', color='green', markersize=5)

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
    plt.savefig("C:/Users/Keys/Desktop/Image.png")
