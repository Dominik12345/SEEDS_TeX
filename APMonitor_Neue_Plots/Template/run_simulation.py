# Setup --->
import numpy as np
import random
import csv
from scipy.integrate import odeint
from simulation_model import *

# <--- Setup
#set random seed for data noise
random.seed(1)

#Make equations of nominal + wtrue
def equations(x,t):
   ret = []
   for i in range(0,len(x0)):
       i = nominal(x,t)[i] + wtrue(t)[i]
       ret.append(i)
	
   return(ret)

# solve and compute observations
solution = odeint(equations, x0, time)
solnom = odeint(nominal, x0, time)

data = [ [-1] * (len(observation(x0)) + 2 )  ]
for i in range(0,len(solution)-1):
	temp = observation(solution[i])
	data.append([time[i]] + temp + [0] )
data.append([time[len(solution)-1]] + observation(solution[ len(solution)-1 ]) + [1])

datanom = [ [-1] * (len(observation(x0)))  ]
for i in range(0,len(solnom)-1):
	temp = observation(solnom[i])
	datanom.append(temp)
datanom.append(observation(solnom[ len(solnom)-1 ]))


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
