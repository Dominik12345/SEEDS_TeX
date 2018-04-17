# This python 3.6 scipt guides through the building of a model.py 

import os, errno

# setup
Break_Statement = 'done'
Exit_Statement = 'exit'


# Start Message
print(
'This python 3.6 script guides you through the building of your \
own model.py file.\n'
)


# Accumulate Data
# Define the Title of your Model
title = input('Please enter the name of your model: ')
reference = input('Reference, type "done" to skip: ')
# Define the parameters

print('\n\nStep 1 of 5: Define the parameters of the model. Type "done" \
if you want to go to the variables.')

parameters = {}

i = 1
while 1:
    temp_name = input(str(i) + '-st parameter: ')
    if temp_name == Break_Statement:
        break
    elif temp_name == Exit_Statement:
        print('Not yet implemented')
    else:
        temp_val = input('value: ')
        
    if temp_val == Break_Statement:
        break
    elif temp_val == Exit_Statement:
        print('Not yet implemented')
    else:
        parameters[temp_name] = float(temp_val)
    i = i+1
    
# Define the variables and initial values

print('\n\nStep 2 of 5: Set the initial values of the states. Type "done" \
if you want to go to the system equations.')

variables = {}

i = 1
while 1:
    temp_val = input('x' + str(i) + ': ')
    if temp_val == Break_Statement:
        break
    elif temp_name == Exit_Statement:
        print('Not yet implemented')
    else:
        variables['x'+ str(i)] = float(temp_val)
    i = i+1
    
# Define the system differential equtions

print('\n\nStep 3 of 5: Define the differential equations.')

equations = {}

for i in range(1,len(variables)+1):
    temp_val = input('dx' + str(i) + ': ')
    equations['dx'+ str(i)] = temp_val


# Define the algebraic conditions

print('\n\nStep 4 of 5: Define algebraic conditions. Type "done" \
if you want to go to define functions.')

algebraic = {}

i = 1
while 1:
    temp_val = input('g' + str(i) + ': ')
    if temp_val == Break_Statement:
        break
    elif temp_name == Exit_Statement:
        print('Not yet implemented')
    else:
        algebraic['x'+ str(i)] = temp_val
    i = i+1


# Define further functions

print('\n\nStep 5 of 5: Define algebraic conditions. Type "done" \
if you want to go to define functions.')

functions = {}

i = 1
while 1:
    temp_name = input('Name of the function: ')
    if temp_name == Break_Statement:
        break
    elif temp_name == Exit_Statement:
        print('Not yet implemented')
    else:
        temp_val = input('definition: ')
        
    if temp_val == Break_Statement:
        break
    elif temp_val == Exit_Statement:
        print('Not yet implemented')
    else:
        functions[temp_name] = temp_val
    i = i+1
    
# Create a directory with yout model's name 
try:
    os.makedirs('../' + title)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

#create file 
file = open('../' + title + '\model.py', 'w')

file.write(str('#') + ' This file contains the model ' + title + '\n')
file.write(str('#') + ' Reference: ' + reference + '\n\n')               
file.write('parameters = ' + str(parameters) + '\n\n')
file.write('variables = ' + str(variables)+ '\n\n')
file.write('equations = ' + str(equations)+ '\n\n')
file.write('algebraic = ' + str(algebraic)+ '\n\n')
file.write('functions = ' + str(functions))
file.close()

print('\nThe ' + title + ' model.py was succesfully generated.')