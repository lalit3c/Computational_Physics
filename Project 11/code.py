
"""
Computational Physics
Project 11
@Lalit Chaudhary
l.chaudhary@jacobs-university.de
"""

import numpy as np
import matplotlib.pyplot as plt

#Possible value of K and B to analyze
K = [0, 1]
B = [1, 5, 12]

#Initial conditions
t0 = 0
x0 = 1
v0 = -1

N = 200     #No. of data points
dt = 0.05  #Time step

#Discrete Fourier Transform
def DFT(ft):
    N = len(ft)
    fw= []                     #to store result of DFT
    for m in range(N):
        sum = 0.0
        for n in range(N):
            sum += ft[n] * np.exp(-1j * 2*np.pi * m * n / N)
        fw.append((sum / np.sqrt(N)))
    return np.abs(fw)


#Euler method of integration
def euler (k, b):
    x, v, t = x0, v0, t0        #Boundary condition
    n = 0                       #no. of data points calculated
    xarr, varr, tarr = [x], [v], [t]
    while n < N:
        
        a = -k*v - x**3 + b*np.cos(t)
        v = v + a*dt
        x = x + v*dt
        t = t+dt
        tarr.append(t)
        varr.append(v)
        xarr.append(x)
        n+= 1


    
    
    #Make relevant plots
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (15, 6))
    plt.suptitle('k = {}, B = {}'.format(k, b))

    #x(t) trajectory
    ax1.plot(tarr, xarr, 'b-')
    ax1.set_xlabel('time (t) [sec]')
    ax1.set_ylabel('Position (x) [meter]')
    ax1.set_title('x(t)')
  
    #fourier transform (linear)
    w = DFT(xarr)
    ax2.plot(tarr, w, 'b-', label = 'DFT')
    ax2.set_title('Fourier Transform (Linear Scale)')
    ax2.set_xlabel('time (t) [sec]')
    ax2.set_ylabel('w')

    #fourier transform (Logarithmic )
    ax3.set_yscale('log')
    ax3.plot(tarr, w, 'b-', label = 'DFT')
    ax3.set_title('Fourier Transform (Logarithmic Scale)')
    ax3.set_xlabel('time (t) [sec]')
    ax3.set_ylabel('w')

    plt.savefig('./Documents/k={},B={}.png'.format(k, b))


#Iterate and plot for all possible values of K and B
for kk in K:
    for bb in B:
        euler(kk, bb)


