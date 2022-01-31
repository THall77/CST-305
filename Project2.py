# Tyler Hall
# CST-305
# Professor Ricardo Citro
# Jan 30, 2022

# Project 2

"""
This program is designed to calculate the given
ODE using the Runge Kutta Method, giving about 1000-2000
solutions, then displaying the computation time.

The goal is to not only get a better understanding of the RK 
Method, it's also supposed to explore the trade-off between
computation time and accuracy of the true solution.

"""

from math import exp
import scipy as sci
import time

# Equation given to solve.
def f(x, y):
    return y / (exp(x) - 1)

# Function to perform RK method.
def rkm(x0,y0,h,n):
    # Printing a format so the table looks nice.
     print('\n--------Solutions--------')
     print('-------------------------')    
     print('x0\ty0\tTrue Solution')
     print('-------------------------')
     # Loop to solve using RKM for every step.
     for i in range(n):
         # Standard RK Method
         k1 = h * (f(x0, y0))
         k2 = h * (f((x0 + h / 2),(y0 + k1 / 2 * h)))
         k3 = h * (f((x0 + h / 2),(y0 + k2 / 2 * h)))
         k4 = h * (f((x0 + h), (y0 + k3 * h)))
         # Finds true solution
         k = (k1 + 2 * k2 + 2 * k3 + k4) / 6
         ts = y0 + k
         # Displays initial values and true solution, with 3 decible points.
         print('%.3f\t%.3f\t%.3f'% (x0,y0,ts) )
         print('-------------------------')
         # Increments by h
         y0 = ts
         x0 = x0+h

# Starts clock for computation time.
start_time = time.time()

# Performs the RKM 1500 times.
rkm(1, 5, 0.02, 1500)

# Resulting time
comp_time = (time.time() - start_time)

print('\nResulting computation time is: ')
print('%.3f'% (comp_time))