import classes.Node as Node
import classes.Edge as Edge
import classes.Net as Net
import classes.Path as Path

from methods.findPath import *
from methods.intersect import *
from methods.isObserverSet import *

from itertools import permutations

#############################

def findObserverSet(net, returnset):
	
	# temporary path set Gamma is a dictionary
	# Gamma['x1']['x2'] = [path1,... ]
	# with instances of Path
	# path1.get_first() = x1, path1.get_last() = x2
	Gamma = {}
	# fill up dictionary keys with keys of erroneous and observed nodes
	# and use findPath to get all paths from i to j
	for i in net.get_nodes():
		if i.is_erroneous():
			Gamma[i.get_name()] = {}
			for j in net.get_nodes():
				if j.is_observed():
					Gamma[i.get_name()][
					j.get_name()] = findPath(net,i,j)
	# for a easier handling of keys
	error_nodes = list(Gamma.keys())
	observed_nodes = list(Gamma[error_nodes[0]].keys())

	# make a multiindex of all observed_nodes permutation. Then
	# (error_nodes,index) is the set of all in-out combinations 
	# without repeatings. Note index[0] itself is a list of keys.
	index = []
	for i in permutations( observed_nodes, len(error_nodes)):
		index.append(list(i))


	# initialize an iteration step counter
	step = 0

	# iterate over all index combinations
	for combi in index:
		# each Gamma[error_node[i]][observed_node[combi[i]]] is a list
		# of paths. k is another multiindex to get through all 
		# combinations.
		# get the number of paths from error_node[i]
		# to the observed_node[combi[i]]
		l = [] 
		for i in range(0,len(error_nodes)):
			l.append(len(Gamma[error_nodes[i]][combi[i]]))
		k = [0]*len(error_nodes)

		# while loop iterates over all mulitindices k
		check_combi = True
		while check_combi:
			step = step + 1
			observerSet = []
			check_pathexists = True
			# if a path from error_node[i] to 
			# observed_node[combi[i]] exists add it to the
			# observerSet
			for i in range(0,len(error_nodes)):
				if len(Gamma[error_nodes[i]][combi[i]]) == 0 :
					check_pathexists = False
				else:
					observerSet.append(
					 Gamma[error_nodes[i]][combi[i]][k[i]]
					)
			# if all paths exists and do not intersect, 
			# observerSet is the solution
			if check_pathexists and isObserverSet(observerSet):
				print('structural Hidden Imput Observable')
				print('Success after ' + str(step) + 
				' iterations')
				if returnset:
					return(observerSet)
				else:
					return(True)
			# make the next k
			check_iterate = True
			h = 0
			while check_iterate:
				# iterate k=(k[0],0,0...) from 0 to l[0], 
				# if k[0]==l[0], set k[1]+=1 and iterate 
				# k[0] again until k[1] == l[1]. Then k[2]+=1
				# and so on
				if k[h] < (l[h]-1):
					k[h] = k[h] + 1
					check_iterate = False
				elif k[h] == (l[h] - 1 ) and h+1 < len(l):
					k[h] = 0
					h = h + 1
				else:
					# the very lasst iteration ends in
					if check_iterate == True:
						check_iterate = False
					else:
						# if this happens something
						# went wrong 
						check_iterate = False
						print('Error: k-iteration')
					# the iteration over all k is done
					# proceed with the next combi
					check_combi = False

	print('not structural Hidden Input Observable')
	print('Stopped after ' + str(step)+ ' iterations')
	if returnset:
		return([])
	else:
		return(False)
