import cmath
from matplotlib import pyplot
import matplotlib
import numpy as np
matplotlib.use('TkAgg')

x = [1, 1/1.2, 1/1.4, 1/1.6, 1/1.8, 0.5]
y = [688, 586, 512, 444, 400, 342]
#
# er = [0.17 for elem in x]
coeffs = np.polyfit(x, y, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x]
pyplot.scatter(x, y, s=7., color='red')
line1 = pyplot.plot(x, line_points, color='b')
# pyplot.errorbar(x, y, yerr=er, fmt=' ', capsize=3, ecolor='blue')
pyplot.xlabel('$1/\\nu$')
pyplot.ylabel('$\\Lambda$')
pyplot.grid()
pyplot.legend(line1, [f'$k = ({k :.0f} \\pm 70) м\\cdotГц$'])
pyplot.savefig('L(nu)')
pyplot.show()
