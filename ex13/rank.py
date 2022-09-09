import sys
sys.path.append('.')

from Matrix import Matrix

if __name__ == '__main__':

    m0 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    m1 = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    m2 = Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1]])
    m3 = Matrix([[-1, 1, -1], [2, 5, -0]])
    m4 = Matrix([[10, 100], [-2, -3], [-2, 5]])
    m5 = Matrix([[1, 2], [3, 4]])
    m6 = Matrix([[1, 2], [2, 4]])
    m7 = Matrix([[8, 5, -2, 4], [4, 2.5, 20, 4], [8, 5, 1, 4], [28, -4, 17, 1]])
    m8 = Matrix([[complex(1, 1), complex(2, 2), complex(5, -2)], [complex(3, 3), complex(4, 4), complex(-2, 1)], [complex(1, 4), complex(5, 3), complex(1, 1)]])

    print('Matrix: ')
    m0.print()
    print('\033[32mRank :', m0.rank(), '\033[0m\n')

    print('Matrix: ')
    m1.print()
    print('\033[32mRank :', m1.rank(), '\033[0m\n')

    print('Matrix: ')
    m2.print()
    print('\033[32mRank :', m2.rank(), '\033[0m\n')

    print('Matrix: ')
    m3.print()
    print('\033[32mRank :', m3.rank(), '\033[0m\n')

    print('Matrix: ')
    m4.print()
    print('\033[32mRank :', m4.rank(), '\033[0m\n')

    print('Matrix: ')
    m5.print()
    print('\033[32mRank :', m5.rank(), '\033[0m\n')

    print('Matrix: ')
    m6.print()
    print('\033[32mRank :', m6.rank(), '\033[0m\n')

    print('Matrix: ')
    m7.print()
    print('\033[32mRank :', m7.rank(), '\033[0m\n')

    print('Complex')
    print('Matrix: ')
    m8.print()
    print('\033[32mRank :', m8.rank(), '\033[0m\n')