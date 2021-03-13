import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

a = 0.69
b = 0.068
c = 0.67
d = 0.066

def dx(x, t):
    dx1 = - a*x[0] + b*x[0]*x[1]
    dx2 = c*x[1] - d*x[0]*x[1]
    return dx1, dx2

x0 = [4, 11]

t = np.arange(0, 150, 0.1)

y = odeint(dx, x0, t)

y1 = y[:, 0]
y2 = y[:, 1]

plt.plot(t, y1, label = 'хищники')
plt.plot(t, y2, label = 'жертвы')
plt.legend()
plt.grid('axis = "both"')

#plt.plot(y1, y2)
#plt.grid('axis = "both"')