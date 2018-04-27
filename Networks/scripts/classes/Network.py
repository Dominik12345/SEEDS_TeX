import numpy as np
class Network:
# Network provides a class to handle linear dynamic systems
# dx/dt = Ax + Bu + Dw , y = Cx

	def __init__(self):
		# initialize the Network dimension
		self.number_nodes = 0
		self.number_observables = 0
		self.number_errors = 0
		self.number_inputs = 0
		# initialize system matrices
		self.A = [] 
		self.B = []
		self.C = []
		self.D = []
		# states is a dictionary of state variable
		# names  and corresponding initial values
		self.nodes = {} 
		# dynamic equations is a dictionary of 
		# state variable names and the 
		# corresponding differential equation
		self.dynamic_equations = {}
		# observation function is a dictionary 
		# of observable names and corresponding 
		# mapping
		self.observables = {}
		self.observed_nodes = []
		# error_nodes is a list of variable names 
		# that are possibly erroreous
		self.error_nodes = []
		# algebraic_equations is a dictionary of 
		# equation names and algebraic statements 
		# e.g. {'g1', x1 + x2 - N}
		self.algebraic_equations = {}
		

	# ---> get and set
	def get_number_nodes(self):
		return(len(self.nodes))
	def get_number_observables(self):
		return(len(self.observed_nodes))
	def get_number_errors(self):
		return(len(self.error_nodes))

	def get_nodes(self):
		return(self.nodes)
	def add_node(self, name, initialvalue):
		if isinstance(initialvalue,int):
			initialvalue = float(initialvalue)
		if isinstance(name, str) and isinstance(initialvalue,float):
			self.nodes[name] = initialvalue
		else:
			print('add_node expects str and float')

	def get_observables(self):
		return(self.observables)
	def get_observed_nodes(self):
		return(self.observed_nodes)
	def add_observed_node(self, name):
		keys = list(self.nodes.keys())
		if name in keys:
			self.observed_nodes.append(name)
		else:
			print(name + ' does not exist')
	def add_observable(self, name, definition):
		if isinstance(name, str) and isinstance(definition,str):
			# keys = list names of the nodes
			keys = list(self.nodes.keys())
			definition = definition.replace(' ','')
			definition_temp = definition.replace('-','+')
			terms = definition_temp.split('+')
			bool_definition = True
			# check if the given definition is linear
			for i in terms:
				for j in keys:
					if j+'**' in i or j+'^' in i:
						bool_definition = False
					elif j in i:
						i_temp = i.replace(j,'')
						for k in keys:
							if k in i_temp:
								bool_definition = False	
			if bool_definition:
				self.observables[name] = definition
			else:
				print('invalid observable definition')

	def get_error_nodes(self):
		return(self.error_nodes)
	def add_error_node(self,name):
		keys = list(self.nodes.keys())
		if name in keys:
			self.error_nodes.append(name)
		else:
			print(name + ' does not exist')
	# <--- get and set

	# define differential equations --->
	def add_dynamic_equation(self, name, definition):
			keys = list(self.nodes.keys())
			if not (name in keys):
				bool_definition = False 
			definition = definition.replace(' ','')
			definition_temp = definition.replace('-','+')
			terms = definition_temp.split('+')
			bool_definition = True
			# check if the given definition is linear
			for i in terms:
				for j in keys:
					if j+'**' in i or j+'^' in i:
						bool_definition = False
					elif j in i:
						i_temp = i.replace(j,'')
						for k in keys:
							if k in i_temp:
								bool_definition = False	
			if bool_definition:
				
				self.dynamic_equations[name] = definition
			else:
				print('invalid definition')
	def get_dynamic_equations(self):
		return(self.dynamic_equations)

	
	# <--- define differential equations

	# system matrices --->
	def make_A(self, structural):
		A = np.zeros((self.get_number_nodes(),self.get_number_nodes()))
		A_structural = np.zeros((self.get_number_nodes(),self.get_number_nodes()))
		keys = list(self.nodes.keys())
		counter_row = 0
		for i in keys: # differential equation of node i
			temp_eq = self.dynamic_equations[i]
			counter_column = 0		
			for j in keys:
				if j in temp_eq:
					A_structural[counter_row,counter_column] = True
				else:
					A_structural[counter_row,counter_column] = False
				counter_column = counter_column + 1
			counter_row = counter_row + 1
		if structural:	
			return(A_structural)	
	
		for i in range(0,len(keys)):
			order_string = []
			order_keys = []
			temp_eq = self.dynamic_equations[keys[i]]
			temp_number = 0
			for j in range(0,len(keys)):
				if A_structural[i,j] == 1:
					order_string.append(temp_eq.find(keys[j]))
					order_keys.append(keys[j])
					temp_number = temp_number + 1
			order_keys = [x for _,x in sorted(zip(order_string,order_keys))]
			for j in range(0,len(order_keys)):
				temp_key = order_keys[j]
				temp = temp_eq.split(temp_key)
				if len(temp) == 2:
					temp_coeff,temp_eq = temp
				else:
					temp_coeff = temp
					temp_eq = temp
 			
				column = keys.index(temp_key)
				if temp_coeff == '-':
					temp_coeff = -1
				elif temp_coeff == '+':
					temp_coeff = 1
				elif (temp_coeff[-1] == '*' or temp_coeff[-1]=='+' or 
				temp_coeff[-1]=='-'):
					temp_coeff = temp_coeff[:-1]
				if temp_coeff == '':
					temp_coeff = 1
				A[i,column] = temp_coeff
				order_string.remove(np.min(order_string))
		self.A = A
		return(A)
		
	def make_C(self):
		C = np.zeros((self.get_number_observables(),self.get_number_nodes()))
		keys = list(self.nodes.keys())
		for i in range(0,len(self.observed_nodes)):
			#row = self.observed_nodes[i]
			column = keys.index(self.observed_nodes[i])
			C[i,column] = True
		self.C = C
		return(C)
		
	def make_D(self):
		D = np.zeros((self.get_number_nodes(),self.get_number_errors()))
		keys = list(self.nodes.keys())
		for i in range(0,len(self.error_nodes)):
			row = keys.index(self.error_nodes[i])
			D[row,i] = True
		self.D = D
		return(D)
	
	# <--- system matrices


	# methods --->
	def index(self,node):
		return(list(self.nodes.keys()).index(node))

	def parents(self,node):
		A = self.make_A(True)
		index = self.index(node)
		keys = list(self.nodes.keys())
		parents = []
		for i in range(0,len(A[index])):
			if A[index,i] == 1 and not (i == index):
				parents.append(keys[i])
		return(parents)

	def children(self,node):
		A = np.transpose(self.make_A(True))
		index = self.index(node)
		keys = list(self.nodes.keys())
		childen = []
		for i in range(0,len(A[index])):
			if A[index,i] == 1 and not (i == index):
				childen.append(keys[i])
		return(childen)

	# <--- methods	
