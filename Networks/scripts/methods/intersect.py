import classes.Path as Path
def intersect(path1,path2):
	for i in path1.get_nodes():
		for j in path2.get_nodes():
			if i == j:
				return(True)
	return(False)
