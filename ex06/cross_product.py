import sys
sys.path.append('.')

from Vector import Vector

# c_x = a_y * b_z − a_z * b_y
# c_y = a_z * b_x − a_x * b_z
# c_z = a_x * b_y − a_y * b_x

def cross_product(v1, v2):
	if isinstance(v1, Vector) and isinstance(v2, Vector):
		if v1.shape()[0] != 3 or v2.shape()[0] != 3:
			print('The 2 Vectors must be 3-dimensional')
			sys.exit(1)
		result = [0, 0, 0]
		result[0] = v1.array[1] * v2.array[2] - v1.array[2] * v2.array[1]
		result[1] = v1.array[2] * v2.array[0] - v1.array[0] * v2.array[2]
		result[2] = v1.array[0] * v2.array[1] - v1.array[1] * v2.array[0]
		return result
	print('The parameters must be both Vectors')
	sys.exit(1)


if __name__ == '__main__':
	v1 = Vector([5, 6, 7])
	v2 = Vector([2, 3, 4])
	v3 = Vector([-2, 4, -6])
	v4 = Vector([0, 1, 0])
	v5 = Vector([-10, 5, 50])

	print('Vector 1: ')
	v1.print()
	print('Vector 2: ')
	v1.print()
	print('\033[32mCross Product: ', cross_product(v1, v1), '\033[0m\n')

	print('Vector 1: ')
	v1.print()
	print('Vector 2: ')
	v2.print()
	print('\033[32mCross Product: ', cross_product(v1, v2), '\033[0m\n')

	print('Vector 1: ')
	v1.print()
	print('Vector 2: ')
	v3.print()
	print('\033[32mCross Product: ', cross_product(v1, v3), '\033[0m\n')

	print('Vector 1: ')
	v1.print()
	print('Vector 2: ')
	v4.print()
	print('\033[32mCross Product: ', cross_product(v1, v4), '\033[0m\n')

	print('Vector 1: ')
	v1.print()
	print('Vector 2: ')
	v4.print()
	print('\033[32mCross Product: ', cross_product(v1, v4), '\033[0m\n')

	print('Vector 1: ')
	v1.print()
	print('Vector 2: ')
	v5.print()
	print('\033[32mCross Product: ', cross_product(v1, v5), '\033[0m\n')