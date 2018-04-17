import numpy as np

def equations(x,t):
	dx1 = -0.2 * x[0] + 0.1 * x[2] + np.sin(t)
	dx2 = -0.2 * x[1] + 0.1 * x[0] + 5. * np.exp(-t)+ 0.5
	dx3 = -0.2 * x[2] + 0.2 * x[1] 
	
	return([dx1,dx2,dx3])

x0 = [1.,2.,4.]

time = np.linspace(0,10)

head = 'time, y1obs, y2obs, last\n'

def observation(x):
	y1 = x[0] + x[1]
	y2 = x[1] + x[2]
	return([y1,y2])
