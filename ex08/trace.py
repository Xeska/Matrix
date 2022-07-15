import sys
sys.path.append('.')

from Matrix import Matrix

if __name__ == '__main__':
	m1 = Matrix([[1, 1, 1], [2, 0, 0], [0, 0, -3]])
	m2 = Matrix([[1, -1, 1], [2, 0, 10], [0, 5, -3]])
	m3 = Matrix([[-1, 1, -1], [2, 5, -0], [0, 1, 3]])
	m4 = Matrix([[10, 100, 1000], [-1, -2, -3], [1, -2, 5]])

	print('Matrix: ')
	m1.print()
	print('\033[32mTrace :', m1.trace(), '\033[0m\n')

	print('Matrix: ')
	m2.print()
	print('\033[32mTrace :', m2.trace(), '\033[0m\n')

	print('Matrix: ')
	m3.print()
	print('\033[32mTrace :', m3.trace(), '\033[0m\n')

	print('Matrix: ')
	m4.print()
	print('\033[32mTrace :', m4.trace(), '\033[0m\n')