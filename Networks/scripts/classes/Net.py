import matplotlib.pyplot as plt
import numpy as np

class Net:
	def __init__(self):
		self.nodes = []
		self.edges = []
		
	# --->
	def get_nodes(self):
		return(self.nodes)
	def get_edges(self):
		return(self.edges)
	def add_node(self,node):
		self.nodes.append(node)
	def add_edge(self,edge):
		self.edges.append(edge)
	# <---

	# ---> plot method

	def plot(self, plotname):
		# positions of nodes
		N = len(self.nodes)
		dphi = 2*np.pi / N
		x_pos = []
		y_pos = []
		names = []
		for i in range(0,N):
			x_pos.append(N * np.cos(i*dphi) * 1./(1+
				len(self.nodes[i].get_edges_in()))**(1/2))
			y_pos.append(N * np.sin(i*dphi) * 1./(1+
				len(self.nodes[i].get_edges_in()))**(1/2))
			names.append(self.nodes[i].get_name())
		# make scatter plot
		fig, ax = plt.subplots()
		ax.get_xaxis().set_visible(False)
		ax.get_yaxis().set_visible(False)
		ax.scatter(x_pos, y_pos,zorder = 2, s=200, alpha = 0.5)
		for i, name in enumerate(names):
			ax.annotate(name,(x_pos[i],y_pos[i]),
				horizontalalignment='center',
                		verticalalignment='center',
                 		size=10
			)
		# make edges
		linewidth = 0.2 * N
		for edge in self.edges:
			x1 = x_pos[names.index(edge.get_parent().get_name())]
			y1 = y_pos[names.index(edge.get_parent().get_name())]
			x2 = x_pos[names.index(edge.get_child().get_name())]
			y2 = y_pos[names.index(edge.get_child().get_name())]
			ax.arrow(x1 + 0.1 * (x2-x1),y1+ 0.1 * (y2-y1),0.8 * (x2-x1),0.8*(y2-y1), 
				zorder = 1, fc="k", ec="k",
                         	head_width=0.1*linewidth, head_length=0.1*linewidth
			)

		fig.savefig(plotname + '.png')
	# <--- plot method

