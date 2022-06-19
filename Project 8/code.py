
"""
Compuatational Physics II
Project 2
Lalit Chauhdary
l.chaudhary@jacobs-university.de
"""

import numpy as np
import matplotlib.pyplot as plt
import random

grid_spacing = [0.1, 0.05, 0.025, 0.0125]

r_squared = 0.5
r = np.sqrt(r_squared)

#Boundary of the domain 
def circe (x):
    return np.sqrt(r**2 - x**2)

def circe_neg (x):
    return -1*np.sqrt(r**2 - x**2)

#Function to be integrated
def f(x,y):
    return 2*x**2 + 3*x*y + y**2

#Number of points the function f was called on
number_of_points = []

#Analytical Solution of the Problem
analytical_solution = (3/4) * np.pi * r**4

#Using Midpoint Approximation
def Midpoint(h):
    Area_element = h**2
    x_points= np.arange(-r, r, h)

    """
    To test the domain and grid points
    plt.figure(1, figsize = (8,6))
    plt.plot(x_points, circe(x_points), 'b.-', label = 'Boundary Domain')
    plt.plot(x_points, circe_neg(x_points), 'b.-')
    """
    sum = 0
    n_points = 0            
    for i in range(1, len(x_points)):       
        mid_x = (x_points[i] + x_points[i-1])/2
        y_points = np.arange(circe_neg(x_points[i]), circe(x_points[i]), h)
        n_points+= (len(y_points))
        for j in range(1, len(y_points)):
            #plt.plot(x_points[i], y_points[j], 'ro')
            mid_y = (y_points[j] + y_points[j-1])/2
            sum+= f(mid_x,mid_y)
            #plt.plot(mid_x, mid_y, 'k.')
    #plt.legend()
    #plt.savefig('test.jpg')
    Integral =   sum*Area_element
    number_of_points.append(n_points)
    return Integral

#Monte Carlo Method with N points repeated k (=100 by default) times
def Monte_Carlo(N, m = 100):
    Integral = 0
    Number_of_repititons = m
    for k in range(Number_of_repititons):
        n = 0
        sum = 0
        while (n < N):
            x_point = random.uniform(-r, r)
            y_point = random.uniform(-r, r)
            if (x_point**2 + y_point**2 <= 0.5):
                sum+= f(x_point, y_point)
                #plt.plot(x_point, y_point, 'g.')
                n+= 1
            else:
                pass
        Integral+= sum*np.pi*r**2/N
    
    return Integral/Number_of_repititons
    #plt.show()


if __name__ == "__main__":
    print("\n Using Midpoint Approximation \n ...................\n")
    error = []
    for h in grid_spacing: 
        print("\nWith h = ", h)
        Integral = Midpoint(h)
        err = np.abs(analytical_solution - Integral)
        print("\nEvaluated Integral = ", Integral)
        print("Error = ", err)
        error.append(err)
    plt.figure(1, figsize = (8,6))
    plt.plot(number_of_points, error, 'g.--')
    plt.xlabel('N')
    plt.ylabel('Error')
    plt.title('[Midpoint Approximation]')
    #plt.savefig('errma.png')

    plt.figure(2, figsize = (8,6))
    print("\n Using Monte Carlo Method \n ...................\n")
    error = []
    for n in number_of_points:
        print("\nWith N = ", n)
        Integral = Monte_Carlo(n, 200)
        err = np.abs(analytical_solution - Integral)
        print("\nEvaluated Integral = ", Integral)
        print("Error = ", err)
        error.append(err)
    plt.plot(number_of_points, error, 'k.--')
    
    plt.title('[Monte Carlo Method]')
    plt.show()

  
