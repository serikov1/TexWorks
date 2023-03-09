from matplotlib import pyplot
import matplotlib
import numpy as np
matplotlib.use('TkAgg')

x = [37.7, 36.8, 12.5, 11.9, 15.4, 15.2]   # a
y = [13.4, 14.1, 58.5, 59.1, 29.6, 30]  # b
er = [1/375 for elem in x]

x = [1/elem for elem in x]
y = [1/elem for elem in y]

x_1 = [17.1, 17.4, 16.4, 16.6, 26.4, 26.0]
y_1 = [52.1, 51.8, 60.1, 60, 24.7, 25.1]

x_1 = [1/elem for elem in x_1]
y_1 = [1/elem for elem in y_1]

x_2 = [24.5, 50.7]
y_2 = [49.1, 23.3]

x_2 = [1/elem for elem in x_2]
y_2 = [1/elem for elem in y_2]
er2 = [1/375 for elem in x_2]


coeffs = np.polyfit(x, y, 1)
k = coeffs[0]
b = coeffs[1]
print(k, b, 1/b, sep='\n')
line_points = [k * number + b for number in x]
pyplot.scatter(x, y, s=7., color='red')
line1, = pyplot.plot(x, line_points, color='b')
pyplot.errorbar(x, y, yerr=er, fmt=' ', capsize=3, ecolor='blue')

coeffs = np.polyfit(x_1, y_1, 1)
k_1 = coeffs[0]
b_1 = coeffs[1]
print(k_1, b_1, 1/b_1, sep='\n')
line_points = [k_1 * number + b_1 for number in x_1]
pyplot.scatter(x_1, y_1, s=7., color='red')
line2, = pyplot.plot(x_1, line_points, color='b', linestyle='--')
pyplot.errorbar(x_1, y_1, yerr=er, fmt=' ', capsize=3, ecolor='blue')

coeffs = np.polyfit(x_2, y_2, 1)
k_2 = coeffs[0]
b_2 = coeffs[1]
print(k_2, b_2, 1/b_2, sep='\n')
line_points = [k_2 * number + b_2 for number in x_2]
pyplot.scatter(x_2, y_2, s=7., color='red')
line3, = pyplot.plot(x_2, line_points, color='b', linestyle='-.')
pyplot.errorbar(x_2, y_2, yerr=er2, fmt=' ', capsize=3, ecolor='blue')

pyplot.xlabel('a, см')
pyplot.ylabel('b, см')
pyplot.grid()
pyplot.legend((line1, line2, line3), [f'$1/b(1/a), F_1 = {1/b: .0f} \\pm 1 см$, $k_1$ = {k: .2f}',
                                      f'$1/b(1/a), F_2 = {1/b_1: .0f} 'f'\\pm 1 см$, $k_2$ = {k_1: .2f}',
                                      f'$1/b(1/a), F_3 = {1/b_2: .0f} 'f'\\pm 1 см$, $k_3$ = {k_2: .2f}'])
# pyplot.savefig('a(b)')
pyplot.show()
