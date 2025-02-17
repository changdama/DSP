# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:47:22 2025

@author: Changda Ma
"""
import numpy as np
import matplotlib.pyplot as plt


#2.Convolution
##2.1 Convolution Function
def cvoltn(a,b):
    L=len(a)+len(b)-1

    ### Fill each side of a with len(b)-1 amount of 0
    Filled_a= np.pad(a, (len(b)-1, len(b)-1))

    ###reverse b
    reverse_b=b[::-1]

    ###initialize
    otput=np.zeros(L)

    ###dot product
    for n in range(L):
        window = Filled_a[n:n+len(b)]
        otput[n] = np.dot(window, reverse_b)
        
    return otput
###returns the result from a convolution between two random independent signals   
length_N = 10000
Sequence_a = np.random.randn(length_N)
Sequence_b = np.random.randn(length_N)
Sequence_a = 2 * (Sequence_a - np.min(Sequence_a)) / (np.max(Sequence_a) - np.min(Sequence_a)) - 1
Sequence_b = 2 * (Sequence_b - np.min(Sequence_b)) / (np.max(Sequence_b) - np.min(Sequence_b)) - 1

result = cvoltn(Sequence_a , Sequence_b)
print(result)

##2.2 Create Signals and Convolve
###Create two triangular windows with your own implementation
def tr_windw(N):
    windw = np.zeros(N)
    half_L=(N-1)/2
    for n in range(N):
        if n <= half_L:
            windw[n]=(2 * n) / (N-1)
        else:
            windw[n]=(2 * (N-1-n)) / (N-1)
    return windw

### Window length
N=101

### Generate two triangular windows
windw1=tr_windw(N) #a[n]
windw2=tr_windw(N) #b[n]

plt.plot(windw1, label='a[n]',color='grey')
plt.plot(windw2, label='b[n]',color='grey')
plt.xlabel('n')
plt.ylabel('Value')
plt.title('Triangular Windows a[n] and b[n]')
plt.show()

##2.3 Convolve
###Calculate the output y[n]
convolve_y=cvoltn(windw1,windw2)
print(convolve_y)
###Calculate the length of y[n]
convolve_y_L=N+N-1
print(convolve_y_L)            


##2.4 Plot and Interpret
#plot the convolution result
plt.plot(convolve_y, label='y[n]',color='grey')
plt.xlabel('n')
plt.ylabel('Value')
plt.title('Convolution result y[n]')
plt.show()
    