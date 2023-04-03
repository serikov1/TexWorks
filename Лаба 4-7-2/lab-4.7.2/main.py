import cmath
from matplotlib import pyplot
import matplotlib
import numpy as np
matplotlib.use('TkAgg')

y = [2.4, 3.4, 4.3, 5.1, 5.7, 6.3]
y = [elem**2 for elem in y]
x = [x+1 for x in range(len(y))]

er = [0.17 for elem in x]

coeffs = np.polyfit(x, y, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x]
pyplot.scatter(x, y, s=7., color='red')
line1 = pyplot.plot(x, line_points, color='b')
pyplot.errorbar(x, y, yerr=er, fmt=' ', capsize=3, ecolor='blue')
pyplot.xlabel('m')
pyplot.ylabel('$r^2$, см$^2$')
pyplot.grid()
pyplot.legend(line1, [f'$r^2 = km$, k = ({k :.1f} $\\pm$ 0.2) см$^2$'])
# pyplot.savefig('km')
pyplot.show()
