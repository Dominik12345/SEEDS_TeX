# Setup --->
import numpy as np
import csv
from scipy.integrate import odeint
from simulation_model import *

# <--- Setup

# solve and compute observations
solution = odeint(equations, x0, time)

data = [ [-1 , -1 , -1, -1] ]
for i in range(0,len(solution)-1):
	data.append([time[i]] + observation(solution[i]) + [0] )
data.append([time[len(solution)-1]] + observation(solution[ len(solution)-1 ]) + [1])

# save
np.savetxt('data0.csv', data, delimiter = ',')
# reedit the data.csv file
with open('data0.csv','r') as input_file, open('data.csv','w') as output_file:
	counter = 0
	for line in input_file:
		if counter == 0:
			output_file.write(head)
		else:
			output_file.write(line)		
		counter = counter + 1
