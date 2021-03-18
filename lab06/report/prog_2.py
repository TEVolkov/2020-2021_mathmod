import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

a = 0.01
b = 0.02
N = 10300
I0 = 55
R0 = 27
S0 = N - I0 - R0

x0 = [S0, I0, R0]
t = np.arange(0, 200, 0.01)

def dx(x, t):
    dx1 = - a*x[0]
    dx2 = a*x[0] - b*x[1]
    dx3 = b*x[1]
    return dx1, dx2, dx3

y = odeint(dx, x0, t)

y1 = y[:, 0]
y2 = y[:, 1]
y3 = y[:, 2]

plt.plot(t, y1, label = 'S(t)')
plt.plot(t, y2, label = 'I(t)')
plt.plot(t, y3, label = 'R(t)')
plt.legend()
plt.grid('axis = "both"')