#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lalit Chaudhary
Computational Physics
Project 4
"""
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from random import seed
from random import random
from random import randint
from datetime import datetime

N = 100          #No. of Cells
size = 7.5      #Size of each cell
vmax = 5        #Max speed of car
inf = -1        #Denotes empty cell
p = 0.2         #dawdle probability
n = 100         #No. of iterations to perform

#To generate random numbers
seed(datetime.now())

#Set up a street with N cells
def createStreet(N):
    S = []
    for i in range(N):
        S.append(inf)
    return S

#Count no. of empty cells after current position
def countEmpty(S, i):
    count = 0
    if (i+1 == N):
        i = -1
    while (S[i+1] == inf):
        i = i+1
        count = count+1
        if (i+1 == N):
            i = -1
    return count    
    
#Nagel-Schreckenberg model of traffic flow
def NaSc (S, n):
    
    #To store resulting matrix
    result=np.zeros(shape=(n, N)) 
    result[0] = S
    t = 0
    
    while (t < n):                  #iterate n times
    
        for i in range(len(S)):
            if(S[i] == inf):        #do nothing on empty cells
                continue
            
            if(S[i] < vmax):        #Accelerate if not at max speed
                S[i] = S[i]+1   
                
            d = countEmpty(S, i)
            S[i] = min(d, S[i])     #Prevent Collision
      
        for i in range(len(S)):     #Randomization with dawdle probability
            if(S[i] == inf):
                continue
            prob = random()
            if(prob < p and S[i]>0):
                S[i] = S[i] - 1
        
        Snew = [inf]*len(S)         #Store updated values in new array
        
        for i in range(len(S)):
            if(S[i] == inf):
                continue
            if (i+S[i] < N):         #make street Circular
                Snew[i+S[i]] = S[i]
            else:
                Snew[i+S[i]-N] = S[i]
                
        S=Snew.copy()               #pass udated array for next iteration
        result[t] = Snew            #Store updated array in matrix
        t = t+ 1
    return result
      
#For plotting the results
def Plot(result, title):
    #get discrete colormap
    cmap = plt.get_cmap('Greys', np.max(result)-np.min(result)+1)
    mat = plt.matshow(result,cmap=cmap,vmin = np.min(result)-.5, 
                                      vmax = np.max(result)+.5)
    cax = plt.colorbar(mat, ticks=np.arange(np.min(result),np.max(result)+1))

    plt.xlabel('Position on Road')
    plt.ylabel('Simulation Time')
    plt.title(title, loc='center')
    plt.show()
    #plt.savefig(title)
       
 
#Traffic jam with 6 cars; p = 0       
S = createStreet(N)
p = 0.0
pos = randint(0,80)             #position of traffic jam
for i in range(pos, pos+6):     
    S[i] = 0        

#12 other cars at random position 
for a in range (12):
    x = randint(0, 99)
    while (S[x] != inf):
        x = randint(0, 99)
    S[x] = randint(0, 5)
    
r1 = NaSc(S, n)     
Plot(r1, '18 Cars with p = 0')


#Traffic jam with 12 cars; p = 0
S2 = createStreet(N)
p = 0.0
pos = randint(0,80)             #position of traffic jam
for i in range(pos, pos+12):     
    S2[i] = 0        

#24 other cars at random position 
for a in range (24):
    x = randint(0, 99)
    while (S2[x] != inf):
        x = randint(0, 99)
    S2[x] = randint(0, 5)
    
r2 = NaSc(S2, n)     
Plot(r2, '36 Cars with p = 0')



#Traffic jam with 6 cars; p = 0.2    
   
S3 = createStreet(N)
p = 0.2
pos = randint(0,80)             #position of traffic jam
for i in range(pos, pos+6):     
    S3[i] = 0        

#12 other cars at random position 
for a in range (12):
    x = randint(0, 99)
    while (S3[x] != inf):
        x = randint(0, 99)
    S3[x] = randint(0, 5)
    
r3 = NaSc(S3, n)     
Plot(r3, '18 Cars with p = 02')

#Traffic jam with 12 cars; p = 0.2
S4 = createStreet(N)
p = 0.2
pos = randint(0,80)             #position of traffic jam
for i in range(pos, pos+12):     
    S4[i] = 0        

#24 other cars at random position 
for a in range (24):
    x = randint(0, 99)
    while (S4[x] != inf):
        x = randint(0, 99)
    S4[x] = randint(0, 5)
    
r4 = NaSc(S4, n)     
Plot(r4, '36Cars with p = 02')





