import sys
sys.path.append('.')

from Matrix import Matrix

if __name__ == '__main__':

    m0 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    print(m0.projection(1, 2, 3, 4), end='')

