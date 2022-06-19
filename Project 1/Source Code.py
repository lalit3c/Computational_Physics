
"""
Computational Physics
Project 1
@Lalit Chaudhary
l.chaudhary@jacobs-university.de
"""

import numpy as np
import matplotlib.pyplot as plt

#Setting up the constants
G = 6.67*10**(-11)
M = 5.99*10**(24)
R = 6370000
m = 1
k = 3*10**(-4)

#Initial conditions
t0 = 0
y0 = 10000
v0 = 0
g = -9.81

#height dependenet acceleration and velocity dependent damping
def ac(y, v):
   return  -1*(G*M*m)/(R*R*(1+y**2/R**2)) + (k/m)*v**2 


dt = 0.5

#Euler method
y, v, t = y0, v0, t0
yarr, varr, tarr = [y], [v], [t]
while y > 0:
    
    a = ac(y, v)
    v = v - a*dt
    y = y - v*dt
    t = t+dt
    tarr.append(t)
    varr.append(v)
    yarr.append(y)


#analytical solution without damping
th = np.linspace(0, t, 100)
pos = []
for t in th:
    p = y0 + v0*t + 0.5 * ac(y0, v0) * t**2
    pos.append(p)


plt.figure(1, figsize=(10,8))
plt.plot(tarr, yarr, 'b-', label = 'Eulers Method')
plt.plot(th, pos, 'r', label = 'analytical solution')
#plt.text(35, 8000, 'k = 0 i.e. no damping')
plt.xlabel('time (t) [sec]')
plt.ylabel('Position (y) [meter]')
plt.legend()
#plt.savefig('NoDamping.jpg')


#Euler-Richardson Scheme
y, v, t = y0, v0, t0
y1arr, v1arr, t1arr = [y], [v], [t]
while y > 0:
    
    k1v = ac(y, v)*dt
    k1y = v * dt
    k2v = ac((y - k1y/2), (v-k1v/2))*dt
    k2y = (v - k1v/2)*dt
    v = v - k2v 
    y = y - k2y
    t = t+dt
    
    t1arr.append(t)
    v1arr.append(v)
    y1arr.append(y)





plt.figure(1, figsize=(10,8))
plt.plot(t1arr, y1arr, 'b-', label = 'Euler-Richardson Method')
plt.plot(th, pos, 'r', label = 'analytical solution')
#plt.text(35, 8000, 'k = 0 i.e. no damping')
plt.xlabel('time (t) [sec]')
plt.ylabel('Position (y) [meter]')
plt.legend()
#plt.savefig('NoDampingER.jpg')

    
plt.figure(3, figsize=(10,8))
plt.plot(t1arr, y1arr, 'k-', label = 'Euler Richardson Method')
plt.plot(tarr, yarr, 'r-', label='Euler Method')
plt.plot(th, pos, 'g-', label = 'analytical solution')
plt.xlabel('time (t) [sec]')
plt.ylabel('Position (y) [meter]')
plt.legend()
plt.text(55, 9200, 'dt = 0.5')
plt.show()


plt.figure(2, figsize = (10,8))
plt.plot(tarr, varr, 'r', label ='Euler Method')
plt.plot(t1arr, v1arr, 'k', label = 'Euler Richardson Method')
plt.xlabel('time (t) [sec]')
plt.ylabel('velocity (v) [m/s]')
plt.ylim(0, 185)
plt.text(55, 150, r'$k = 3 \times10^{-4} \:kg/m$')
plt.text(55,145, r'$ dt = 6.5\:sec$')
plt.legend()
#plt.savefig('stableE.jpg')


