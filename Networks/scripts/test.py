import classes.Network as Net

import classes.Path as Path

#############################

N = Net.Network()


for i in range(1,10):
	N.add_node('x'+str(i),0)

N.add_error_node('x1')
N.add_error_node('x2')
N.add_observed_node('x6')
N.add_observed_node('x7')

N.add_dynamic_equation('x1', '-x1 + 0.5 * x9 ')
for i in range(2,10):
	N.add_dynamic_equation('x'+str(i), '-x'+str(i)+ ' + 0.5 * x' + str(i-1))

#############################


print(N.children('x2'))
print(N.parents('x2'))




#############################

P = Path.Path('x1')
P.append_node('x2')


print(P.get_sequence())
print(P.children('x1'))
print(P.parents('x2'))
print(P.len())
