#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 16:41:54 2021

@author: lalitc
"""


import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats


#linear congruent generator
def LCG( m, a, c, lim, I0):
    r = [I0/m]
    for i in range (lim-1):
        I = (a*I0 + c)%m
        I0 = I                  #Update seed for next iteration
        ri = I0/m                #Random number between 0 and 1
        r.append(ri)
    return r

N = 1000
index = []    
# An example of common LCG
r = LCG(2**48, 25214903917, 11, N,0.4*2**48  )
print(r)  
  
#LCG with poor parameters
random_lcg = LCG(256, 57, 1, N, 256)    

#Randomly generated python array
random_python = []
for i in range(N):
    index.append(i+1)
    random_python.append(random.random())
    
#Checking randomness
plt.figure(1, figsize= (8,6))
plt.xlabel("Index i", fontsize = 14)
plt.ylabel(r"Random number, $r_i$", fontsize = 14)
plt.title(r'$r_i$ vs i [LCG]',  fontsize = 14)
plt.plot(index,random_lcg, 'b.')    
plt.savefig('1.png')

plt.figure(2, figsize= (8,6))
plt.xlabel("Index i",  fontsize = 14)
plt.ylabel(r"Random number, $r_i$",  fontsize = 14)
plt.title(r'$r_i$ vs i [Mersenne Twister generator]',  fontsize = 14)
plt.plot(index,random_python, 'g.')
plt.savefig('2.png')


#Plot of consecutive random numbers
plt.figure(3, figsize= (8,6))
plt.xlabel(r"$r_{2i}$",  fontsize = 14)
plt.ylabel(r"$r_{2i+1}$",  fontsize = 14)
plt.title(r'$r_{2i} \:vs\: r_{2i+1}$ [LCG]',  fontsize = 14)
for i in range(int(N/2-1)):
    plt.plot(random_lcg[2*i], random_lcg[2*i+1], 'b.')
plt.savefig('3.png')

plt.figure(4, figsize= (8,6))
plt.xlabel(r"$r_{2i}$",  fontsize = 14)
plt.ylabel(r"$r_{2i+1}$",  fontsize = 14)
plt.title(r'$r_{2i} \:vs\: r_{2i+1}$ [Mersenne Twister generator]',  fontsize = 14)
for i in range(int(N/2-1)):
    plt.plot(random_python[2*i], random_python[2*i+1], 'b.')
plt.savefig('4.png')


#Test of Uniformity using moment genrating function
k = 2
sum = 0 
plt.figure(5, figsize= (8,6))
i_u, r_u, root = [], [], []
for i in range (0, N):
    sum += random_lcg[i]**k
    d = sum/(i+1)
    r_u.append(d-(1/(k+1)))
    root.append(1/np.sqrt(i+1))
    
plt.xlabel('N',  fontsize = 14)
plt.title('Uniformity Test [LCG]')
plt.plot(index, r_u, label = 'deviation')
plt.plot(index, root, label = r'$1/\sqrt{N}')
plt.savefig('5.png')

k = 2
sum = 0 
plt.figure(6, figsize= (8,6))
i_u, r_u, root = [], [], []
for i in range (0, N):
    sum += random_python[i]**k
    d = sum/(i+1)
    r_u.append(d-(1/(k+1)))
    root.append(1/np.sqrt(i+1))
plt.title('Uniformity Test [Mersenne Twister generator]')
plt.plot(index, r_u, label = 'deviation')
plt.plot(index, root, label = r'$1/\sqrt{N}')
plt.savefig('6.png')

#RANDOM WALK

p = 0.8
x = 0 
l = 1

def visited (x, X):
    for xx in X:
        if x == xx:
            return True
        else:
            return False
        

N = [4, 8, 16, 32, 64, 128, 256]
ev_x = []
ev_x_sq = []
var = []
Dsteps = []
for n in N:
    print("For N = ", n)
    final_posx=[]
    final_posx_sq=[]
    k=0
    no = 1000
    sum = 0
    while (k<no):
        x = 0
        X = set ('0')
        for i in range(n):
            rl = random.random()
            #print(rl)
            if rl <= p:
                x+= l  
            else:
                x-= l   
            if (visited(x, X) == False):
                    X.add(x) 
        sum+= len(X)        
        final_posx.append(x)
        final_posx_sq.append(x**2)
        k+=1    
    Dsteps.append(sum/no)
    evx =  np.sum(final_posx)/len(final_posx)
    print('Expected values of x, <x> = ',evx)
    evx_sq = np.sum(final_posx_sq)/len(final_posx_sq)
    ev_x.append(evx)
    ev_x_sq.append(evx_sq)
    var.append(evx_sq - evx**2)    
    print('Variance of x, <del (x^2)> = ',evx_sq - evx**2)
plt.figure(7, figsize= (8,6))
plt.plot(N, Dsteps)
plt.title('Distinct Steps vs N', fontsize = 14)
plt.savefig('7.png')

plt.figure(8, figsize= (8,6))
plt.plot(N, var)
plt.title('Variance vs N', fontsize = 14)
plt.savefig('8.png')

    
