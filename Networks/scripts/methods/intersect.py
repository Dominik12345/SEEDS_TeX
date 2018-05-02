import classes.Path as Path

# intersect get two paths path1 and path2. 
# returns True if path1 and path2 share a common node
# returns False else

def intersect(path1,path2):
	for i in path1.get_nodes():
		for j in path2.get_nodes():
			if i == j:
				return(True)
	return(False)
