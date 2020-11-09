# importando modulos necesarios
import matplotlib.pyplot as plt 
import numpy as np 
from scipy import optimize
np.random.seed(1984) #replicar random


# Ejemplo mínimos cuadrados no lineales utilizando scipy.optimize
beta = (5, 2, 1)

# funcion modelo
def f(x, b0, b1, b2):
    return b0 + b1 * np.exp(-b2 * x**2)

# datos aleatorios para simular las observaciones
xdata = np.linspace(0, 5, 50)
y = f(xdata, *beta)
ydata = y + 0.05 * np.random.randn(len(xdata))

# función residual
def g(beta):
    return ydata - f(xdata, *beta)

# comenzamos la optimización
beta_start = (1, 1, 1)
beta_opt, beta_cov = optimize.leastsq(g, beta_start)
beta_opt

# graficamos
fig, ax = plt.subplots(figsize=(10,8))
ax.scatter(xdata, ydata)
ax.plot(xdata, y, 'r', lw=2)
ax.plot(xdata, f(xdata, *beta_opt), 'b', lw=2)
ax.set_xlim(0, 5)
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"$f(x, \beta)$", fontsize=18)
ax.set_title('Mínimos cuadrados no lineales')
plt.show()
