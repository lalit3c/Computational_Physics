"""
Lalit Chaudhary
Computational Physics
Project 5
"""

from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import glob
from PIL import Image

l = 1               #length of the string
h = 0.01           #grid spacing
T = 10              #Tension in the string
m = 10**(-3)        #mass
v0 = 0              #initial velocity, du/dt at at = 0

c = np.sqrt(T/m)    #speed of wave

dt =10**(-4)        #time step
cprime = h/dt       #lattice velocity 

size = int(l/h)+1   #size of array to store position of each point on string

x = np.linspace(0, l, size) #mark point on strings

u = np.zeros(shape = (size,))   #Position at current time
unew = np.zeros_like(u)         #Position at previous time step
uold = np.zeros_like(u)         #Position at next time step


#Set Boundary Conditions
def boundary(u):
    u[i], u[size-1] = 0, 0
                
#initial pulse                
for i in range(1, size-1):
    u[i] = np.exp(-200*(i*h -l/2)**2)
plt.plot(x, u, 'g-')
plt.title('time = 0')
plt.ylim(-1.1, 1.1)
plt.savefig('100')                
boundary(u)
boundary(uold)

#update uold based on velocity at t=0 [explicitly ignore boundary points]
for i in range(1, size-1):
     uold[i] = u[i] - dt*v0 + 0.5 * (c/cprime)**2 * (u[i+1]+u[i-1]-2*u[i])


count = 0       #count the number of iterations
t = 0           #elapsed time
tmax = 0.02     #time limit

#loop until time limit
while t< tmax:
    count = count+1
    t = t+dt
    boundary(unew)      
    
    #Update ynew using Leapfrog method, ignore boundary points
    for i in range(1, size-1):
        unew[i] = 2*u[i] - uold[i] + (c/cprime)**2 *(u[i+1]+u[i-1]-2*u[i])
    
    #Updare uold and u for future iteration     
    uold = np.copy(u)
    u = np.copy(unew)
    
    #make plots after every 5 iterations
    if count%5 == 0:
        plt.clf()
        plt.plot(x,u, 'g-')
        plt.ylim(-1.1, 1.1)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('time = {:1.4f}'.format(t))
        plt.savefig(str(ord('a')+int(count))+'.png')
        plt.show

#make animation using saved images
"""
fp_in = "*.png"
fp_out = "a.gif"


img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=200, loop=0)    
"""