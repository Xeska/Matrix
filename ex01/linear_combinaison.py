import sys
sys.path.append('.')

from Vector import Vector
from Matrix import Matrix

def linear_combinaison(matrixes, scalars):
    len_matrixes = len(matrixes)
    len_scalars = len(scalars)

    result_matrix = Matrix(matrixes[0].zeros())

    if len_matrixes != len_scalars:
        print(
            '\033[31mInput error : Vectors/Matrixes number different from scalars number\033[0m')
        return

    for i in range(len_scalars):
        print('Scalar: ', scalars[i])
        matrixes[i].print()
        matrixes[i].scl(scalars[i])
        # Need to recast things as Matrix to cover case with Vectors (cannot loop on int)
        result_matrix.add(Matrix(matrixes[i].array).array)
    print('Result: \033[32m')
    result_matrix.print()
    print('\033[0m')

if __name__ == '__main__':
    print('\033[7;49;32mVector\033[0m\n')
    linear_combinaison([Vector([1]), Vector([5]), Vector([10])], [1, 2, 3])
    linear_combinaison([Vector([1, 2]), Vector([5, 10]), Vector([10, 10])], [1, 2, -1])
    linear_combinaison([Vector([1, 2, 3]), Vector([5, 10, 15]), Vector([10, 10, 10])], [0, 0, 0])

    print('\033[7;49;32mMatrix\033[0m\n')
    linear_combinaison([Matrix([1, 2]), Matrix([5, 10]), Matrix([10, 10])], [1, 2, -1])
    linear_combinaison([Matrix([[1, 2], [1, 2]]), Matrix([[5, 10], [15, 20]]), Matrix([[10, 10], [1, 1]])], [1, 2, -1])
    linear_combinaison([Matrix([[1, 2, 3], [1, 4, 3], [1, 2, 6]]), Matrix([[1, -1, 3], [0, 2, 0], [10, 2, 3]]), Matrix([[1, 2, 13], [1, 2, 3], [13, 2, 3]])], [1, 0, 3])

