
"""
Compuatational Physics II
Project 9
Lalit Chauhdary
l.chaudhary@jacobs-university.de
"""

import numpy as np
import matplotlib.pyplot as plt
import random

#function to be integrated
def f(x):
    return (x**2 + x)*np.exp(-x)


analytical_solution = np.exp(-5)*(7*np.exp(4)-43)

#3 probability distribution functions
def p_a(x):
    norm_factor = 0.25
    return 0.0 if (x < 0) else norm_factor

def p_b(x):
    norm_factor = 1/(np.exp(-1)-np.exp(-5))
    return 0.0 if (x < 0) else norm_factor * np.exp(-x)


def p_c(x):
    norm_factor = 1/analytical_solution
    return 0.0 if (x < 0) else norm_factor * f(x)

#Paramateres 
del_x = 0.1
low_lim, upp_lim = 1, 5
no_of_intervals = int((upp_lim - low_lim) / del_x)

#Metropolis Algorithm
def metropolis(prob, low_lim, upp_lim, max_step, n):
    x_initial = random.uniform(low_lim, upp_lim)

    accepted = []
    accepted.append(x_initial)

    i = 0
    integral = f(x_initial)/prob(x_initial)
    while (i <=n ):
        x_low = low_lim if accepted[i] - max_step < low_lim else accepted[i] - max_step
        x_upp = upp_lim if accepted[i] + max_step > upp_lim else accepted[i] + max_step
        x_trial = random.uniform(x_low, x_upp)
        w = prob(x_trial)/prob(accepted[i])
        
        if w >= 1:
            accepted.append(x_trial)
        
        else:
            r = random.uniform(0, 1)
            if r <=w:
                accepted.append(x_trial)
            else:
                accepted.append(accepted[i]) 
        i+= 1
        integral+= f(accepted[i])/prob(accepted[i])
    return accepted, integral/n


N_arr = [1000*i for i in range(1, 11)]
d_steps = [2, 2.5, 3]

#Graph of function
x = np.linspace(1,5,100)
plt.plot(x, f(x), 'k-')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

#For 3 step sizes
for d in d_steps:
    plt.figure(figsize=(10,8))
    accepted = metropolis(p_c, 1, 5, d, 1000)[0]
    plt.hist(accepted, bins=no_of_intervals,)
    
    #plt.xlim(1,5)
    plt.title('p_c with d = %.2f'%d)
    plt.show()

#Colour for each line of the plot
colour = [['r.-', 'b.-', 'g.-'], ['k.-', 'c.-', 'm.-'], ['y.-', 'rs-', 'bs-']]

I_pa = [[], [], []]
I_pb = [[], [], []]
I_pc = [[], [], []]
for d in range(len(d_steps)):
    for n in N_arr:
        I_pa[d].append((metropolis(p_a, 1, 5, d_steps[d], n))[1])
        I_pb[d].append((metropolis(p_b, 1, 5, d_steps[d], n))[1])
        I_pc[d].append((metropolis(p_c, 1, 5, d_steps[d], n))[1])

for d in range(len(d_steps)):
    plt.figure(figsize=(10,8))
    plt.xlabel("N")
    plt.ylabel("Value of integral")
    plt.plot(N_arr, I_pa[d], colour[0][0] , label = "p_a")
    plt.plot(N_arr, I_pb[d], colour[0][1],label = "p_b")
    plt.plot(N_arr, I_pc[d], colour[0][2] , label = "p_c")
    plt.plot(range(0, N_arr[-1], 1000), [analytical_solution+(i-i) for i in range(0, N_arr[-1], 1000)], 'k-', label = 'Analytical Solution')
    plt.legend(loc = 2)
    plt.title("d = %.2f"%d_steps[d])
    plt.show()

