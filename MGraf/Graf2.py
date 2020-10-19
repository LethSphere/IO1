
import numpy as np
import matplotlib.pyplot as plt


# Construct lines
# x > 0
x = np.linspace(0, 20, 2000)
# x1 >= 0
y1 = 5 + x*0

plt.xlabel(r'$x_2>=0$')
plt.ylabel(r'$x_1>=0$')
# Make plot
plt.plot(x, y1)

plt.xlim((0, 16))
plt.ylim((0, 11))


# Fill feasible region

plt.fill_between(x, y1, color='purple', alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.grid()

plt.show()