import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

x0 = 4
N = 741

t = np.arange(0, 30, 0.1)

def k(t):
    g = 0.65*np.sin(7*t)
    return g

def p(t):
    v = np.cos(3*t)
    return v

def f(x, t):
    xd = (k(t) + p(t)*x)*(N - x)
    return xd

x = odeint(f, x0, t)

plt.plot(t, x)
plt.grid('axis = "both"')