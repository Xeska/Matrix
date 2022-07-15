class Vector:
	def __init__(self, array) -> None:
		self.array = []

		# Fill the coordinates in the vector
		for coord in array: 
			self.array.append(coord)

	
	# Print values of Vector object
	def print(self):
		for i in range(len(self.array)):
			if i == 0:
				print('[', end='')
			if i == len(self.array) - 1:
				print(str(self.array[i]) + ']')
			else:
				print(self.array[i], end=', ')
		print()


	# Returns an array with shape
	def shape(self):
		if isinstance(self.array[0], (float, int)):
			return [len(self.array), 1]


	# Returns a same sized array filled with 0
	def zeros(self):
		shape = self.shape()
		zeros = []
		for i in range(shape[0]):
			row = []
			for j in range(shape[1]):
				row.append(0)
			zeros.append(row)
		return zeros

	# Add a vector to the current vector
	def add(self, vector):
		for i in range(len(vector)):
			if len(self.array) == len(vector):
				self.array[i] += vector[i]
			else:
				print(
					'\033[31mAdd error : Invalid size between two vectors\033[0m')
				return

	# Subtract a vector to the current vector
	def sub(self, vector):
		for i in range(len(vector)):
			if len(self.array) == len(vector):
				self.array[i] -= vector[i]
			else:
				print(
					'\033[31mAdd error : Invalid size between two vectors\033[0m')
				return

	# Multiply a vector with a scalar
	def scl(self, scalar):
		for i in range(len(self.array)):
			self.array[i] *= scalar

	# Dot product
	def dot(self, vector):
		if isinstance(vector, Vector):
			if (vector.shape()[0] == self.shape()[0]):
				product = 0
				for i in range(len(self.array)):
					product += self.array[i] * vector.array[i]
				return product
			print('The Vector used as a parameter must have the same length')
		print('The parameter has to be a vector')
		return

	# Manhattan norm
	def norm_1(self):
		norm = 0
		for value in self.array:
			norm += abs(value)
		return norm

	# Euclidian norm
	def norm(self):
		norm = 0
		for value in self.array:
			norm += value ** 2
		return norm ** (1/2)

	# Supremum norm
	def norm_inf(self):
		return max(map(abs, self.array))
