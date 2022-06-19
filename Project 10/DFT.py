
"""
Compuatational Physics II
Project 10
Lalit Chauhdary
l.chaudhary@jacobs-university.de
"""
import numpy as np
import matplotlib.pyplot as plt

#Discrete Fourier Transform
def DFT(ft):
    N = len(ft)
    fw= []                     #to store result of DFT
    for m in range(N):
        sum = 0.0
        for n in range(N):
            sum += ft[n] * np.exp(-1j * 2*np.pi * m * n / N)
        fw.append((sum / np.sqrt(N)))
    return fw

#Inverse Discrete Fourier Transform     
def InverseDFT(fw):
    N = len(fw)
    ft = []
    for n in range(N):
        sum = 0.0
        for m in range(N):
            sum += fw[m] * np.exp(1j * 2* np.pi * m * n / N)
        ft.append(sum/np.sqrt(N))
    return ft

#PART A
#Input Gaussian
Gaussian_data = []
mu  = 0                       #Mean
sigma = 0.5                   #Standard deviation
N = 50                        #Number of data points

x = np.linspace(-2, 2, N)

def gaussian (x):
    return 1/(sigma * np.sqrt(2*np.pi)) * np.exp (-(x - mu)**2 /(2*sigma**2))

#Input data array
for xx in x:
    Gaussian_data.append(gaussian(xx))

plt.plot(x, Gaussian_data, label = 'Original data')

DFT_gaussian = DFT(Gaussian_data)

#Separate real, imaginary and absolute value of result
DFT_gaussian_real = [d.real for d in DFT_gaussian]
DFT_gaussian_imag = [d.imag for d in DFT_gaussian]
DFT_gaussian_abs = [np.abs(d) for d in DFT_gaussian]

plt.plot(x,DFT_gaussian_abs, label = 'magnitude')
plt.plot(x,DFT_gaussian_real, label = 'real part')
plt.plot(x,DFT_gaussian_imag, label = 'imaginary part')

plt.legend()
plt.show()

#PART B
def f(x):
    return np.sin(x)**2 * np.exp(-(x-np.pi/2)**2)

x = np.linspace(0, 3, 50)

data = [f(t) for t in x]

DFT_data = DFT(data)
Inverse_data = InverseDFT(DFT_data)

plt.figure(2)
plt.plot(x, data, 'k.', label = 'original data')
plt.plot(x, [i.real for i in DFT_data], label = 'After DFT')
plt.plot(x, [i.real for i in Inverse_data], label = 'Retrieved data after IDFT')
plt.legend()
plt.show()

#Compare the original data and the back transformed data
diff = 0
for i in range (len(data)):
    diff += np.abs (data[i] - Inverse_data[i].real)

if diff >= 1*10**(-7):
    print('There is some deviation between the original and the retrieved data')
else:
    print('The original and the retrieved data are similar')

