
"""
Computational Physics
Project 3
@Lalit Chaudhary
l.chaudhary@jacobs-university.de
"""

import numpy as np 
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

h = 1/5
m = int(1/h)

square = (m+1, m+1)



def SetBoundary(V):
     V[0] = [100]*(m+1)
"""  
NOTE: The other boundary cases can be ignored in this specific problem since the inital
matrix by default has all initial components as 0. Also, the iterations in various methods
specifically ignore the boundary lines and hence preserving the boundary conditions.    
"""
def CheckPrecision(V1, V0):
    S = 0
    for i in range(1, m):
        for j in range(1, m):
            S += V1[i][j] - V0[i][j] 
    if S < 10**(-4):
        return False
    else:
        return True


#Jacobi's Method
V = np.zeros(square)

SetBoundary(V)

V1 = np.zeros(square)
SetBoundary(V1)

k = 1

status = True

while(status):
    for i in range(1, m):
        for j in range(1, m):
            temp = V[i+1][j] + V[i-1][j] + V[i][j+1] + V[i][j-1]
            V1[i][j] = temp/4
    for i in range(1, m+1):
        V[i][m] = V[i][m-1]        
    status = CheckPrecision(V1, V)        
    k += 1
    for i in range(1, m, 1):
        for j in range (1, m, 1):
            V[i][j] = V1[i][j]

x = np.linspace(0, 1, m+1)
y= np.linspace(0,1, m+1)
X,Y = np.meshgrid(x,y)



fig, ax = plt.subplots(1, 1, figsize=(10, 8), subplot_kw={'projection': '3d'})
ax.set_xlabel('y')
ax.set_ylabel('x')
ax.set_zlabel('Potential, V')
ax.view_init(elev=40, azim = 75)
ax.set_title('Surface Plot (Jacobi Method) [h= 1/30]', y = 1.1)
ax.text(1.0,0, 120,'Number of iterations = {}'.format(k) )
ax.plot_surface(X,Y, V1, cmap='cividis')
plt.savefig('J30')



#Gauss-Jacobi's Method
V = np.zeros(square)

SetBoundary(V)

V1 = np.zeros(square)
SetBoundary(V1)
k = 1

status = True

while(status):
    for i in range(1, m, 1):
        for j in range (1, m, 1):
            temp = V[i+1][j] + V1[i-1][j] + V[i][j+1] + V1[i][j-1]  
            V1[i][j] = temp/4
    for i in range(1, m+1):
        V[i][m] = V[i][m-1]        
    status = CheckPrecision(V1, V)        
    k += 1
    for i in range(1, m, 1):
        for j in range (1, m, 1):
            V[i][j] = V1[i][j]


x = np.linspace(0, 1, m+1)
y= np.linspace(0,1, m+1)
X,Y = np.meshgrid(x,y)



fig, ax = plt.subplots(1, 1, figsize=(10, 8), subplot_kw={'projection': '3d'})
ax.set_xlabel('y')
ax.set_ylabel('x')
ax.set_zlabel('Potential, V')
ax.view_init(elev=40, azim = 75)
ax.set_title('Surface Plot (Gauss-Jacobi Method) [h= 1/5]', y = 1.1)
ax.text(1.0,0, 120,'Number of iterations = {}'.format(k) )
ax.plot_surface(X,Y, V1, cmap='cividis')
plt.savefig('GJ5')


#SOR Method
w = 2/(1+np.pi/m)
V = np.zeros(square)

SetBoundary(V)

V1 = np.zeros(square)
SetBoundary(V1)
k = 1

status = True

while(status):
    for i in range(1, m, 1):
        for j in range (1, m, 1):
            temp = V[i+1][j] + V1[i-1][j] + V[i][j+1] + V1[i][j-1] 
            V1[i][j] = temp*w/4 + (1-w) * V[i][j]
    for i in range(1, m+1):
        V[i][m] = V[i][m-1]            
    status = CheckPrecision(V1, V)        
    k += 1
    for i in range(1, m, 1):
        for j in range (1, m, 1):
            V[i][j] = V1[i][j]

x = np.linspace(0, 1, m+1)
y= np.linspace(0,1, m+1)
X,Y = np.meshgrid(x,y)



fig, ax = plt.subplots(1, 1, figsize=(10, 8), subplot_kw={'projection': '3d'})
ax.set_xlabel('y')
ax.set_ylabel('x')
ax.set_zlabel('Potential, V')
ax.view_init(elev=40, azim = 75)
ax.set_title('Surface Plot (SOR Method) [h= 1/5]', y = 1.1)
ax.text(1.0,0, 120,'Number of iterations = {}'.format(k) )
ax.plot_surface(X,Y, V1, cmap='cividis')
plt.savefig('SOR5')