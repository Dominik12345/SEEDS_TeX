from model import *

# check if model can be build
if len(variables) != len(equations):
	print('problem: number of equations and state space dimension do not coincide')
	quit()
if len(hi_knots) > len(variables):
	print('problem: more hidden inputs that state variables')
	quit()
if max(hi_knots) > len(variables):
	print('problem: hidden input on nonexisting knot')
	quit()


# Rewrite model as strings in APMonitor style --->
# variables
str_variables = ''
for i in range(0,len(variables)):
	str_variables = ( str_variables + '\t\t' + list(variables.keys())[i] + ' = ' + 
	str(list(variables.values())[i]) +'\n' )

# parameters
str_parameters = ''
for i in range(0,len(parameters)-2):
	str_parameters = ( str_parameters + '\t\t' + list(parameters.keys())[i] + ' = ' + 
	str(list(parameters.values())[i]) +'\n' )

str_parameters = str_parameters + '\n\t\t!apm stuff\n\t\t'+list(parameters.keys())[len(parameters)-2] + ' = ' + str(list(parameters.values())[len(parameters)-2])+ '\n\t\t' +list(parameters.keys())[len(parameters)-1] + ' = ' + str(list(parameters.values())[len(parameters)-1])

# observables y
str_observables = ''
for i in range(0,len(observables)):
	str_observables = ( str_observables + '\t\t' + list(observables.keys())[i] + ' = ' + list(observables.values())[i] + '\n')

# measurements yobs
measurements = []
str_measurements = ''
for i in range(0,len(observables)):
	measurements.append('y' + str(i+1) + 'obs') 
	str_measurements = (str_measurements + '\t\t' + measurements[i] + '\n')

#  hi (hidden inputs)
hi = []
str_hi = ''
for i in range(0,len(hi_knots)):
	hi.append('w'+ str(i+1))
	str_hi = str_hi + '\t\t' + hi[i] + '\n'

# equations
str_equations = ''
tempcount = 0
for i in range(0,len(equations)):
	str_equations = ( str_equations + '\t\t' + list(equations.keys())[i] + ' = ' + 
	str(list(equations.values())[i]) )
	if tempcount < len(hi_knots) and hi_knots[tempcount] == (i+1):
		str_equations = str_equations + ' + ' + hi[tempcount]
		tempcount = tempcount + 1
	str_equations = str_equations + '\n'

# objective function
str_objective = ''
for i in range(0,len(measurements)):
	str_objective = str_objective +'(' + measurements[i] +' - ' + list(observables.keys())[i] +')**2 + '
for i in range(0,len(hi)):
	str_objective = (str_objective + 'alpha2/2. * ' + '(' + hi[i] + ')**2' )  
	if i != (len(hi)-1):
		str_objective = str_objective + ' + '
#+ 'alpha1 * ' +'abs('+ hi[i]+')' +' + ' L1

# concatenate strings
write_parameters = (str_parameters + '\n\t\tlast\n' + str_measurements + str_hi) 

write_equations = '\t\tminimize last * J\n' + '\t\tdJ = ' + str_objective+ '\n\n' + str_equations + '\n' + str_observables 

write_variables = '\t\tJ = 0\n\n' + str_variables + '\n' + str_observables

# <--- Rewrite model as strings in APMonitor style

# open .apm file
modelfile = open('model.apm','w')

# write model into file 
modelfile.write('Model\n\n')
modelfile.write('\tParameters\n' + write_parameters + '\tEnd Parameters')
modelfile.write('\n\n')
modelfile.write('\tVariables\n' + write_variables + '\tEnd Variables')
modelfile.write('\n\n')
modelfile.write('\tEquations\n'+ write_equations + '\tEnd Equations')
modelfile.write('\n\nEnd Model')


#close .apm file
modelfile.close()



### TO DO (later) ###

# Adjust the file
# read in the file
with open('model.apm', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('dx', '$x')
filedata = filedata.replace('dJ', '$J')
# Write the file out again
with open('model.apm', 'w') as file:
  file.write(filedata)
