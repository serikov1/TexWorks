from matplotlib import pyplot
import matplotlib
import numpy as np

matplotlib.use('TkAgg')

psi_1 = np.array([8.5/25.5, 7/22.5, 6/20, 5.5/18.5, 4.5/17, 4/15.5, 3.5/14,
       3/13, 2.5/12.5, 4.5/22, 2.5/16, 4/31.5, 2.5/23, 4/44,
       2.5/38, 2/33, 1.5/30, 1/22, 0.5/25, 0.01])
nu_1 = np.array([100, 112, 124, 136, 148, 160, 172, 184, 196, 220, 305,
      390, 475, 560, 645, 730, 815, 900, 985, 1070])
psi_1 = -(psi_1 - 0.5) * np.pi


psi_2 = np.array([0.01, 2/15, 4.5/22.5, 4.5/16, 5/12.5, 5/10, 4.5/8, 4.5/7,
                  4.5/6, 18/23, 17/21, 17/19, 16/18, 15.5/16.5])
psi_2 = (psi_2 + 0.5) * np.pi
nu_2 = np.array([1.1, 3.3, 5.5, 7.7, 9.9, 12.1, 14.3, 16.5, 18.7,
                 20.9, 23.1, 25.3, 27.5, 29.7])
nu_2 = nu_2 * 1000

x = np.array(np.sqrt(np.append(nu_1, nu_2)))
y = np.array(np.append(psi_1, psi_2) - np.pi/4)

x_1 = np.array(np.append([0], x[10:]))
y_1 = np.array(np.append([0], y[10:]))

coeffs = np.polyfit(x_1, y_1, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number for number in x_1]
pyplot.scatter(x, y, s=7., color='red')
line1 = pyplot.plot(x_1, line_points, color='b')

pyplot.ylabel('$\\psi - \\pi/4$')
pyplot.xlabel('$\\sqrt{\\nu}, \\sqrt{Гц}$')
pyplot.xlim(0, 180)
pyplot.grid()
pyplot.legend(line1, [f'$k = ({k * 1000:.1f} \\pm 0.4)'' \\cdot 10^{-3}$'])
# pyplot.savefig('3-7-1_psi(nu)')
pyplot.show()
