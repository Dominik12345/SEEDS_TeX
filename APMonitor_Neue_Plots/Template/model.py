# This file contains the information about the model

# Set Hidden Input Knots
hi_knots = [1,3]

# Define Parameters of the model as a list

parameters = {	'a1' : 0.1 , 
		'a2' : 0.1 ,
		'a3' : 0.1 ,
      'a4' : 0.1 ,
		'b1' : 0.2 ,
		'b2' : 0.2 ,
		'b3' : 0.2 ,
      'b4' : 0.2 ,

		'alpha1': 5, # L1 regularisation
		'alpha2': 0.1   # L2 regularisation
}

# Declare variables and inital values

variables = { 	'x1' : 1 , 
		'x2' : 0.01 , 
		'x3' : 0.01 ,
      'x4' : 0.01
}

# Define System equations (dx1 abbrev. dx1/dt )

equations = {	'dx1' : '-a1 * x1 + b4 * x4' ,
		'dx2' : '-a2 * x2 + b1 * x1' ,
		'dx3' : '-a3 * x3 + b2 * x2' ,
      'dx4' : '-a4 * x4 + b3 * x3'
}

# Define Observables

observables = { 'y1' : 'x1 +  x2 + 2*x3' ,
		'y2' : 'x2 + 2 * x3' ,
      'y3' : 'x3'
}  

