from matplotlib import pyplot
import matplotlib
import numpy as np
from scipy.interpolate import interp1d

matplotlib.use('TkAgg')

x = [690.7, 623.4, 579.1, 577, 546.1, 491.6, 435.8, 404.7]
y = [1.672, 1.676, 1.6809, 1.6812, 1.684, 1.692, 1.704, 1.713]

values = interp1d(x, y)
n_d = values(589.3)
n_f = values(486.1)
n_c = values(656.3)

print(n_d, n_f, n_c, sep='\n')

coeffs = np.polyfit(x, y, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x]
pyplot.scatter(x, y, s=7., color='red')
# line1 = pyplot.plot(x, line_points, color='b')

pyplot.xlabel('$\\lambda$, нм')
pyplot.ylabel('n')
pyplot.grid()
pyplot.legend(['$n(\\lambda)$'])
# pyplot.savefig('n(lambda)')
pyplot.show()
