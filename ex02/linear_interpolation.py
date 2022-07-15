from Matrix import Matrix
from Vector import Vector
import sys
sys.path.append('.')


def linear_interpolation(o1, o2, coef):
    if not isinstance(coef, (int, float)):
        print(
            '\033[31mInput error : The coefficient must be a number\033[0m')
        return

    if isinstance(o1, (int, float)) and isinstance(o2, (int, float)):
        print(o1, ' [ ', coef, ' ] ', o2)
        print('Result: ', o1 + (o2 - o1) * coef, end='\n\n')
    elif isinstance(o1, (Vector, Matrix)) and isinstance(o2, (Vector, Matrix)):
        result = Matrix(o2.array)
        result.sub(Matrix(o1.array).array)
        result.scl(coef)
        result.add(Matrix(o1.array).array)
        print('Coef: ', coef)
        print('Object 1: ')
        o1.print()
        print('Object 2: ')
        o2.print()
        print('Result: \033[32m')
        result.print()
        print('\033[0m')


if __name__ == '__main__':

    print('\033[7;49;32mNumber \033[0m\n')
    linear_interpolation(1, 5, 0.25)
    linear_interpolation(-1, 9, 0.5)
    linear_interpolation(1, 11, 0.75)
    linear_interpolation(1, 11, 1)

    print('\n\033[7;49;32mVector \033[0m\n')
    linear_interpolation(Vector([1, 2, 3]), Vector([2, 5, 5]), 0)
    linear_interpolation(Vector([1, 2, 3]), Vector([2, 5, 5]), 1)
    linear_interpolation(Vector([1, 2, 3]), Vector([2, 5, 5]), 0.5)

    print('\033[7;49;32mMatrix \033[0m\n')
    linear_interpolation(Matrix([[1, 2, 3], [1, 4, 3], [1, 2, 6]]), Matrix(
        [[1, 2, 3], [2, 5, 5], [10, 4, 10]]), 0)
    linear_interpolation(Matrix([[1, 2, 3], [1, 4, 3], [1, 2, 6]]), Matrix(
        [[1, 2, 3], [2, 5, 5], [10, 4, 10]]), 0.5)
    linear_interpolation(Matrix([[1, 2, 3], [1, 4, 3], [1, 2, 6]]), Matrix(
        [[1, 2, 3], [2, 5, 5], [10, 4, 10]]), 1)
    linear_interpolation(Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]]), Matrix(
        [[11, 11, 11], [101, 101, 101], [4, 5, 6]]), 0.4)
