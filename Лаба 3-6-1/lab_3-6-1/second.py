import matplotlib.pyplot as plt
import numpy
import matplotlib

matplotlib.use('TkAgg')

x = [1.2, 1.4, 1.6, 1.8, 2, 2.5, 3, 3.5, 4, 4.5, 5]
y = [0.9, 0.76, 0.6, 0.56, 0.52, 0.4, 0.32, 0.3, 0.24, 0.22, 0.2]
x = [1/elem for elem in x]

coeffs = numpy.polyfit(x, y, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x]
plt.scatter(x, y, s=7., color='red')
line = plt.plot(x, line_points, color='green')
print(k)

plt.ylabel('$\\delta \\nu$, кГц')
plt.xlabel('$1/T, мc^{-1}$')
# plt.xlim(10, 40)
# plt.ylim(0, 2)
plt.grid()
plt.title('График зависимости \n  $\delta\\nu(1/T)$')
plt.legend(line, [f'k = {k: .2f}$\\pm 0,01 $'])
# plt.savefig('v(T1)')
plt.show()
