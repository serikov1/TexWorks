import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.use('TkAgg')

x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1, 1.2]
y = [18.7, 150.2, 276.8, 386.9, 504, 614.5, 751.8, 900, 1031, 1153.6, 1220]

coeffs = numpy.polyfit(x, y, 1)
k = coeffs[0]
b = coeffs[1]

pyplot.scatter(x, y, s=10., color='red')
line_points = [k * number + b for number in x]
# pyplot.plot(x, line_points, color='green')
print(k)

pyplot.ylabel('$B$, мТл')
pyplot.xlabel('$I$, Ам')
# pyplot.xlim(10, 40)
# pyplot.ylim(0, 2)
pyplot.grid()
# pyplot.title('График зависимости \n  $B(I)$ для пермаллоя')
pyplot.legend(['$B(I)$'])
# pyplot.savefig('B(I)')

pyplot.show()