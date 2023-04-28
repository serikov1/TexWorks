import cmath
from matplotlib import pyplot
import matplotlib
import numpy as np

matplotlib.use('TkAgg')

x = [20, 40, 60, 80]
y = [0.019, 0.033, 0.047, 0.061]
x = [elem / 1000 for elem in x]
x_1 = [20, 40, 60]
y_1 = [0.014, 0.028, 0.038]
x_1 = [elem / 1000 for elem in x_1]

#
# er = [0.17 for elem in x]

coeffs = np.polyfit(x, y, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x]
pyplot.scatter(x, y, s=7., color='red')
line1, = pyplot.plot(x, line_points, color='b', linestyle='--')
# pyplot.errorbar(x, y, yerr=er, fmt=' ', capsize=3, ecolor='blue')

coeffs = np.polyfit(x_1, y_1, 1)
k_1 = coeffs[0]
b = coeffs[1]
line_points = [k_1 * number + b for number in x_1]
pyplot.scatter(x_1, y_1, s=7., color='red')
line2, = pyplot.plot(x_1, line_points, color='b')

pyplot.xlabel('$L_2, м$')
pyplot.ylabel('$\\rho_c, мм$')
pyplot.grid()
pyplot.legend((line1, line2), ['$k_{20} = $'f'{k :.1f}''$ \cdot 10^{-3}$ => $\\rho_L = 0,202 мм$', '$k_{30}$' f'= {k_1 :.1f}'' $\cdot 10^{-3}$ => $\\rho_L = 0,236 мм$'])
pyplot.savefig('z(m)')
pyplot.show()
