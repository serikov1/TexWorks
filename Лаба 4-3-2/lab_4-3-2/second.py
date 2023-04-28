import cmath
from matplotlib import pyplot
import matplotlib
import numpy as np
matplotlib.use('TkAgg')

x_1 = [0, 1, 2, 3]
y_1 = [0, 128, 250, 384]

x_2 = [0, 1, 2]
y_2 = [0, 111, 228]

x_3 = [0, 1, 2]
y_3 = [0, 171, 342]

coeffs = np.polyfit(x_1, y_1, 1)
k_1 = coeffs[0]
b = coeffs[1]
line_points = [k_1 * number + b for number in x_1]
pyplot.scatter(x_1, y_1, s=7., color='red')
line1, = pyplot.plot(x_1, line_points, color='b', linestyle='--')
# pyplot.errorbar(x, y, yerr=er, fmt=' ', capsize=3, ecolor='blue')

coeffs = np.polyfit(x_2, y_2, 1)
k_2 = coeffs[0]
b = coeffs[1]
line_points = [k_2 * number + b for number in x_2]
pyplot.scatter(x_2, y_2, s=7., color='red')
line2, = pyplot.plot(x_2, line_points, color='b')

coeffs = np.polyfit(x_3, y_3, 1)
k_3 = coeffs[0]
b = coeffs[1]
line_points = [k_3 * number + b for number in x_3]
pyplot.scatter(x_3, y_3, s=7., color='red')
line3, = pyplot.plot(x_3, line_points, color='b', linestyle=':')

pyplot.xlabel('m')
pyplot.ylabel('$l, мкм$')
pyplot.grid()
pyplot.legend((line1, line2, line3), [f'$k_1 = ({k_1 :.0f} \\pm 10)$ мкм', f'$k_2 = ({k_2 :.0f} \\pm 10)$ мкм', f'$k_3 = ({k_3 :.0f} \\pm 10)$ мкм'])
pyplot.savefig('l(m)')
pyplot.show()
