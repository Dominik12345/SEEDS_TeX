# This file contains the model HANDY
# http://dx.doi.org/10.1016/j.ecolecon.2014.02.014

# Set Hidden Input Knots
hi_knots = [1,2,3,4]

# Parameters

parameters = {	'a_m' : 0.01, # normal birth rate 
		'a_M' : 0.07 , # famine bith rate
		'b_C' : 0.03, # death rate commoners
		'b_E' : 0.03 , # death rate elites
		'g' : 0.01 , # regeneration factor
		'd' : 1 , # rate of depletion per worker
		'l' : 100 , # nature saturation level
		's' : 0.0005 , # subsistence salary per capita
		'k' : 10 , # elites salary factor
		'r' : 0.005 , # minimum required consumption per capita

		'alpha1': 0.1,  # L1 regularisation
		'alpha2': 0.1   # L2 regularisation
}

# Variables and inital values

variables = { 	'x1' : 100 , # population of commoners 
		'x2' : 25 , # population of elites
		'x3' : 100 , # nature
		'x4' : 0   # accumulated wealth 
}

# System equations (dx1 abbrev. dx1/dt )

equations = {	'dx1' : '-a_C * x1 + b_c * x1' ,
		'dx2' : '-a_E * x2 + b_E * x2' ,
		'dx3' : 'gamma * x3 * (l - x3) - d * x1 * x3' ,
		'dx4' : 'd * x1 * x3 - C_C - C_E'
}

# Observables

observables = { 'y1' : 'x1' ,
		'y2' : 'x2' ,
		'y3' : 'x3' ,
		'y4' : 'x4'
}  

# Further Functions

functions = {
	'x4th' : 'r * x1 + k * r * x2' ,      # famine threshold
	'C_C' : 'min(1,x4/x4th) * s * x1' ,   # consumption of commoners
	'C_E' : 'min(1,x4/x4th) * k * s * x2', # consumption of elites
	'a_C' : 'a_m + max(0, 1 - C_c/(s*x1)) * (a_M - a_m)',
	'a_E' : 'a_m + max(0, 1 - C_E/(s*x1)) * (a_M - a_m)'
}
