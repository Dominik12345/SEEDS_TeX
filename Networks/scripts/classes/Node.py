class Node:
	def __init__(self, name):
		self.name = name
		self.edges_in = []
		self.edges_out = []
		self.initial_value = 0
		self.observed = False
		self.erroneous = False
	# --->
	def is_observed(self):
		return(self.observed)
	def set_observed(self,boolean):
		self.observed = boolean
	def is_erroneous(self):
		return(self.erroneous)
	def set_erroneous(self,boolean):
		self.erroneous = boolean

	def get_name(self):
		return(self.name)
	def get_edges_in(self):
		return(self.edges_in)
	def get_edges_out(self):
		return(self.edges_out)
	def set_name(self,name):
		self.name = name
	def add_edge_in(self,edge):
		self.edges_in.append(edge)
	def add_edge_out(self,edge):
		self.edges_out.append(edge)
	def remove_edge(self,edge):
		self.edges_in.remove(edge)
		self.edges_out.remove(edge)
	def get_initial_value(self):
		return(self.initial_value)
	def set_initial_value(self, value):
		self.initial_value = value
	# <---

	def get_parents(self):
		parents = []
		for i in self.edges_in:
			parents.append(i.get_parent())
		return(parents)
	def get_children(self):
		children = []
		for i in self.edges_out:
			children.append(i.get_child())
		return(children)
