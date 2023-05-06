import cmath
from matplotlib import pyplot
import matplotlib
import numpy as np

matplotlib.use('TkAgg')
x = [0, 1, 2, 3, 4, 5]
y = [0, 2, 3.2, 4.1, 4.9, 6.3]

x_1 = [0, 1, 2, 3, 4, 5]
y_1 = [0, 2.1, 3.9, 5.4, 7.0, 8.8]

x_2 = [0, 1, 2, 3, 4, 5]
y_2 = [0, 4.1, 7.0, 10.0, 13.8, 16.6]

x_3 = [0, 1, 2]
y_3 = [0, 11.7, 29.1]

x_4 = [0, 1]
y_4 = [0, 18.6]

coeffs = np.polyfit(x, y, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x]
pyplot.scatter(x, y, s=10., color='red')
line1, = pyplot.plot(x, line_points, '*', color='b', linestyle='-')
# pyplot.errorbar(x, y, yerr=er, fmt=' ', capsize=3, ecolor='blue')

coeffs = np.polyfit(x_1, y_1, 1)
k_1 = coeffs[0]
b = coeffs[1]
line_points = [k_1 * number + b for number in x_1]
pyplot.scatter(x_1, y_1, s=10., color='red')
line2, = pyplot.plot(x_1, line_points, 'o', color='b', linestyle='-')

coeffs = np.polyfit(x_2, y_2, 1)
k_2 = coeffs[0]
b = coeffs[1]
line_points = [k_2 * number + b for number in x_2]
pyplot.scatter(x_2, y_2, s=10., color='red')
line3, = pyplot.plot(x_2, line_points, 'v', color='b', linestyle='-')

coeffs = np.polyfit(x_3, y_3, 1)
k_3 = coeffs[0]
b = coeffs[1]
line_points = [k_3 * number + b for number in x_3]
pyplot.scatter(x_3, y_3, s=10., color='red')
line4, = pyplot.plot(x_3, line_points, 's', color='b', linestyle='-')

coeffs = np.polyfit(x_4, y_4, 1)
k_4 = coeffs[0]
b = coeffs[1]
line_points = [k_4 * number + b for number in x_4]
pyplot.scatter(x_4, y_4, s=10., color='red')
line5, = pyplot.plot(x_4, line_points, 'p', color='b', linestyle='-')

pyplot.xlabel('$N$')
pyplot.ylabel('$z_N, мм$')
pyplot.grid()
pyplot.legend((line1, line2, line3, line4, line5), ['$k_{1} = 2\\frac{d^2}{\\lambda} = $'f'{k :.1f} => d = 18$\\pm1$  мкм',
                                                    '$k_{2} = $'f'{k_1 :.1f} => d = 21$\\pm1$  мкм',
                                                    '$k_{3} = $'f'{k_2 :.1f} => d = 30$\\pm1$  мкм',
                                                    '$k_{4} = $'f'{k_3 :.1f} => d = 62$\\pm2$  мкм',
                                                    '$k_{5} = $'f'{k_4 :.1f} => d = 70$\\pm2$  мкм'])
# pyplot.savefig('z(N)')
pyplot.show()
