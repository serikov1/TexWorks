import matplotlib.pyplot as plt
import numpy
import matplotlib

matplotlib.use('TkAgg')

x = [1 / ((x + 1) * 20) for x in range(7)]
y = [49.9, 25, 16.6, 12.5, 9.9, 8.5, 7]

coeffs = numpy.polyfit(x, y, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x]
plt.scatter(x, y, s=7., color='red')
line = plt.plot(x, line_points, color='green')
print(k)

plt.ylabel('$\\Delta \\nu$, кГц')
plt.xlabel('$1/\\tau, мкc^{-1}$')
# plt.xlim(10, 40)
# plt.ylim(0, 2)
plt.grid()
plt.title('График зависимости \n  $\Delta\\nu(1/\\tau)$')
plt.legend(line, [f'k = {k / 1000: .3f}$\\pm 0,001 $'])
# plt.savefig('v(t)')
plt.show()
