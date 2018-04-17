# This file contains the model predator-prey
# http://dx.doi.org/10.1016/j.ecolecon.2014.02.014

# Set Hidden Input Knots
hi_knots = [1,2]

# Parameters

parameters = {	'a' : 0.00003, # birth rate predator
		'b' : 0.02 , # death rate predator
		'c' : 0.03, # birth rate prey
		'd' : 0.0002 , # death rate prey
		
		'alpha1': 0.1,  # L1 regularisation
		'alpha2': 0.1   # L2 regularisation
}

# Variables and inital values

variables = { 	'x1' : 100 , # population of predators
		'x2' : 1000    # population of preys
}

# System equations (dx1 abbrev. dx1/dt )

equations = {	'dx1' : 'a * x2 * x1 - b * x1' ,
		'dx2' : 'c * x2 - d * x * y'
}

# Observables

observables = { 'y1' : 'x1' ,
		'y2' : 'x2'
}  

# Further Functions

functions = {
}
