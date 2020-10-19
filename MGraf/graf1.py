# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 09:18:59 2020

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt


# Construct lines
# x > 0
x = np.linspace(-20, 20, 200)
# x1 >= 0
y1 = 5 - 2*x
# 2x1+x2<=10
y2 = 10-2*x
# x2 >= 4x-8
y3 = (4*x-8)/4.0
# y <= 2x - 5 
y4 = (5 * x +2)/2
plt.xlabel(r'$x_2>=0$')
plt.ylabel(r'$x_1>=0$')
# Make plot
plt.plot(x, y1)
plt.xlim((-15, 20))
plt.ylim((0, 20))


# Fill feasible region
y5 = np.minimum(y2, y4)
y6 = np.maximum(y1, y3)
plt.fill_between(x, y1, color='purple', alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.grid()

plt.show()