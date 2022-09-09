import sys
sys.path.append('.')

from Vector import Vector
from Matrix import Matrix

if __name__ == '__main__':
	v1 = Vector([5, 6, 7])
	v2 = Vector([2, 3, 4])
	v3 = Vector([-2, 4, -6])
	v4 = Vector([0, 1, 0])
	v5 = Vector([-10, 5, 50])
	v6 = Vector([complex(1, 2), complex(2, 3), complex(4, 1)])

	m1 = Matrix([[1, 1, 1], [2, 0, 0], [0, 0, -3]])
	m2 = Matrix([[1, -1, 1], [2, 0, 10], [0, 5, -3]])
	m3 = Matrix([[-1, 1, -1], [2, 5, -0], [0, 1, 3]])
	m4 = Matrix([[10, 100, 1000], [-1, -2, -3], [1, -2, 5]])
	m5 = Matrix([[1, 2], [2, 0], [1, 0]])
	m6 = Matrix([[1, 2, 3], [2, 0, -5]])
	m7 = Matrix([[complex(1, 1), complex(2, 2), complex(5, -2)], [complex(3, 3), complex(4, 4), complex(-2, 1)]])

	# Matrix * Vector

	print('\n\033[7;49;32mMatrix * Vector\033[0m\n')
	print('Matrix: ')
	m1.print()
	print('Vector: ')
	v2.print()
	print('\033[32mResult :', m1.mul_vec(v2), '\033[0m\n')

	print('\n\033[7;49;32mMatrix * Vector\033[0m\n')
	print('Matrix: ')
	m4.print()
	print('Vector: ')
	v5.print()
	print('\033[32mResult :', m4.mul_vec(v5), '\033[0m\n')

	print('\n\033[7;49;32mMatrix * Vector\033[0m\n')
	print('Matrix: ')
	m3.print()
	print('Vector: ')
	v3.print()
	print('\033[32mResult :', m3.mul_vec(v3), '\033[0m\n')

	print('\n\033[7;49;32mMatrix * Vector\033[0m\n')
	print('Matrix: ')
	m3.print()
	print('Vector: ')
	v4.print()
	print('\033[32mResult :', m3.mul_vec(v4), '\033[0m\n')

	print('\n\033[7;49;32mMatrix * Vector\033[0m\n')
	print('Matrix: ')
	m3.print()
	print('Vector: ')
	v6.print()
	print('\033[32mResult :', m3.mul_vec(v6), '\033[0m\n')

	# Matrix * Matrix

	print('\n\033[7;49;36mMatrix * Matrix\033[0m\n')
	print('Matrix: ')
	m1.print()
	print('Matrix: ')
	m2.print()
	print('\033[36mResult :', m1.mul_mat(m2), '\033[0m\n')

	print('\n\033[7;49;36mMatrix * Matrix\033[0m\n')
	print('Matrix: ')
	m4.print()
	print('Matrix: ')
	m1.print()
	print('\033[36mResult :', m4.mul_mat(m1), '\033[0m\n')

	print('\n\033[7;49;36mMatrix * Matrix\033[0m\n')
	print('Matrix: ')
	m1.print()
	print('Matrix: ')
	m3.print()
	print('\033[36mResult :', m1.mul_mat(m3), '\033[0m\n')

	print('\n\033[7;49;36mMatrix * Matrix\033[0m\n')
	print('Matrix (left): ')
	m6.print()
	print('Matrix (right): ')
	m5.print()
	print('\033[36mResult :', m6.mul_mat(m5), '\033[0m\n')

	print('\n\033[7;49;36mMatrix * Matrix\033[0m\n')
	print('Matrix (left): ')
	m7.print()
	print('Matrix (right): ')
	m5.print()
	print('\033[36mResult :', m5.mul_mat(m7), '\033[0m\n')