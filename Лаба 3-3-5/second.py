import matplotlib
import numpy
from matplotlib import pyplot
from scipy.interpolate import interp1d

matplotlib.use('TkAgg')

I_k = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1, 1.2]
B_k = [18.7, 150.2, 276.8, 386.9, 504, 614.5, 751.8, 900, 1031, 1153.6, 1220]

I_1 = [0.1, 0.19, 0.39, 0.6, 0.8, 1, 1.2]
U_1 = [4, 5, 6, 7, 8.5, 9, 10]
U_1 = [(x - 2) * 4 for x in U_1]

I_2 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.9, 1.1]
U_2 = [5, 6, 8, 9, 10.5, 13, 14, 16, 17]
U_2 = [(x - 3) * 4 for x in U_2]

I_3 = I_2
U_3 = [6, 8, 10.5, 12.5, 15, 17, 19, 22, 23]
U_3 = [(x - 4) * 4 for x in U_3]

I_4 = I_2
U_4 = [7, 9.5, 12.5, 15.5, 18, 21, 23, 27, 29]
U_4 = [(x - 4) * 4 for x in U_4]

I_5 = I_2
U_5 = [7, 11, 15, 18, 22, 25, 28, 32.5, 35]
U_5 = [(x - 4) * 4 for x in U_5]

I_6 = I_2
U_6 = [8, 13, 17.5, 21.5, 26, 30, 33, 39, 42.5]
U_6 = [(x - 4) * 4 for x in U_6]

I_7 = [round(x * 0.1 + 0.1, 2) for x in range(12)]
print(I_7)
U_7 = [18.5, 14.5, 10, 6, 3.5, 0, -3, -6, -7.5, -9, -10.5, -11.5]
U_7 = [-(x - 23) * 4 for x in U_7]

temp = interp1d(I_k, B_k)
B_1 = temp(I_1)
B_2 = temp(I_2)
B_3 = temp(I_3)
B_4 = temp(I_4)
B_5 = temp(I_5)
B_6 = temp(I_6)
B_7 = temp(I_7)

coeffs = numpy.polyfit(B_1, U_1, 1)
k1 = coeffs[0]
b = coeffs[1]
pyplot.scatter(B_1, U_1, s=7., color='red')
line_points = [k1 * number + b for number in B_1]
line1, = pyplot.plot(B_1, line_points, color='green')
print(k1)

coeffs = numpy.polyfit(B_2, U_2, 1)
k2 = coeffs[0]
b = coeffs[1]
pyplot.scatter(B_2, U_2, s=7., color='red')
line_points = [k2 * number + b for number in B_2]
line2, = pyplot.plot(B_2, line_points, color='green')
print(k2)

coeffs = numpy.polyfit(B_3, U_3, 1)
k3 = coeffs[0]
b = coeffs[1]
pyplot.scatter(B_3, U_3, s=7., color='red')
line_points = [k3 * number + b for number in B_3]
line3, = pyplot.plot(B_3, line_points, color='green')
print(k3)

coeffs = numpy.polyfit(B_4, U_4, 1)
k4 = coeffs[0]
b = coeffs[1]
pyplot.scatter(B_4, U_4, s=7., color='red')
line_points = [k4 * number + b for number in B_4]
line4, = pyplot.plot(B_4, line_points, color='green')
print(k4)

coeffs = numpy.polyfit(B_5, U_5, 1)
k5 = coeffs[0]
b = coeffs[1]
pyplot.scatter(B_5, U_5, s=7., color='red')
line_points = [k5 * number + b for number in B_5]
line5, = pyplot.plot(B_5, line_points, color='green')
print(k5)

coeffs = numpy.polyfit(B_6, U_6, 1)
k6 = coeffs[0]
b = coeffs[1]
pyplot.scatter(B_6, U_6, s=7., color='red')
line_points = [k6 * number + b for number in B_6]
line6, = pyplot.plot(B_6, line_points, color='green')
print(k6)

coeffs = numpy.polyfit(B_7, U_7, 1)
k7 = coeffs[0]
b = coeffs[1]
pyplot.scatter(B_7, U_7, s=7., color='red')
line_points = [k7 * number + b for number in B_7]
line7, = pyplot.plot(B_7, line_points, color='blue', ls='--')
print(k7)

pyplot.ylabel('$U, \\cdot 10^{-8} B$')
pyplot.xlabel('$B$, мТл')
# pyplot.xlim(10, 40)
# pyplot.ylim(0, 2)
pyplot.grid()
# pyplot.title('График зависимости \n  $B(I)$ для пермаллоя')
pyplot.legend((line1, line2, line3, line4, line5, line6, line7),
              [f'k = {k1: .3f} $\\pm$ {k1 * 0.1: .3f}, $I = 0,21 A$', f'k = {k2: .3f}$\\pm$ {k2 * 0.1: .3f}, $I = 0,4 A$',
               f'k = {k3: .2f}$\\pm$ {k3 * 0.1: .2f}, $I = 0,6 A$',f'k = {k4: .2f}$\\pm$ {k4 * 0.1: .2f}, $I = 0,8 A$',
               f'k = {k5: .2f}$\\pm$ {k5 * 0.1: .2f}, $I = 1,0 A$', f'k = {k6: .2f}$\\pm$ {k6 * 0.1: .2f}, $I = 1,1 A$',
               f'k = {k7: .2f}$\\pm$ {k7 * 0.1: .2f}, $I = 1,0 A$'])
# pyplot.savefig('U(B)')

pyplot.show()
I = [0.2, 0.4, 0.6, 0.8, 1, 1.2]
k = [k1, k2, k3, k4, k5, k6]
coeffs = numpy.polyfit(I, k, 1)
k8 = coeffs[0]
b = coeffs[1]
pyplot.scatter(I, k, s=7., color='red')
line_points = [k8 * number + b for number in I]
line = pyplot.plot(I, line_points, color='green')
print(k8)

pyplot.ylabel('$k, \\frac{B\\cdot 10^{-5}}{Тл}$')
pyplot.xlabel('$I$, A')
# pyplot.xlim(10, 40)
# pyplot.ylim(0, 2)
pyplot.grid()
# pyplot.title('График зависимости \n  $B(I)$ для пермаллоя')
pyplot.legend(line, [f'$\\alpha$ = {k8: .2f}$\\pm${k8 * 0.2: .2f}, $B\\cdot 10^-5 / Тл A $'])
# pyplot.savefig('k(I)Cu')

pyplot.show()
