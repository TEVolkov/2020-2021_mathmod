import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

p_cr = 10
tau1 = 15
tau2 = 24
p1 = 7
p2 = 4.9
N = 27
q = 1

M1 = 4.3
M2 = 3.9
x0 = [M1, M2]

t = np.arange(0, 30, 0.01)

a1 = p_cr/(tau1*tau1*p1*p1*N*q)
a2 = p_cr/(tau2*tau2*p2*p2*N*q)
b = p_cr/(tau1*tau1*p1*p1*tau2*tau2*p2*p2*N*q)
c1 = (p_cr - p1)/(tau1*p1)
c2 = (p_cr - p2)/(tau2*p2)

def syst(x, t):
    dx1 = (c1/c1)*x[0] - (b/c1)*x[0]*x[1] - (a1/c1)*x[0]*x[0]
    dx2 = (c2/c1)*x[0] - (b/c1)*x[0]*x[1] - (a2/c1)*x[1]*x[1]
    return dx1, dx2

y = odeint(syst, x0, t)

plt.plot(t, y[:, 0], label = 'Фирма 1')
plt.plot(t, y[:, 1], label = 'Фирма 2')
plt.legend()
plt.grid('axis = "both"')