import classes.Node as Node
import classes.Edge as Edge
import classes.Net as Net
import classes.Path as Path

import numpy.random as rand
from itertools import product
from itertools import permutations
##########################

from methods.randomNet import *
from methods.findPath import *
from methods.intersect import *
from methods.isObserverset import *

##########################

net = randomNet(30,2,0.05)
net.get_nodes()[21].set_observed(True)
net.get_nodes()[20].set_observed(True)
net.get_nodes()[0].set_erroneous(True)
net.get_nodes()[1].set_erroneous(True)


net.plot('Network')
###########################

Gamma = {}

for i in net.get_nodes():
	if i.is_erroneous():
		Gamma[i.get_name()] = {}
		for j in net.get_nodes():
			if j.is_observed():
				Gamma[i.get_name()][j.get_name()] = findPath(net,i,j)
#for i in Gamma:
#	print('from ' + i)
#	for j in Gamma[i]:
#		print('to ' + j)
#		print(len(Gamma[i][j]))
#		for k in Gamma[i][j]:
#			k.show()
#			print(' % ')

error_nodes = list(Gamma.keys())
observed_nodes = list(Gamma[error_nodes[0]].keys())

index = []
for i in permutations( observed_nodes, len(error_nodes)):
	index.append(list(i))
#print(index)

solution = []

step = 0
for temp_index in index:
	l = []
	for i in range(0,len(error_nodes)):
		l.append(len(Gamma[error_nodes[i]][temp_index[i]]))
	k = [0]*len(error_nodes)
	#print('l = ' + str(l))
	check2 = True
	check3 = True
	while check2:
		step = step + 1
		Pi = []
		#print('k = ' + str(k))
		for i in range(0,len(error_nodes)):
			if len(Gamma[error_nodes[i]][temp_index[i]]) == 0:
				check3 = False	
			else:
				Pi.append(Gamma[error_nodes[i]][temp_index[i]][k[i]])
				check3 = True
		#print('Testing Pi')
		if check3 and isObserverset(Pi):
			print('Hidden Input Observable')
			solution = Pi
			break

		check = False
		h1 = 0
		while not check:
			if k[h1] < (l[h1]-1):
				k[h1] = k[h1] + 1
				check = True
			elif k[h1] == (l[h1] - 1) and h1+1 < len(l):
				k[h1] = 0
				h1 = h1 + 1	
			else:
				if check == False:
					check = True
				else:
					check = True
					print('Error')
				check2 = False
print('success after' + str(step))
for i in solution:
	i.show()
