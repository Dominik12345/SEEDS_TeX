import classes.Path as Path

# findPaths returns all nonselfintersecting paths in 
# network starting at startnote and ending at finalnode
def findPath(net,startnode, finalnode):
	max_len = len(net.get_nodes())
	#print(max_len)
	Gamma = [] # temporary paths
	Pi = [] # final paths to return
	for edge in startnode.get_edges_out():
		temp_path = Path.Path(
			edge.get_parent(),
			edge.get_child(),
			edge
		)
		#print('Initialize')
		#temp_path.show()
	
		if temp_path.get_last() == finalnode:
			Pi.append(temp_path)
			#print('Yeah')	
		else:
			Gamma.append(temp_path)
	if len(Gamma) == 0:
		return(Pi)

	i = 0
	while True:
		i = i + 1 # only for emergency break
		# Gamma gets update by remove Gamma[0] and Gamma.append
		path = Gamma[0]
		#print('Iterate Gamma')
		#path.show()
		temp_node = path.get_last()
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
			#print('Max len reached')
			break
		elif i > 10000:
			print('emergency break')
			break
	return(Pi)

