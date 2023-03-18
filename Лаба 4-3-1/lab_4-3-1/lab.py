from matplotlib import pyplot
import matplotlib
import numpy as np
matplotlib.use('TkAgg')

y = np.array([0.1, 0.24, 0.36, 0.48, 0.61])
x = [i+1 for i in range(len(y))]
# er = [0.09 * elem for elem in x]
# print(er)
coeffs = np.polyfit(x, y, 1)
k = coeffs[0]
b = coeffs[1]
print(k)
line_points = [k * number + b for number in x]
pyplot.scatter(x, y, s=40, color='red')
# pyplot.errorbar(x, y, xerr=er, fmt=' ', capsize=3, ecolor='blue')
line1 = pyplot.plot(x, line_points, color='b')

pyplot.xlabel('m')
pyplot.ylabel('$\\delta x$, мм')
# pyplot.ylim(-0.2, 0.2)
pyplot.grid()
pyplot.legend(line1, [f'$\\delta x$ = km, k = {k : .2f} мм'])
# pyplot.savefig('fraungofer1')
pyplot.show()
