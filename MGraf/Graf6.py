import numpy as np
import matplotlib.pyplot as plt


# Construct lines
# x > 0
x = np.linspace(-10, 200, 2000)

y1 = 180-2*x
y2 = (160-x)*2
y3 = x*0
y4 = 100-x

# Make plot
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.xlim((-10, 100))
plt.ylim((-10, 100))


# Fill feasible region
y5 = np.minimum(y2, y4)
y6 = np.minimum(y1, y3)
plt.fill_between(x, y5, y6, where=y5>y6, color='purple', alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.grid()

plt.show()
