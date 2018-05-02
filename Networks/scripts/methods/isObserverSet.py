from methods.intersect import *
import copy
# isObserveset checks if any two paths of Pi 
# intersect. Returns True if no two paths intersect
# and returns False else

def isObserverSet(Set):
	Pi = copy.copy(Set)
	while len(Pi) > 0:
		for i in Pi[1:]:
			if intersect(Pi[0],i):
				return(False)
		Pi.remove(Pi[0])
	return(True)
