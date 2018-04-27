from methods.intersect import *
def isObserverset(Pi):
	
	while len(Pi) > 0:
		for i in Pi[1:]:
			if not intersect(Pi[0],i):
				return(True)
		Pi.remove(Pi[0])
	return(False)
