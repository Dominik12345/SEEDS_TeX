class Edge:
	
	def __init__(self,parent,child,weight):
		self.parent = parent
		self.child = child
		self.weight = weight

		parent.add_edge_out(self)
		child.add_edge_in(self)
	# --->
	def get_parent(self):
		return(self.parent)
	def get_child(self):
		return(self.child)
	def get_weight(self):
		return(self.weight)

	def set_parent(self, parent):
		self.parent = parent
	def set_child(self, child):
		self.child = child
	def set_weight(self, weight):
		self.weight = weight
	# <---
