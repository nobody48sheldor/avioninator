import matplotlib.pyplot as plt
import numpy as np
import pygame as pg
import os

WHITE = (255, 255, 255)

pg.display.init()
screen = pg.display.set_mode((1200, 800))
image = pg.Surface((32, 32))
image.fill(WHITE)
#plane = pg.Rect((0, 0), (32, 32))
plane = pg.image.load('plane.png')

run = False
Thrust = False

n = 10000

t = np.linspace(1, 10, n)
dt = t[1]-t[0]
Time = []

g = 9.8
rho = 1.293

Sx = 0.5
Sy = 0.5

alpha_st = 2

k = 0.1

Cd = 0.025

m = 0.6

Th = (g*Sx*Cd)/(k*alpha_st*Sy)
print(Th)

time = 0

X = []
Y = []
VX = []
VY = []
vx = 0
vy = 0
x = 0
y = 0

input("ready to lift off ? ")
run = True


alpha = alpha_st
T = Th

while run == True:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_z:
                T = Th
                print("i am speed")
            if event.key == pg.K_s:
                T = 0
                print("i am not speed")
            if event.key == pg.K_a:
                T = Th + 1
                print("i am verry speed")
            if event.key == pg.K_UP:
                alpha = alpha + 0.2
                print("wing go BRRRR")
            if event.key == pg.K_DOWN:
                alpha = alpha - 0.2
                print("wing go BRRRRn'tq")
            if event.key == pg.K_p:
                quit()
    vx = vx + (T - (0.5/m)*rho*Cd*Sx*vx*vx)*dt
    vy = vy + ((0.5/m)*rho*k*alpha*Sy*vx*vx -(0.5/m)*rho*Cd*Sy*vy*vy - g)*dt
    x = x + vx*dt
    if y < 0 and vy < 0:
        y = 0
        vy = 0
    else:
        y = y + vy*dt
    time = time + dt
    Time.append(time)
    X.append(x)
    Y.append(y)
    VX.append(vx)
    VY.append(vy)
    screen.blit(plane, (int(0.8*(x+10)), int(0.8*(-y+500))))
    print("time = {} \n \n thrust = {} \n \n alpha = {} \n \n xspeed = {} \n \n yspeed = {}".format(time, T, alpha, vx, vy))
    pg.display.update()
    os.system('clear')
