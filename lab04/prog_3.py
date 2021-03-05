import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

w = 2.0
g = 2.0

def f(t):
    f = 2*np.cos(2*t)
    return f

def dx(x, t):
    dx1 = x[1]
    dx2 = - w*x[0] - g*x[1] - f(t)
    return dx1, dx2

x0 = np.array([0.5, 1])

t = np.arange(0, 51, 0.05)

x = odeint(dx, x0, t)

y1 = x[:, 0]
y2 = x[:, 1]

plt.plot(y1, y2)
plt.grid('axis = "both"')
