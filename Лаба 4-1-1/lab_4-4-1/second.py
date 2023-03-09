from matplotlib import pyplot
import matplotlib
import numpy as np

matplotlib.use('TkAgg')

x = np.array([37.7, 36.8, 12.5, 11.9, 15.4, 15.2])  # a
y = np.array([13.4, 14.1, 58.5, 59.1, 29.6, 30])  # b
# er = [0.2 for elem in x]

# x = [1/elem for elem in x]
# y = [1/elem for elem in y]

x_1 = np.array([17.1, 17.4, 16.4, 16.6, 26.4, 26.0])
y_1 = np.array([52.1, 51.8, 60.1, 60, 24.7, 25.1])

# x_1 = [1/elem for elem in x_1]
# y_1 = [1/elem for elem in y_1]

x_2 = np.array([23.3, 20.2, 49.1, 71])
y_2 = np.array([50.7, 72.4, 24.5, 21.5])

coeffs = np.polyfit(x + y, x * y, 1)
k = coeffs[0]
b = coeffs[1]
print(k)
line_points = [k * number + b for number in x + y]
pyplot.scatter(x + y, x * y, s=7., color='red')
line1, = pyplot.plot(x + y, line_points, color='b')
# pyplot.errorbar(x + y, y*x, yerr=er, fmt=' ', capsize=3, ecolor='blue')

coeffs = np.polyfit(x_1 + y_1, x_1 * y_1, 1)
k_1 = coeffs[0]
b_1 = coeffs[1]
print(k_1)
line_points = [k_1 * number + b_1 for number in x_1 + y_1]
pyplot.scatter(x_1 + y_1, x_1 * y_1, s=7., color='red')
line2, = pyplot.plot(x_1 + y_1, line_points, color='b', linestyle=':')
# pyplot.errorbar(x_1 + y_1, x_1*y_1, yerr=er, fmt=' ', capsize=3, ecolor='blue')

coeffs = np.polyfit(x_2 + y_2, x_2 * y_2, 1)
k_2 = coeffs[0]
b_2 = coeffs[1]
print(k_2)
line_points = [k_2 * number + b_2 for number in x_2 + y_2]
pyplot.scatter(x_2 + y_2, x_2 * y_2, s=7., color='red')
line3, = pyplot.plot(x_2 + y_2, line_points, color='b', linestyle='--')
# pyplot.errorbar(x_2, y_2, yerr=er2, fmt=' ', capsize=3, ecolor='blue')

pyplot.xlabel('a + b, см')
pyplot.ylabel('ab, $см^2$')
pyplot.grid()
pyplot.legend((line1, line2, line3), [f'ab = k(a+b), $F_1$ = {k: .0f} $\\pm 1$ см',
                               f'ab = k(a+b), $F_2$ = {k_1: .0f} $\\pm 1$ см',
                               f'ab = k(a+b), $F_3$ = {k_2: .0f} $\\pm 1$ см'])
# pyplot.savefig('ab(a+b)')
pyplot.show()
