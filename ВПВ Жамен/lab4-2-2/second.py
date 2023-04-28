import cmath
from matplotlib import pyplot
import matplotlib
import numpy as np
matplotlib.use('TkAgg')

x = [-950, -800, -750, -650, -600, -500, -450, -400, -300, -200, -175, -100, -50, 50, 125, 200, 275, 350, 475]
y = [16.83, 16.79, 16.78, 16.75, 16.75, 16.73, 16.72, 16.71, 16.68, 16.67, 16.66, 16.64,
     16.63, 16.61, 16.58, 16.55, 16.53, 16.51, 16.49]

y = [(-elem + 16.65) * 130 for elem in y]
x = [(elem + 75) / 100 for elem in x]
#
# er = [0.17 for elem in x]
coeffs = np.polyfit(x, y, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x]
pyplot.scatter(x, y, s=7., color='red')
line1 = pyplot.plot(x, line_points, color='b')
# pyplot.errorbar(x, y, yerr=er, fmt=' ', capsize=3, ecolor='blue')
pyplot.xlabel('$P, кПа$')
pyplot.ylabel('$\\Delta n, мкм$')
pyplot.grid()
pyplot.legend(line1, [f'$k = ({k :.5f} \\pm ) нм/Па$'])
# pyplot.savefig('z(m)')
pyplot.show()
