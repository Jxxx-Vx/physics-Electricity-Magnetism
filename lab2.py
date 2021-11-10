# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:11:42 2021

@author: johnc
"""

import matplotlib.pyplot as plt
import numpy as np
data = np.loadtxt("ohmslaw_data.txt")

x = data [ : , 0 ] 
y = data [ : , 1 ] 
n = len ( x ) #length of x array

#summation of an array by adding each element of array into sum
def sum_func(array):
    sum = 0
    for i in array:
        sum += i
    return sum

# Function for R, Linear Regression
def R(x,y,n):
    num = n*sum_func(x*y) - sum_func(x)*sum_func(y)
    denom = n*sum_func(x * x) - sum_func(x)*sum_func(x)
    return num/denom

#Build Function using I
def V(I):
    return I * R(x,y,n)


I = np.linspace(0,400,50)

plt.figure()
plt.xlabel("Current (A)")
plt.ylabel("Voltage (V)") 
plt.title("Current-Voltage Plot")

plt.scatter(x,y)
plt.plot(I,V(I), color='k')

plt.text(7, 10, r'$V =$ I*%0.3f' % R(x,y,n), fontsize=15)

plt.show()