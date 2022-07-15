import sys
sys.path.append('.')

from Matrix import Matrix

if __name__ == '__main__':

	m1 = Matrix([[1, 1, 1], [2, 0, 0], [0, 0, -3]])
	m2 = Matrix([[1, -1, 1], [2, 0, 10], [0, 5, -3]])
	m3 = Matrix([[-1, 1, -1], [2, 5, -0], [0, 1, 3]])
	m4 = Matrix([[10, 100, 1000], [-1, -2, -3], [1, -2, 5]])
	m5 = Matrix([[1, 2], [2, 0], [1, 0]])

	print('Matrix: ')
	m1.print()
	print('\033[32mTranspose :', m1.transpose(), '\033[0m\n')

	print('Matrix: ')
	m2.print()
	print('\033[32mTranspose :', m2.transpose(), '\033[0m\n')

	print('Matrix: ')
	m3.print()
	print('\033[32mTranspose :', m3.transpose(), '\033[0m\n')

	print('Matrix: ')
	m4.print()
	print('\033[32mTranspose :', m4.transpose(), '\033[0m\n')

	print('Matrix: ')
	m5.print()
	print('\033[32mTranspose :', m5.transpose(), '\033[0m\n')