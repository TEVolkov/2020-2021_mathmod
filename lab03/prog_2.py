import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

x0 = 20850
y0 = 9900
t0 = 0

a = 0.71
b = 0.85
c = 0.59
h = 0.73

tmax = 1
dt = 0.05
t = np.arange(t0, tmax, dt)

def P(t):
    p = 1.5*np.sin(6*t)
    return p

def Q(t):
    q = 1.5*np.cos(t)
    return q

def syst(y, t):
    y1 = - a*y[0] - b*y[1] + P(t)
    y2 = - c*y[0]*y[1] - h*y[1] + Q(t)
    return y1, y2

v0 = np.array([x0, y0])

y = odeint(syst, v0, t)

plt.plot(t, y)
plt.xlabel('время')
plt.ylabel('численность армии')