import classes.Node as Node
import classes.Edge as Edge
import classes.Net as Net
import classes.Path as Path

import numpy.random as rand
from itertools import product
from itertools import permutations
##########################

from methods.randomNet import *
from methods.findPath import *
from methods.intersect import *
from methods.isObserverSet import *
from methods.findObserverSet import *

##########################

net = randomNet(30,5,0.05)
net.get_nodes()[5].set_observed(True)
net.get_nodes()[6].set_observed(True)
net.get_nodes()[7].set_observed(True)
net.get_nodes()[8].set_observed(True)
net.get_nodes()[9].set_observed(True)
net.get_nodes()[10].set_observed(True)

net.get_nodes()[0].set_erroneous(True)
net.get_nodes()[1].set_erroneous(True)
net.get_nodes()[2].set_erroneous(True)
net.get_nodes()[3].set_erroneous(True)
net.get_nodes()[4].set_erroneous(True)

net.plot('Network')
###########################


sol = findObserverSet(net)
for i in sol:
	i.show()
