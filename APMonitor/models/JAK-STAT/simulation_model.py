import numpy as np

def wtrue(t):
   w1 = 0
   w2 = 0
   w3 = np.arctan(t)
   w4 = 0
   
   return([w1,w2,w3,w4])
   
def nominal(x,t):
   dx1 = -10^(0.31) * x[0] * x[3]
   dx2 = 10^(0.31) * x[0] * x[3] - 10^(-1) * x[1]^2
   dx3 = -10^(-0.49) * x[2] + 0.5 * 10^(-1) * x[1]^2
   dx4 = 10^(-0.49) * x[2]
	
   return([dx1,dx2,dx3,dx4])

x0 = [10^(0.31),0.,0.,0.]

time = np.linspace(0,10)

head = 'time, y1obs, y2obs, last\n'

def observation(x):
   y1 = 10^(-0.21) * (x[1] + 2 * x[2])
   y2 = 10^(-0.34) * (x[0] + x[1] + 2 * x[2])
   return([y1,y2])
