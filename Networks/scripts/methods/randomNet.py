import classes.Edge as Edge
import classes.Net as Net
import classes.Node as Node
import numpy as np

def randomNet(number_nodes, in_nodes, bias):
	net = Net.Net()
	for i in range(0,number_nodes):
		net.add_node(Node.Node('x' + str(i+1)))
	for i in range(0,number_nodes):
		for j in range(0,number_nodes):
			if i == j:
				prob = 0
			else:
				prob = (1-bias) * in_nodes/number_nodes
		
			node1 = net.get_nodes()[i]
			node2 = net.get_nodes()[j]
			temp = np.random.choice([True,False],
				 p = [prob,1-prob]
			) 	
			if temp:
				e = Edge.Edge(node1,node2,1)
				net.add_edge(e)
				bias = bias * (1-bias)
	return(net)
