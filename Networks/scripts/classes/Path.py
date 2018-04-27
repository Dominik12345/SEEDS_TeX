from classes.Net import Net

class Path(Net):
	
	def __init__(self,node1,node2,edge):
		if edge.get_parent() == node1 and edge.get_child() == node2:
			Net.__init__(self)
		
			self.add_node(node1)
			self.add_node(node2)
			self.add_edge(edge)
		else:
			print('Not possible')
			return(0)

	def get_last(self):
		return(self.nodes[-1])
	def get_first(self):
		return(self.nodes[0])
	# ---> methods
	def len(self):
		return(len(self.edges))
	def show(self):
		output = ''
		for i in self.nodes:
			output = output + i.get_name() + '->'
		print(output[:-2])
	# <--- methods

def concatenate(path1,path2):
	if not (path1.get_last() == path2.get_first()):
		return(0)
	else:
		path = Path(path1.get_edges()[0].get_parent(),
				 path1.get_edges()[0].get_child(),
				path1.get_edges()[0])
		for i in path1.get_nodes()[2:]:
			path.add_node(i)
		for i in path2.get_nodes()[1:]:
			path.add_node(i)
		for i in path1.get_edges()[1:]:
			path.add_edge(i)
		for i in path2.get_edges():
			path.add_edge(i)
		return(path)
