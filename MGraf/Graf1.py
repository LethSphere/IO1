import numpy as np
import matplotlib.pyplot as plt


# Construct lines
# x > 0
x = np.linspace(-20, 20, 200)

y1 = 5 - 2*x
# Make plot
plt.plot(x, y1)
plt.xlim((-15, 20))
plt.ylim((0, 20))


# Fill feasible region
plt.fill_between(x, y1, color='purple', alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.grid()

plt.show()
