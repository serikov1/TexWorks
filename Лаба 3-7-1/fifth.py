import numpy
from matplotlib import pyplot
import matplotlib
import numpy as np

matplotlib.use('TkAgg')

nu = np.array([50, 150, 250, 400, 500, 600, 750, 800, 1000, 1500, 5000,
               7500, 10000, 15000, 16200, 20000])

L = np.array([10.38, 7.55, 5.68, 4.27, 3.86, 3.62, 3.40, 3.35, 3.22, 3.09,
              3.03, 3.07, 3.15, 3.47, 3.58, 4.1])

x = nu[:-7] ** 2
y = (max(L) - min(L)) / (L[:-7] - min(L))

coeffs = np.polyfit(x, y, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number for number in x]
pyplot.scatter(x, y, s=7., color='red')
line1 = pyplot.plot(x, line_points, color='b')

pyplot.ylabel('$(L_{max} - L_{min})/(L - L_{min})$')
pyplot.xlabel('$\\nu^2$, Гц^2')
pyplot.grid()
pyplot.legend(line1, [f'$k = ({k * 10**6:.1f} \\pm 0.1)$''$\\cdot 10^{-6} Гц^{-2}$'])
# pyplot.savefig('3-7-1_L(nu2)')
pyplot.show()
