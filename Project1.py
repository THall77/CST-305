# CST-305 Project1
# Tyler Allen Hall
# January 16,2022
# Graphs the Ethernet frame rate of a system.

from cmath import exp
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Ethernet frame rate is the rate at whic a device
# can send or recieve ethernet frames.

# The formula to calculate framerate is F = k/p.
# F = Frame rate
# k = constant
# p = framesize

def model(p,t):
    # Calculates above equaltion, result is in F/s.
    # The changing variable is the packet size.
     s = 2
     eth = 125000000/(p * s)
     return eth

# initial value
N0 = 1
# range
t = np.linspace(0, 1600)
# ODE solver
x = odeint(model,N0,t)

# Plots the graph.
plt.plot(t,x)
plt.title('Ethernet Frame Rate: Base case 1GB ethernet')
plt.xlabel('Size of packets (Bytes)')
plt.ylabel('Bits per second (s = 2)')
plt.show()