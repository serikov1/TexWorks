from matplotlib import pyplot
import matplotlib
import numpy as np
matplotlib.use('TkAgg')

x = np.array([3.31, 3.13, 1.8, 4.9, 3.1, 1.75, 5.06, 3.17, 1.85, 3.12])
y = [0 for _ in range(len(x))]
er = [0.09 * elem for elem in x]
print(er)
coeffs = np.polyfit(x, y, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x]
pyplot.scatter(x, y, s=40, color='red')
pyplot.errorbar(x, y, xerr=er, fmt=' ', capsize=3, ecolor='blue')
# line1 = pyplot.plot(x, line_points, color='b')

pyplot.xlabel('q, $\\cdot 10^{-19}$ Кл')
pyplot.ylim(-0.2, 0.2)
pyplot.grid()
# pyplot.savefig('milliken')
pyplot.show()
