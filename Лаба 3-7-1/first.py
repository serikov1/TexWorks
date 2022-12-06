from matplotlib import pyplot
import matplotlib
import numpy as np
matplotlib.use('TkAgg')

V = np.array([ 0.194, 0.249, 0.301, 0.349, 0.393, 0.433, 0.469, 0.502, 0.531, 0.557, 0.580])
I = np.array([ 465, 461, 456, 450, 444, 438, 432, 426, 420, 414, 409])
nu = np.array([ 29, 38, 47, 56, 65, 74, 83, 92, 101, 110, 119])
xi = V / (I * 0.001 * nu)
print(xi)
x = nu ** 2
y = 1 / xi**2

coeffs = np.polyfit(x, y, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x]
pyplot.scatter(x, y, s=7., color='red')
line1 = pyplot.plot(x, line_points, color='b')

pyplot.ylabel('$1/\\xi^2, (Гц \\cdot А / В)^2$')
pyplot.xlabel('$\\nu^2$, Гц$^2$')
pyplot.grid()
pyplot.legend(line1, [f'$1/\\xi^2 = k \\cdot \\nu^2$,  \n $k = {k :.2f} \\pm {k * 0.05 :.2f}$, $(A/B)^2$, \n'
                      f'$b = {b:.0f} \\pm {b*0.05 :.0f}, (Гц \\cdot А / В)^2$'])
pyplot.savefig('3-7-1_xi2(nu2)')
pyplot.show()
