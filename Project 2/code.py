
"""
Computational Physics
Project 2
@Lalit Chaudhary
l.chaudhary@jacobs-university.de
"""

import numpy as np
import matplotlib.pyplot as plt

#Setting up the constants
m = 1
#k = 0.8
g = 9.8
#n = 1
#Initial conditions
t0 = 0
y0 = 0

x0 = 0
v0 = 20

theta0 = 34/180 *np.pi

vx0 = v0 * np.cos(theta0)
vy0 = v0 * np.sin(theta0)

def euler(n, k):
    
    #height dependenet acceleration and velocity dependent damping
    def acy(vx, vy):
        v = (vx**2 + vy**2)**0.5
        return v**(n-1) * k *(-1) * vy - g
    
    
    def acx(vx, vy):
        return -1*k*((vx**2 + vy**2)**(0.5*(n-1)))*vx
        
    
    dt = 0.005
    
    #Euler method
    x, y, vx, vy, t = x0, y0, vx0, vy0, t0
    xarr, yarr, vxarr, vyarr, tarr = [x], [y], [vx], [vy] ,[t]
    
    while y >= 0:
        
        ax = acx(vx, vy)
        ay = acy(vx, vy)
        vx = vx + ax*dt
        vy = vy + ay*dt
        x = x + vx*dt
        y = y + vy*dt
        t = t+dt
        
        tarr.append(t)
        xarr.append(x)
        vxarr.append(vx)
        yarr.append(y)
        vyarr.append(vy)
        
    return xarr, yarr

#analytical
"""
th = np.linspace(0, 20, 500)
x,y=[],[]
yt = 1
for t in th:
    if yt >= 0:
        xt = x0+vx0 * t
        yt =y0+vy0 *t - 0.5 * g * t**2
        x.append(xt)
        y.append(yt)
"""
x1arr, y1arr = euler(1, 0.8)
x2arr, y2arr = euler(1.5, 0.17)
x3arr, y3arr = euler(2, 0.036)

plt.figure(1, figsize=(10,8))
#plt.plot(tarr, yarr, 'b-')
#plt.plot(x[:], y[:], 'b', label = 'Without Drag')
plt.plot(x1arr[:], y1arr[:], 'r', label = 'n=1')
plt.plot(x2arr[:], y2arr[:], 'b', label = 'n=3/2')
plt.plot(x3arr[:], y3arr[:], 'g', label = 'n=2')
plt.legend()
plt.text(2.5, 4, r'$v_0 = 20 m/s$')
plt.xlabel('x-position')
plt.ylabel('y-position')
plt.savefig('1.jpg')
plt.show()



