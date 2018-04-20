import numpy as np
import random

noise = [1,2] #noise on y
noisesd = 0.015

def wtrue(t):
   w1 = -0.1*np.exp(-t)
   w2 = 0
   w3 = 0.025*np.arctan(t/2)
   w4 = 0
   
   return([w1,w2,w3,w4])

def nominal(x,t):
   dx1 = -1.0023 * x[0] + 1.005 * x[3]
   dx2 = -0.9943 * x[1] + 0.9923 * x[0] 
   dx3 = -1.0056 * x[2] + 1.0034 * x[1]
   dx4 = -1.0023 * x[3] + 0.9947 * x[2]
	
   return([dx1,dx2,dx3,dx4])

x0 = [1.,0.01,0.01,0.01]

time = np.linspace(0,10)

head = 'time, y1obs, y2obs, last\n'

def observation(x):
   y1 = x[1]
   y2 = x[3]
   return([y1,y2])
