import sys
from typing import Type
sys.path.append('.')

from Vector import Vector

#					U.V
# cos(U, V) = _________________ (expressed in Rad)
#			  norm(U) * norm(V)

def angle_cos(v1, v2):
	if isinstance(v1, Vector) and isinstance(v2, Vector):
		if v1.norm() == 0 or v2.norm() == 0:
			print('One of the parameters cannot be nul Vector')
			sys.exit(1)
		res = v1.dot(v2) / (v1.norm() * v2.norm())
		if isinstance(res, complex):
			return complex(round(res.real, 3), round(res.imag, 3))
		return round(v1.dot(v2) / (v1.norm() * v2.norm()), 3)
	print('The parameters must be both Vectors')
	sys.exit(1)

if __name__ == '__main__':
	v1 = Vector([-1, -2, 3])
	v2 = Vector([2, 4, 6])
	v3 = Vector([-2, 4, -6])
	v4 = Vector([0, 1, 0])
	v5 = Vector([-10, 5, 50])
	v6 = Vector([complex(1, 2), complex(2, 3), complex(4, 1)])

	print('Vector 1: ')
	v1.print()
	print('Vector 2: ')
	v1.print()
	print('\033[32mCosine: ', angle_cos(v1, v1), '\033[0m\n')

	print('Vector 1: ')
	v1.print()
	print('Vector 2: ')
	v2.print()
	print('\033[32mCosine: ', angle_cos(v1, v2), '\033[0m\n')

	print('Vector 1: ')
	v1.print()
	print('Vector 2: ')
	v3.print()
	print('\033[32mCosine: ', angle_cos(v1, v3), '\033[0m\n')

	print('Vector 1: ')
	v1.print()
	print('Vector 2: ')
	v4.print()
	print('\033[32mCosine: ', angle_cos(v1, v4), '\033[0m\n')

	print('Vector 1: ')
	v1.print()
	print('Vector 2: ')
	v4.print()
	print('\033[32mCosine: ', angle_cos(v1, v4), '\033[0m\n')

	print('Vector 1: ')
	v1.print()
	print('Vector 2: ')
	v5.print()
	print('\033[32mCosine: ', angle_cos(v1, v5), '\033[0m\n')

	print('Complex')
	print('Vector 1: ')
	v1.print()
	print('Vector 2: ')
	v5.print()
	print('\033[32mCosine: ', angle_cos(v1, v6), '\033[0m\n')