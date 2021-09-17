import matplotlib.pyplot as plt
import numpy as np
from math import *

#n = int(input("n = "))
n = 10000000

t = np.linspace(1, 40, n)
dt = t[1]-t[0]

print(dt)

g = 9.8
rho = 1.293

Sx = 0.5
Sy = 0.5

alpha_st = 5

k = 0.1

Cd = 0.025

m = 0.6

T = (g*Sx*Cd)/(k*alpha_st*Sy)
print(T)

def alpha(t):
    S = 70*np.exp(-0.3*t)*np.sin(0.1*t) + 5
    return(S)

alphaf = alpha(t)

def fligh(Sx, Sy, m):
    X = [0, 0]
    Y = [0, 0]
    x = 0
    y = 0
    for i in range(1, len(t)-1):
        x = ((T - (0.5/m)*rho*Cd*Sx*(((X[i]-X[i-1])/dt)*((X[i]-X[i-1])/dt)))*(dt*dt)) + 2*X[i] - X[i-1]
        y = ((((0.5/m)*rho*k*alphaf[i]*Sy*(((X[i]-X[i-1])/dt)*((X[i]-X[i-1])/dt))) - g)*(dt*dt)) + 2*Y[i] - Y[i-1]
        X.append(x)
        Y.append(y)
    return(X, Y)

X, Y = fligh(Sx, Sy, m)


plt.plot(t, alphaf, color='red')
plt.show()

plt.plot(t, X, color='green')
plt.show()
plt.plot(t, Y, color='blue')
plt.show()

plt.plot(X, Y, color='blue')
plt.show()
