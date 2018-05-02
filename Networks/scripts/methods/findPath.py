import classes.Path as Path

# findPaths returns all nonselfintersecting paths in 
# network starting at startnote and ending at finalnode

def findPath(net,startnode, finalnode):
	# a path longer than max_len must contain
	# loops
	max_len = len(net.get_nodes())
	# Gamma is temporary list of instances if Path,
	# Pi contains only the paths from startnode to finalnode
	Gamma = []
	Pi = []
	# initialize the first paths as Path from startnode 
	# to starnode.get_childen()
	for edge in startnode.get_edges_out():
		temp_path = Path.Path(
			edge.get_parent(),
			edge.get_child(),
			edge
		)
		if temp_path.get_last() == finalnode:
			Pi.append(temp_path)	
		else:
			Gamma.append(temp_path)
	# this happens if startnode.get_children()=finalnode
	if len(Gamma) == 0:
		return(Pi)

	i = 0
	while True:
		i = i + 1 # only for emergency break
		# Gamma gets updated by remove Gamma[0] and Gamma.append
		path = Gamma[0]
		temp_node = path.get_last()
		# in each iteration, take the last node and append 
		# the child of each edge in edges_out
		for edge in temp_node.get_edges_out():
			temp_path = Path.concatenate(
				path ,
				Path.Path(edge.get_parent(),edge.get_child(),edge)
			)			
			#print('temp_path')
			#temp_path.show()
			if temp_path.get_last() == finalnode:
				Pi.append(temp_path)
				#print('added')
			elif not temp_path.get_last() in path.get_nodes():
				Gamma.append(temp_path)
				#print('appended')
		Gamma.remove(path)
		
		if len(Gamma) == 0:
			#print('Empty Gamma')
			break
		elif Gamma[-1].len() > max_len:
			print('max_len reached')
			break
		# arbitrary emergency break to avoid unexpectedly long 
		# computation times
		elif i > 10000:
			print('findPath stopped after ' + str(i) + ' combinations')
			break
	return(Pi)

