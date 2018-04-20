# This file contains the model JAK-STAT
# REFERENCE

# Set Hidden Input Knots
hi_knots = [1,2,3,4]

# Parameters

parameters = {	'k1' : 10**0.31		, # 
		'k2' : 10**(-1) 		, # 
		'k3' : 10**(-0.49)	, # 
		'k4' : 10**(0.42) 	, # 
		's1' : 10**(-0.21)	, # 
		's2' : 10**(-0.34) 	, # 
		'N'  : 10**(0.31) 	, #

		'alpha1': 0.1		, # L1 regularisation
		'alpha2': 0.1   	  # L2 regularisation
}

# Variables and inital values

variables = { 	'x1' : '10**(0.31)' 			, #
		'x2' : '0' 			 	, #
		'x3' : '0'			 	, #
		'x4' : '0'	 			  #
}

# System equations (dx1 abbrev. dx1/dt )

equations = {	'dx1' : '-k1 * x1' 			, #
		'dx2' : 'k1 * x1 - k2 * x2^2' 	, #
		'dx3' : '-k3 * x3 + 0.5 * k2 * x2^2' 	, #
		'dx4' : 'k3 * x3' 			  #
}

# Observables

observables = { 'y1' : 's1 * (x2 + 2 * x3)' 		, #
		'y2' : 's2 * (x1 + x2 + 2 * x3)'	  #
}  

# Algebraic Constraints

algebraic = { 'g1' : '2*x4 + 2*x3 + x1 + x2 - N' 	  # conservation law
}