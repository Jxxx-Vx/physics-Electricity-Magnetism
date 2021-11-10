# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 19:42:19 2021

@author: johnc
"""

import matplotlib.pyplot as plt
import numpy as np
data = np.loadtxt("LED_data.txt")

x = data [ : , 0 ] 
y = data [ : , 1 ] 
n = len ( x ) #length of x array

def sum(array):
    sum = 0
    for i in array:
        sum += i
    return sum

def a(x,y,z):
    num = sum(x*x*y)*sum(y*np.log(y)) - sum(x*y)*sum(x*y*np.log(y))
    denom = sum(y)*sum(x*x*y) -(sum(x*y) * sum(x*y))
    return num/denom


def b(x,y,z):
    num = sum(y) * sum(x*y*np.log(y)) - sum(x*y) * sum(y*np.log(y))
    denom = sum(y) * sum(x*x *y) - (sum(x*y)*sum(x*y))
    return num/denom

def I(a,b,v):
    return np.exp(a) * np.exp(b*v)

v = np.linspace(0,5,n)

plt.figure()
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)") 
plt.title("Current-Voltage Plot")

plt.scatter(x,y)

plt.plot(v,I(a(x,y,n),b(x,y,n),v), color='Green')
plt.text(0, 10, r'$I =$%0.3f ' % np.exp(a(x,y,n)) + '* $e^{%0.3f * v}$' % b(x,y,n), fontsize=15)

plt.show()

    



