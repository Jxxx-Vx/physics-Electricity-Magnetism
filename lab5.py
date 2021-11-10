# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:12:16 2021

@author: johnc
"""

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


t= np.linspace(0,2*np.pi,1000,endpoint = True)
plt.plot(t,5*np.sin(t))
#plt.plot(t, signal.triang(len(t)))


plt.title('Sine wave − sampled at 1000 Hz')
#plt.title('Triangle wave - sampled at 1000 Hz')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid('True', which = 'both')
plt.axhline(y=0,color='k')
plt.ylim(-6,6)



