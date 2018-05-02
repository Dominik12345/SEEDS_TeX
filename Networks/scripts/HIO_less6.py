import classes.Net as Net
from methods.randomNet import *
from methods.findObserverSet import *

#############################

# Network setup

number_nodes = 5
mean_edges_out = 2
bias = 0.6

number_errors = 2
number_observables = 2

#############################
N = 100
result = {'sHIO' : 0, 'notsHIO':0}

n = 0
while n < N:
	n = n + 1
# make randomNet
	net = randomNet(number_nodes, mean_edges_out,bias)
	i = 0
	while i < number_errors:
		net.get_nodes()[i].set_erroneous(True)
		i = i + 1
	while i < number_errors+number_observables:
		net.get_nodes()[i].set_observed(True)
		i = i + 1

#############################

	if findObserverSet(net,False):
		result['sHIO'] = result['sHIO'] + 1
	else:
		result['notsHIO'] = result['notsHIO'] + 1

print(result)


