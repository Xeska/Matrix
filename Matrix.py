import math
import sys
from unittest import result
from Vector import Vector


# Verify content provided in matrices
def is_valid(array):
	if len(array) < 1:
		print('\033[31mEmpty array.\033[0m')
		sys.exit(1)
	# Case for one single row
	if isinstance(array[0], (int, float)):
		for val in array:
			if not isinstance(val, (int, float)):
				print('\033[31mIncorrect value given (' +
					  str(val) + ').\033[0m')
				sys.exit(1)
		return 1
	elif not isinstance(array[0], list):
		print('\033[31mIncorrect type given.\033[0m')
		sys.exit(1)

	# Case for multiple rows
	for row in array:
		for val in row:
			if not isinstance(val, (int, float)):
				print('\033[31mIncorrect value given (' +
					  str(row) + ').\033[0m')
				sys.exit(1)


class Matrix():
	def __init__(self, array):
		is_valid(array)
		self.array = []

		# Matrix filling
		# Case for one column
		if isinstance(array[0], (int, float)):
			for row in array:
				self.array.append([row])
			return

		# Check if matrice given is valid
		length = len(array[0])
		for row in array:
			if length != len(row):
				print('\033[31mConstructor error : Invalid size input\033[0m')
				sys.exit(1)

		# Matrix filling
		# Case for multiple columns
		for i in range(len(array)):
			row = []
			for j in range(len(array[i])):
				row.append(array[i][j])
			self.array.append(row)

	# Print values of Matrix object

	def print(self, new_line=True):
		for row in self.array:
			for i in range(len(row)):
				row[i] = round(row[i], 4)
			print(row)
		if new_line:
			print()

	# Returns an array with shape [rows, columns]

	def shape(self):
		return [len(self.array), len(self.array[0])]

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

	# Returns a boolean if the Matrix is a square

	def is_square(self):
		if len(self.array[0]) == len(self.array):
			return True
		return False

	# Add a matrix to the current matrix

	def add(self, matrix):
		for i in range(len(matrix)):
			for j in range(len(matrix[i])):
				len_row_source = len(self.array[i])
				len_row_target = len(matrix[i])
				if len_row_source == len_row_target:
					self.array[i][j] += matrix[i][j]
				else:
					print(
						'\033[31mAdd error : Invalid size between two matrices\033[0m')
					return

	# Subtract a matrix to the current matrix

	def sub(self, matrix):
		for i in range(len(matrix)):
			for j in range(len(matrix[i])):
				if len(self.array[i]) == len(matrix[i]):
					self.array[i][j] -= matrix[i][j]
				else:
					print(
						'\033[31mAdd error : Invalid size between two matrices\033[0m')
					return

	# Multiply a matrix with a scalar

	def scl(self, scalar):
		for i in range(len(self.array)):
			for j in range(len(self.array[i])):
				self.array[i][j] *= scalar

	# Multiply a matrix with a vector

	def mul_vec(self, vector):
		if isinstance(vector, Vector):
			if vector.shape()[0] != self.shape()[1]:
				print(
					'The size of the Vector must be the same than the column number of the Matrix')
				return
			result = self.shape()[0] * [0]
			for i in range(vector.shape()[0]):
				for j in range(self.shape()[0]):
					result[i] += self.array[i][j] * vector.array[j]
			return result
		print('The parameter must be a Vector')
		return

	# Multiply a matrix with a matrix
	def mul_mat(self, matrix):
		if isinstance(matrix, Matrix):
			if self.shape()[1] != matrix.shape()[0]:
				print(
					'in A x B, the number of colums of A must be equal to the number of line of B')
				return
			result = [[0 for _ in range(self.shape()[0])]
					  for _ in range(matrix.shape()[1])]
			for i in range(self.shape()[0]):
				for j in range(self.shape()[0]):
					sum = 0
					for k in range(self.shape()[1]):
						sum += self.array[i][k] * matrix.array[k][j]
					result[i][j] = sum
			return result
		print('The parameter must be a Matrix')
		return

	# Trace
	def trace(self):
		if self.shape()[0] != self.shape()[1]:
			print('The Matrix is not square')
			return
		trace = 0
		for i in range(self.shape()[0]):
			trace += self.array[i][i]
		return trace

	# Transpose
	def transpose(self):
		result = []
		for i in range(self.shape()[1]):
			tmp = []
			for j in range(self.shape()[0]):
				tmp.append(self.array[j][i])
			result.append(tmp)
		return result

	# Row Echelon - Switch Lines
	def __switch_lines(self, i: int, j: int):
		# Li <-> Lj to A
		self.array[i], self.array[j] = self.array[j], self.array[i]

	# Row Echelon - Transvection
	def __transvection(self, i: int, j: int, mult: float):
		# Li <- Li + mult * Lj to A
		for k in range(self.shape()[1]):  # Columns
			self.array[i][k] = self.array[i][k] + mult * self.array[j][k]

	# Row Echelon - Pivot
	def __get_pivot(self, line: int, col: int, identity = []):
		pivot = self.array[line][col]
		# Will be used in case there is only 0 in the current column
		if pivot == 0:
			for following_line in range(line, self.shape()[0]):
				if self.array[following_line][col] != 0:
					self.__switch_lines(following_line, line)
					# Use the same action on the original identity Matrix to find inverse
					if isinstance(identity, Matrix) and len(identity.array) > 0:
						identity.array[line], identity.array[following_line] = identity.array[following_line], identity.array[line]
					return self.array[line][col], col
			if (col + 1 < self.shape()[1]):
				return self.__get_pivot(line, col + 1, identity)
			return 42, 0
		else:
			return pivot, col

	# Row Echelon - Result
	def row_echelon(self):
		nb_lines = self.shape()[0]
		nb_cols = self.shape()[1]
		for line in range(nb_lines):
			if line >= nb_cols:
				self.print()
				return self.array
			pivot, col = self.__get_pivot(line, line)
			for c in range(nb_cols):
				self.array[line][c] /= pivot
			if (line != 0):
				# Go back to reduce above lines
				for previous_line in range(line):
					self.__transvection(
						previous_line, line, -self.array[previous_line][col])
			for following_line in range(line + 1, nb_lines):
				self.__transvection(following_line, line, -
									self.array[following_line][col])
		# Go back to reduce above lines from the last one
		for previous_line in range(line):
			self.__transvection(previous_line, line, -
								self.array[previous_line][col])
		self.print()
		return self.array

	# Determinant of square matrix
	def determinant(self):
		if self.is_square() == False:
			print('Not a square Matrix, we cannot find its determinant')
		size = self.shape()[0]
		if (size == 1):
			return self.array[0][0]
		elif (size == 2):
			return self.array[0][0] * self.array[1][1] - self.array[0][1] * self.array[1][0]
		elif size == 3:
			a = self.array[0][0]
			b = self.array[0][1]
			c = self.array[0][2]
			d = self.array[1][0]
			e = self.array[1][1]
			f = self.array[1][2]
			g = self.array[2][0]
			h = self.array[2][1]
			i = self.array[2][2]
			return a * e * i + d * h * c + g * b * f - c * e * g - f * h * a - i * b * d
		elif size == 4:
			a = self.array[0][0]
			b = self.array[0][1]
			c = self.array[0][2]
			d = self.array[0][3]
			e = self.array[1][0]
			f = self.array[1][1]
			g = self.array[1][2]
			h = self.array[1][3]
			i = self.array[2][0]
			j = self.array[2][1]
			k = self.array[2][2]
			l = self.array[2][3]
			m = self.array[3][0]
			n = self.array[3][1]
			o = self.array[3][2]
			p = self.array[3][3]

			adjMatrix_1 = Matrix([[f, g, h], [j, k, l], [n, o, p]])
			adjMatrix_2 = Matrix([[e, g, h], [i, k, l], [m, o, p]])
			adjMatrix_3 = Matrix([[e, f, h], [i, j, l], [m, n, p]])
			adjMatrix_4 = Matrix([[e, f, g], [i, j, k], [m, n, o]])

			return a * adjMatrix_1.determinant() - b * adjMatrix_2.determinant() + c * adjMatrix_3.determinant() - d * adjMatrix_4.determinant()
		else:
			print('Awaited size is to be below 4 !')
			return
			
	# Inverse
	def inverse(self):
		if self.determinant() == 0:
			print('The determinant is 0, thus the Matrix has not inverse !')
			return
		if self.is_square() == False:
			print('The Matrix is not square :( ')
			return
		size = self.shape()[0]
		identity = Matrix([[0] * size] * size)
		for i in range(size):
			identity.array[i][i] = 1
		inverse = self.__row_echelon(identity)
		return inverse

	# Elementary row operation for inverse Matrix
	def __row_echelon(self, identity):
		nb_lines, nb_cols = self.shape()
		for line in range(nb_lines):
			if line >= nb_cols:
				self.print()
				return self.array
			pivot, col = self.__get_pivot(line, line, identity)
			for c in range(nb_cols):
				identity.array[line][c] /= pivot
				self.array[line][c] /= pivot
			if (line != 0):
				# Go back to reduce above lines
				# It is important to process 'identity' before 'self' to use original values
				for previous_line in range(line):
					identity.__transvection(
						previous_line, line, -self.array[previous_line][col])
					self.__transvection(
						previous_line, line, -self.array[previous_line][col])
			for following_line in range(line + 1, nb_lines):
				identity.__transvection(following_line, line, -
									self.array[following_line][col])
				self.__transvection(following_line, line, -
									self.array[following_line][col])
		# Go back to reduce above lines from the last one
		for previous_line in range(line):
			self.__transvection(previous_line, line, -
								self.array[previous_line][col])
			identity.__transvection(previous_line, line, -
								self.array[previous_line][col])
		identity.print()
		return identity.array

	# Rank
	def rank(self):
		rank = 0

		# Make a deep copy
		matrix = Matrix(self.array)

		matrix.row_echelon()
		nb_cols = matrix.shape()[1]
		for row in matrix.array:
			nb_zeros = 0
			for value in row: 
				if value == 0:
					nb_zeros += 1
			if nb_zeros != nb_cols:
				rank += 1
		return rank

	# Projection matrix for OpenGL
	def projection(self, fov, ratio, near, far):
		proj = Matrix([[0] * 4] * 4)

		f = 1 / math.tan(fov / 2)
		proj.array[0][0] = near / ratio
		proj.array[1][1] = near * near / f
		proj.array[2][2] = -(near + far) / (far - near)
		proj.array[2][3] = -2 * near * far / (far - near)
		proj.array[3][2] = -1

		result_string = ''

		for line in proj.array:
			length_line = len(line)
			for i in range(length_line):
				result_string += str(line[i])
				if (i < length_line - 1):
					result_string += ', '
				else:
					result_string += '\n'

		return result_string

	def __tan(self, angle):
		print('tanned')
