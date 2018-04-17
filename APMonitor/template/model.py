# This file contains the information about the model

# Set Hidden Input Knots
hi_knots = [1,2]

# Define Parameters of the model as a list

parameters = {	'a1' : 0.2 , 
		'a2' : 0.2 ,
		'a3' : 0.2 ,
		'b1' : 0.1 ,
		'b2' : 0.2 ,
		'b3' : 0.1 ,

		'alpha1': 0.1, # L1 regularisation
		'alpha2': 0.1   # L2 regularisation
}

# Declare variables and inital values

variables = { 	'x1' : 1 , 
		'x2' : 2 , 
		'x3' : 4 
}

# Define System equations (dx1 abbrev. dx1/dt )

equations = {	'dx1' : '-a1 * x1 + b3 * x3' ,
		'dx2' : '-a2 * x2 + b1 * x1' ,
		'dx3' : '-a3 * x3 + b2 * x2' 
}

# Define Observables

observables = { 'y1' : 'x1 +  x2' ,
		'y2' : 'x2 +  x3'
}  

