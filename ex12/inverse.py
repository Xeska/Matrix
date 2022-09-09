import sys
sys.path.append('.')

from Matrix import Matrix

if __name__ == '__main__':

    m0 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    m1 = Matrix([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
    m2 = Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1]])
    m3 = Matrix([[-1, 1, -1], [2, 5, -0], [0, 1, 3]])
    m4 = Matrix([[10, 100, 1000], [-1, -2, -3], [1, -2, 5]])
    m5 = Matrix([[1, 2], [3, 4]])
    m6 = Matrix([[1, 2], [2, 4]])
    m7 = Matrix([[8, 5, -2, 4], [4, 2.5, 20, 4], [8, 5, 1, 4], [28, -4, 17, 1]])
    m8 = Matrix([[complex(1, 1), complex(2, 2), complex(5, -2)], [complex(3, 3), complex(4, 4), complex(-2, 1)], [complex(1, 4), complex(5, 3), complex(1, 1)]])

    print('Matrix: ')
    m0.print()
    print('Result:')
    print('\033[32mInverse :', m0.inverse(), '\033[0m\n')

    print('Matrix: ')
    m1.print()
    print('Result:')
    print('\033[32mInverse :', m1.inverse(), '\033[0m\n')

    print('Matrix: ')
    m2.print()
    print('Result:')
    print('\033[32mInverse :', m2.inverse(), '\033[0m\n')

    print('Matrix: ')
    m3.print()
    print('Result:')
    print('\033[32mInverse :', m3.inverse(), '\033[0m\n')

    print('Matrix: ')
    m4.print()
    print('Result:')
    print('\033[32mInverse :', m4.inverse(), '\033[0m\n')

    print('Matrix: ')
    m5.print()
    print('Result:')
    print('\033[32mInverse :', m5.inverse(), '\033[0m\n')

    print('Matrix: ')
    m6.print()
    print('Result:')
    print('\033[32mInverse :', m6.inverse(), '\033[0m\n')

    print('Matrix: ')
    m7.print()
    print('Result:')
    print('\033[32mInverse :', m7.inverse(), '\033[0m\n')

    print('Complex')
    print('Matrix: ')
    m8.print()
    print('Result:')
    print('\033[32mInverse :', m8.inverse(), '\033[0m\n')