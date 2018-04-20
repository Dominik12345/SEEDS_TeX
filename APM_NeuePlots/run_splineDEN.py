# Basic Setup --->
from APMonitor.apm import *
import json
import numpy as np
# apm setup 
server = 'http://byu.apmonitor.com' # run optimization on a provided server
app = 'DEN' # intern name of the optimization
apm(server, app, 'clear all') # ensure to start from scratch

# <--- Basic Setup

# Declare Model --->
# get model
import make_splinemodel # generates model.apm version of the model in model.py
from make_splinemodel import xi
from make_splinemodel import eta
from make_splinemodel import theta

apm_load(server, app, 'model.apm' ) # loads the model.apm file
# load data
csv_load(server, app, 'data.csv')
# <--- Declare Model

# Set Optimization Options --->
# apm_options(server, app , 'options', value) see documentation for more details 
apm_option(server, app, 'nlc.imode', 6) # dynamic optimization

# hidden input settings
for i in theta:
	apm_info(server, app, 'MV', i ) # hidden inputs as Manipulated Variable (subject of optimization)
	apm_option(server, app, i + '.status' , 1) # optW activate variable for manipulation
	apm_option(server, app, i + '.dcost'  , 0) # no penalty on dw1


# <--- Set Optimization Options

# Solve Optimization Problem --->
solver_out = apm(server, app, 'solve') # run optimization on server
solution = apm_sol(server, app) # get results of optimization

# put solution together in output_list (needed for json)
output_list = []
for i in list(solution.keys()):
	output_list.append( [i, list(solution[i])] )
#	output_list.append(list(solution[i]))

# Write data into data file
with open("solution.txt",'w') as outfile:
	json.dump( output_list , outfile )
# <--- Solve Optimization Problem

# Visualization --->
# console output
#print(output_list)
# <--- Visualization


#########
print('run completed')
