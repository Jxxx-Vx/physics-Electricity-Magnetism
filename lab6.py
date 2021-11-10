# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 12:55:58 2021

@author: johnc
"""

import matplotlib.pyplot as plt
import numpy as np

E = 10   # insert a value for the potential of a battery
C = 1  # insert a  value for the capacitance 
R = 2   # insert a value for resistance
t0 = 0  # note that t=0 is t0
q0 = 0  # At t=0, the capacitor has zero charge 
tf = 10 # we will assume final time is 10 seconds
n = 101 # here gives us 100 points from 0 to 10 seconds

def delta(t1,t2,n):
    return (t2 - t1) / (n - 1)


t = np.linspace(t0,tf,n) # set a value for t0,t1,...,tn
q = np.zeros([n]) # set every q-value to zero in an array format

q[0] = q0

for i in range (0,n):
    q[i] = delta(t0,tf,n) * (-1/(R*C) * q[i-1] + E/R)+ q[i-1]
    


    
q_exact = np.zeros([n])


for i in range (0,n):
    q_exact[i] = C*E*(1 - np.exp(-t[i] / (R  * C)))
    
error = np.zeros([n])
avg = 0
for i in range (1,n):
    error[i] = np.abs(q_exact[i]-q[i])/q_exact[i] * 100
    avg+=error[i]
    
avg/=n
print("avg: ",avg)
#plot
plt.plot(t,q, label='Approximation')
plt.plot(t,q_exact, label = 'Exact')
plt.text(8,6,"E=%.02f" % E)
plt.text(8,5,"C=%.02f" % C)
plt.text(8,4,"R=%.02f" % R)
plt.legend()
plt.xlabel("Time(s)")
plt.ylabel("Charge(C)")
plt.title("Approximation of Charge in RC Circuit")
plt.show()