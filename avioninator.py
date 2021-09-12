import matplotlib.pyplot as plt
import numpy as np
from math import *

#n = int(input("n = "))
n = 1000000

t = np.linspace(0, 120, n)
dt = t[1]-t[0]

g = 9.8
rho = 1.293

Sx = 0.087
Sy = 0.42

alpha_st = 5

k = 0.1

Cd = 0.6

m = 0.6

T = (g*Sx*Cd)/(k*alpha_st*Sy)
print(T)

def alpha(t):
    S = 50*np.exp(-0.2*t)*np.sin(0.08*t) + 5
    return(S)

alphaf = alpha(t)

def fligh(Sx, Sy, m):
    X = []
    Y = []
    Xv = []
    Yv = []
    x = 0
    y = 0
    vx = 0
    vy = 0
    for i in range(len(t)):
        #vx = vx + ((g*Cd*Sx*t[i])/(k*alphaf[i]*Sy) - (0.5/m)*rho*Cd*Sx*(vx*vx))*dt
        vx = vx + (T*t[i] - (0.5/m)*rho*Cd*Sx*(vx*vx))*dt
        vy = vy + ((0.5/m)*rho*k*alpha_st*Sy*(vx*vx) - g*t[i])*dt
        x = x + vx*dt
        if t[i] < 20:
            if vy < 0:
                y = 0
                vy = 0
            else:
                y = y + vy*dt
        else:
            y = y + vy*dt
        Xv.append(vx)
        Yv.append(vy)
        X.append(x)
        Y.append(y)
    return(X, Y, Xv, Yv)

X, Y, Xv, Yv = fligh(Sx, Sy, m)


plt.plot(t, alphaf, color='red')
plt.show()

plt.plot(t, Xv, color='green')
plt.plot(t, Yv, color='blue')
plt.show()

plt.plot(t, X, color='green')
plt.plot(t, Y, color='blue')
plt.show()

plt.plot(X, Y, color='blue')
plt.show()
