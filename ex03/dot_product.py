import sys
sys.path.append('.')

from Vector import Vector

# Did this before noticing you have to make a function in the Vector class
# def dot_product(v1, v2):
# 	if isinstance(v1, Vector) and isinstance(v2, Vector):
# 		if v1.shape()[0] != v2.shape()[0]:
# 			print('The two Vectors must have the same length')
# 			sys.exit(1)
# 		product = 0
# 		for i in range(len(v1.array)):
# 			product += v1.array[i] * v2.array[i]
# 		# Result printing
# 		print('Vector 1 : ')
# 		v1.print()
# 		print('Vector 2: ')
# 		v2.print()
# 		print('\033[32mDot product: ' + str(product) + '\033[0m\n')
# 	else:
# 		print('Dot product has to be executed between two Vectors...')
# 		sys.exit(1)

if __name__ == '__main__':
	v1 = Vector([1, 2, 3])
	v2 = Vector([0, 0, 0])
	v3 = Vector([-1, -2, -3])
	v4 = Vector([10, 0, 5])

	print('Vector 1: ')
	v1.print()
	print('Vector 2: ')
	v1.print()
	print('\033[32mProduct: ', v1.dot(v1), '\033[0m\n')

	print('Vector 1: ')
	v1.print()
	print('Vector 2: ')
	v2.print()
	print('\033[32mProduct: ', v2.dot(v1), '\033[0m\n')

	print('Vector 1: ')
	v1.print()
	print('Vector 2: ')
	v3.print()
	print('\033[32mProduct: ', v3.dot(v1), '\033[0m\n')

	print('Vector 1: ')
	v1.print()
	print('Vector 2: ')
	v4.print()
	print('\033[32mProduct: ', v4.dot(v1), '\033[0m\n')

	# dot_product(Vector([1, 2, 3]), Vector([1, 2, 3]))
	# dot_product(Vector([0, 0, 0]), Vector([1, 2, 3]))
	# dot_product(Vector([-1, -2, -3]), Vector([1, 2, 3]))
	# dot_product(Vector([10, 0, 5]), Vector([1, 2, 3]))
