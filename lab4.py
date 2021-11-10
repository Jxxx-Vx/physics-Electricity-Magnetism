# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 17:36:13 2021

@author: johnc
"""
import numpy as np
def linear():
    x = 0
    while x < 100:
        if 2*x+5 == 13:
            print('x = ', x)
            break
        x+=1
        
        
def double():
    x=0
    y=0
    while x < 100:
        while y < 100:
            if 2*x + 3*y == 20:
                print('(x,y) = ',(x,y))
            y+=1
        y = 0
        x += 1


def voltage():
    x=0
    y=0
    while x < 1000:
        while y < 1000:
            if 0.5*x + y == 12:
                print('(r,v) = ',(x,y))
            y+=1
        y = 0
        x += 1
        
def exponential():
    I = 20
    A = 0.5
    V = round((np.log((I/A))/0.95), 5)
    
    print('(I, A, V) =', (I,A,V))
    
voltage()
exponential()

