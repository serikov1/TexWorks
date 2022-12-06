import numpy
from matplotlib import pyplot
import matplotlib
import numpy as np

matplotlib.use('TkAgg')

psi = np.array([8.5/25.5, 7/22.5, 6/20, 5.5/18.5, 4.5/17, 4/15.5, 3.5/14,
       3/13, 2.5/12.5, 4.5/22, 2.5/16, 4/31.5, 2.5/23, 4/44,
       2.5/38, 2/33, 1.5/30, 1/22, 0.5/25, 0.01])

nu = [100, 112, 124, 136, 148, 160, 172, 184, 196, 220, 305,
      390, 475, 560, 645, 730, 815, 900, 985, 1070]
psi = (psi + 0.5) * np.pi

x = nu
y = -np.tan(psi)

coeffs = np.polyfit(x[:18], y[:18], 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x[:18]]
pyplot.scatter(x, y, s=7., color='red')
line1 = pyplot.plot(x[:18], line_points, color='b')

pyplot.ylabel('$tan(\\psi)$')
pyplot.xlabel('$\\nu$, Гц')
pyplot.grid()
pyplot.legend(line1, [f'$k = ({k * 1000:.2f} \\pm 0.07)$''$\\cdot 10^{-3}$'])
pyplot.savefig('3-7-1_tan(psi)(nu)')
pyplot.show()
