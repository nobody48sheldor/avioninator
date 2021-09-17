import matplotlib.pyplot as plt
import numpy as np
from math import *

#n = int(input("n = "))
n = 10000000

t = np.linspace(1, 40, n)
dt = t[1]-t[0]

g = 9.8
rho = 1.293

Sx = 0.5
Sy = 0.5

alpha_st = 2

k = 0.1

Cd = 0.025

m = 0.6

T = (g*Sx*Cd)/(k*alpha_st*Sy)
print(T)

def alpha(t):
    S = alpha_st + 9.837*np.exp(-(0.6*t-5)**2)
    return(S)

alphaf = alpha(t)

def fligh(Sx, Sy, m):
    X = []
    Y = []
    VX = []
    VY = []
    vx = 0
    vy = 0
    x = 0
    y = 0
    for i in range(len(t)):
        vx = vx + (T - (0.5/m)*rho*Cd*Sx*vx*vx)*dt
        vy = vy + ((0.5/m)*rho*k*alphaf[i]*Sy*vx*vx - g)*dt
        x = x + vx*dt
        if y < 0 and vy < 0:
            y = 0
        else:
            y = y + vy*dt
        X.append(x)
        Y.append(y)
        VX.append(vx)
        VY.append(vy)
    return(X, Y, VX, VY)

X, Y, VX, VY = fligh(Sx, Sy, m)

plt.plot(t, alphaf, color='red')
plt.show()


plt.plot(t, VX, color='green')
plt.show()

plt.plot(t, VY, color='green')
plt.show()

plt.plot(t, X, color='green')
plt.show()

plt.plot(t, Y, color='blue')
plt.show()

plt.plot(X, Y, color='red')
plt.show()
