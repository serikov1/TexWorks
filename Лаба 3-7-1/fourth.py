import numpy
from matplotlib import pyplot
import matplotlib
import numpy as np

matplotlib.use('TkAgg')

nu = [50, 150, 250, 400, 500, 600, 750, 800, 1000, 1500, 5000,
      7500, 10000, 15000, 16200, 20000]

L = [10.38, 7.55, 5.68, 4.27, 3.86, 3.62, 3.40, 3.35, 3.22, 3.09,
     3.03, 3.07, 3.15, 3.47, 3.58, 4.1]

x = nu
y = L
pyplot.scatter(x, y, s=7., color='red')


pyplot.ylabel('$L, мГн$')
pyplot.xlabel('$\\nu$, Гц')
pyplot.grid()
pyplot.legend(['$L_{min}$'f'={min(L)}$\\pm 0,01$\n''$L_{max}$'f'={max(L)}$\\pm 0,01$'])
# pyplot.savefig('3-7-1_L(nu)')
pyplot.show()
