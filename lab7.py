# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 19:24:16 2021

@author: johnc
"""

import numpy as np
from scipy import random
import matplotlib.pyplot as plt


R = 1000# set length of wire in meters (m)
a1 = -R # set left end point of straight wire
b1 = R # set right end point of straight wire
N = 100000 # set number of intervals N


def f(x):
    return np.exp(-(x*x))
    

results = np.zeros(50)
avg = 0.0

for l in range(50):
    # generate an array of all zeroes 
    array1 = np.zeros(N)
    
    # change each entry in array to a random number between a and b
    for i in range(N):
        array1[i] = random.uniform(a1,b1)
       
        
    # compute summation over all random numbers in array
    integral = 0.0
    
   
    for x in array1:
        integral += f(x)
        
    inc = 0    
    # compute the average value for each 
    # contribution of force from each wire
    summation = ((b1-a1)/float(N)) * integral 
    results[l] = summation
    avg += summation
    print('Testing = ',summation)
    
   

avg = avg/50
print('Average = ', avg)

a = list(range(1,51))    
plt.plot(a, results)
plt.axhline(y = avg, color = 'r', linestyle = '-', label = 'average')
plt.legend()
plt.xlabel('Experiments Ran')
plt.ylabel('Averages of each Experiment')
plt.title('Average from each Experiment Ran')
plt.text(40,1.4,"Avg = %.02f" % avg)
    
    





