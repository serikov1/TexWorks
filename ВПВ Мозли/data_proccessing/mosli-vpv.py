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

K_l = [3031, 2749, 2503, 2289, 2105, 1935, 1660, 1540, 1435, 1339, 1255, 1040, 829, 747, 710, 558, 530, 515, 489]
K_b = [2780, 2514, 2283, 2084, 1910, 1755, 1500, 1390, 1294, 1207, 1130, 932,  741, 664, 630, 496, 475, 453, 427]
z_k = [21,   22,   23,   24,   25,   26,   28,   29,   30,   31,   32,   35,   39,  41,  42,  47,  48,  49,  50]

L_l = [1144, 1173, 1275, 1474, 1519, 1618, 1670, 1722, 1782, 1844, 1912, 1974, 2044, 2120, 2198, 2367, 2461, 2559, 2664]
L_b = [949,  982,  1080, 1279, 1324, 1422, 1475, 1528, 1584, 1647, 1713, 1775, 1844, 1918, 1998, 2164, 2254, 2352, 2454]
z_l = [83,   82,   79,   74,   73,   71,   70,   69,   68,   67,   66,   65,   64,   63,   62,   60,   59,   58,   57]

h = 6.62e-34  #Дж * с
e = 1.6e-19   #Кл
c = 3e8       # м / с
Ry = 13.6     #эВ

E_K_l = [h * c / (e * lamda * pow(10, -13)) for lamda in K_l]
f_K_l = [pow(lamda / Ry, 0.5) for lamda in E_K_l]
E_K_b = [h * c / (e * lamda * pow(10, -13)) for lamda in K_b]
f_K_b = [pow(lamda / Ry, 0.5) for lamda in E_K_b]

E_L_l = [h * c / (e * lamda * pow(10, -13)) for lamda in L_l]
f_L_l = [pow(lamda / Ry, 0.5) for lamda in E_L_l]
E_L_b = [h * c / (e * lamda * pow(10, -13)) for lamda in L_b]
f_L_b = [pow(lamda / Ry, 0.5) for lamda in E_L_b]

print(E_K_l)
print(E_K_b)
print(E_L_l)
print(E_L_b)

# k1 = (f_K_l[-1] - f_K_l[0])/(z_k[-1] - z_k[0])
# k2 = (f_K_b[-2] - f_K_b[0])/(z_k[-2] - z_k[0])
# k3 = (f_L_l[-1] - f_L_l[0])/(z_l[-1] - z_l[0])
# k4 = (f_L_b[-3] - f_L_b[0])/(z_l[-3] - z_l[0])
# print(k1, k2, k3, k4)

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




tochki1 = np.linspace(z_k[0], z_k[-1], 10000)
tochki2 = np.linspace(z_l[0], z_l[-1], 10000)
# tochki3 = np.linspace(x3[0], x3[-1], 10000)
# tochki4 = np.linspace(x4[0], x4[-1], 10000)
#tochki5 = np.linspace(x5[0], x5[-1], 10000)
#tochki6 = np.linspace(x6[0], x6[-1], 10000)


z1 = np.polyfit(z_k, f_K_l, 1)
p1 = np.poly1d(z1)
# print(z1)

z2 = np.polyfit(z_k, f_K_b, 1)
p2 = np.poly1d(z2)
# print(-p2[0]/z2[0])

z3 = np.polyfit(z_l, f_L_l, 1)
p3 = np.poly1d(z3)
# print(-p3[0]/z3[0])

z4 = np.polyfit(z_l, f_L_b, 1)
p4 = np.poly1d(z4)

print(-z1[1]/z1[0], -z2[1]/z2[0], -z3[1]/z3[0], -z4[1]/z4[0])

def sigma_k(f, x, k):
    ff = [y**2 for y in f]
    y_med = sum(f) / len(x)
    x_med = sum(x) / len(x)
    xx = [i**2 for i in x]
    y2_med = sum(ff) / len(x)
    x2_med = sum(xx) / len(x)
    # print(y2_med / x2_med, k)
    sigma = pow(((y2_med - y_med ** 2) / (x2_med - x_med**2) - k**2)/(len(x)), 0.5)
    return (sigma)

def sigma_b(x, s_k):
    xx = [i**2 for i in x]
    x2_med = sum(xx) / len(x)
    return (s_k * pow(x2_med, 0.5))


k1 = format(sigma_k(f_K_l, z_k, z1[0]) / z1[0], ".3f")
k2 = format(sigma_k(f_K_b, z_k, z2[0]) / z2[0], ".3f")
k3 = format(sigma_k(f_L_l, z_l, z3[0]) / z3[0], ".3f")
k4 = format(sigma_k(f_L_b, z_l, z4[0]) / z4[0], ".3f")

b1 = format(-sigma_b(z_k, sigma_k(f_K_l, z_k, z1[0])) / z1[1], ".2f")
b2 = format(-sigma_b(z_k, sigma_k(f_K_b, z_k, z2[0])) / z2[1], ".2f")
b3 = format(-sigma_b(z_l, sigma_k(f_L_l, z_l, z3[0])) / z3[1], ".2f")
b4 = format(-sigma_b(z_l, sigma_k(f_L_b, z_l, z4[0])) / z4[1], ".2f")

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
ax.set_xlabel("Z", fontsize=14)                        #название оси х
ax.set_ylabel("$\\sqrt{\\frac{E}{Ry}}$", fontsize=14)     #название оси у
#названия и имена



#ax.set_yscale('log')
#логарифмический масштаб для оси Y



ax.grid(which="major", linewidth=1.3)                               #мажорная сетка
ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5) #минорная сетка
#создаём сетку для графика


ax.plot(z_k, f_K_l,"r.", markersize=8, label = '')
ax.plot(z_k, f_K_b,"b.", markersize=8, label = '' )
ax.plot(z_l, f_L_l,"g.", markersize=8, label = '' )
ax.plot(z_l, f_L_b,"y.", markersize=8, label = '')
#ax.plot(x5, y5,"k.", markersize=8, label = 'Ток на образце 1.0 А' )
#ax.plot(x6, y6,"m.", markersize=8, label = 'Ток на образце 1.2 А' )
#строительство графика на рисунке
ax.plot(tochki1, p1(tochki1), 'r--', label = "$K_\\alpha : k = {} \\pm {}, b = {} \\pm {}$".format(format(z1[0], ".3f"), k1, format(z1[1], ".2f"), b1))
ax.plot(tochki1, p2(tochki1), 'b--', label = "$K_\\beta : k = {} \\pm {}, b = {} \\pm {}$".format(format(z2[0], ".3f"), k2, format(z2[1], ".2f"), b2))
ax.plot(tochki2, p3(tochki2), 'g--', label = "$L_\\alpha  : k = {} \\pm {}, b = {} \\pm {}$".format(format(z3[0], ".3f"), k3, format(z3[1], ".2f"), b3))
ax.plot(tochki2, p4(tochki2), 'y--', label = "$L_\\beta : k = {} \\pm {}, b = {} \\pm {}$".format(format(z4[0], ".3f"), k4, format(z4[1], ".2f"), b4))
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
    plt.savefig('ERy(z).png')
