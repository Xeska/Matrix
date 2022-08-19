import sys
sys.path.append('.')

from Matrix import Matrix

if __name__ == '__main__':

    m0 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    m1 = Matrix([[1, 1, 1], [2, 0, 0], [0, 0, -3]])
    m2 = Matrix([[1, -1, 1], [2, 0, 10], [0, 5, -3]])
    m3 = Matrix([[-1, 1, -1], [2, 5, -0], [0, 1, 3]])
    m4 = Matrix([[10, 100, 1000], [-1, -2, -3], [1, -2, 5]])
    m5 = Matrix([[1, 2], [3, 4]])
    m6 = Matrix([[1, 2], [2, 4]])
    m7 = Matrix([[8, 5, -2, 4], [4, 2.5, 20, 4],
                [8, 5, 1, 4], [28, -4, 17, 1]])

    print('Matrix: ')
    m1.print()
    print('Result:')
    print('\033[32mDeterminant :', m1.determinant(), '\033[0m\n')

    print('Matrix: ')
    m2.print()
    print('Result:')
    print('\033[32mDeterminant :', m2.determinant(), '\033[0m\n')

    print('Matrix: ')
    m3.print()
    print('Result:')
    print('\033[32mDeterminant :', m3.determinant(), '\033[0m\n')

    print('Matrix: ')
    m4.print()
    print('Result:')
    print('\033[32mDeterminant :', m4.determinant(), '\033[0m\n')

    print('Matrix: ')
    m5.print()
    print('Result:')
    print('\033[32mDeterminant :', m5.determinant(), '\033[0m\n')

    print('Matrix: ')
    m6.print()
    print('Result:')
    print('\033[32mDeterminant :', m6.determinant(), '\033[0m\n')

    print('Matrix: ')
    m7.print()
    print('Result:')
    print('\033[32mDeterminant :', m7.determinant(), '\033[0m\n')
