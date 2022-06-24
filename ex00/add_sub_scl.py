import sys
sys.path.append('.')

from Vector import Vector
from Matrix import Matrix

def testAddVector(v1: Vector, v2: Vector):
    print('Vector 1: ')
    v1.print()
    print('Vector 2: ')
    v2.print()
    v1.add(v2.array)
    print('Result: \033[32m')
    v1.print()
    print('\033[0m')

def testSubVector(v1: Vector, v2: Vector):
    print('Vector 1: ')
    v1.print()
    print('Vector 2: ')
    v2.print()
    v1.sub(v2.array)
    print('Result: \033[32m')
    v1.print()
    print('\033[0m')

def testSclVector(v: Vector, scalar: float):
    print('Vector: ')
    v.print()
    print('Scalar: ', scalar, end='\n\n')
    v.scl(scalar)
    print('Result: \033[32m')
    v.print()
    print('\033[0m')

def testAddMatrix(m1: Matrix, m2: Matrix):
    print('Matrix 1: ')
    m1.print()
    print('Matrix 2: ')
    m2.print()
    m1.add(m2.array)
    print('Result: \033[36m')
    m1.print()
    print('\033[0m')

def testSubMatrix(m1: Matrix, m2: Matrix):
    print('Matrix 1: ')
    m1.print()
    print('Matrix 2: ')
    m2.print()
    m1.sub(m2.array)
    print('Result: \033[36m')
    m1.print()
    print('\033[0m')

def testSclMatrix(m: Matrix, scalar: float):
    print('Matrix: ')
    m.print()
    print('Scalar: ', scalar, end='\n\n')
    m.scl(scalar)
    print('Result: \033[36m')
    m.print()
    print('\033[0m')

if __name__ == '__main__':
    print('\033[7;49;32mVector\033[0m\n')

    print('\033[32mAdd...\033[0m\n')
    testAddVector(Vector([1]), Vector([4]))
    testAddVector(Vector([-1, -2, -3]), Vector([-1, 0, 1]))
    testAddVector(Vector([1, 2, 3]), Vector([4, 5, 6]))

    print('\033[32mSub...\033[0m\n')
    testSubVector(Vector([1]), Vector([4]))
    testSubVector(Vector([-1, -2, -3]), Vector([-1, 0, 1]))
    testSubVector(Vector([1, 2, 3]), Vector([4, 5, 6]))

    print('\033[32mScale...\033[0m\n')
    testSclVector(Vector([1, 2, 3]), -2)
    testSclVector(Vector([1, 2, 3]), 0)
    testSclVector(Vector([1, 2, 3]), 10)
    testSclVector(Vector([1, 2, 3]), 1.5)

    print('\033[7;49;36mMatrix\033[0m\n')

    print('\033[36mAdd...\033[0m\n')
    testAddMatrix(Matrix([[1, 2]]), Matrix([[3, 4]]))
    testAddMatrix(Matrix([[1, 2], [3, 4]]), Matrix([[3, 4], [5, 6]]))
    testAddMatrix(Matrix([[1, 2, 11], [3, 4, 12], [5, 6, 13]]), Matrix([[3, 4, 14], [5, 6, 15], [7, 8, 16]]))
    
    print('\033[36mSub...\033[0m\n')
    testSubMatrix(Matrix([[1, 2]]), Matrix([[3, 4]]))
    testSubMatrix(Matrix([[1, 2], [3, 4]]), Matrix([[3, 4], [5, 6]]))
    testSubMatrix(Matrix([[1, 2, 11], [3, 4, 12], [5, 6, 13]]), Matrix([[3, 4, 14], [5, 6, 15], [7, 8, 16]]))

    print('\033[36mScale...\033[0m\n')
    testSclMatrix(Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), -2)
    testSclMatrix(Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 0)
    testSclMatrix(Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 10)
    testSclMatrix(Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 1.5)