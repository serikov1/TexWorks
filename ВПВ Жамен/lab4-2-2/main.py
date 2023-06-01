import cmath
from matplotlib import pyplot
import matplotlib
import numpy as np
matplotlib.use('TkAgg')

x = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [16.20, 16.25, 16.30, 16.35, 16.40, 16.44, 16.50, 16.55, 16.60, 16.65, 16.69,
     16.75, 16.80, 16.86, 16.90, 16.96, 17.00, 17.06, 17.11, 17.16, 17.21]

y = [(elem) * 1000 for elem in y]

# er = [0.17 for elem in x]
coeffs = np.polyfit(x, y, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x]
pyplot.scatter(x, y, s=7., color='red')
line1 = pyplot.plot(x, line_points, color='b')
# pyplot.errorbar(x, y, yerr=er, fmt=' ', capsize=3, ecolor='blue')
pyplot.xlabel('$m$')
pyplot.ylabel('$z_m, мкм$')
pyplot.grid()
pyplot.legend(line1, [f'$k = ({k :.0f} \\pm 1) мкм$'])
pyplot.savefig('z(m)')
pyplot.show()
