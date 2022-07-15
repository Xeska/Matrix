import sys
sys.path.append('.')

from Vector import Vector

if __name__ == '__main__':
	v = Vector([0, 4, 3])
	print('Vector: ')
	v.print()
	print('\033[32mnorm 1: \t', v.norm_1())
	print('\033[33mnorm 2: \t', v.norm())
	print('\033[34mnorm inf:\t', v.norm_inf(), '\033[0m\n')

	v = Vector([0, 0, 0])
	print('Vector: ')
	v.print()
	print('\033[32mnorm 1: \t', v.norm_1())
	print('\033[33mnorm 2: \t', v.norm())
	print('\033[34mnorm inf:\t', v.norm_inf(), '\033[0m\n')

	v = Vector([1, 10, 100])
	print('Vector: ')
	v.print()
	print('\033[32mnorm 1: \t', v.norm_1())
	print('\033[33mnorm 2: \t', v.norm())
	print('\033[34mnorm inf:\t', v.norm_inf(), '\033[0m\n')

	v = Vector([-1, 0, -3])
	print('Vector: ')
	v.print()
	print('\033[32mnorm 1: \t', v.norm_1())
	print('\033[33mnorm 2: \t', v.norm())
	print('\033[34mnorm inf:\t', v.norm_inf(), '\033[0m\n')

	v = Vector([10, -20, 30])
	print('Vector: ')
	v.print()
	print('\033[32mnorm 1: \t', v.norm_1())
	print('\033[33mnorm 2: \t', v.norm())
	print('\033[34mnorm inf:\t', v.norm_inf(), '\033[0m\n')
	
