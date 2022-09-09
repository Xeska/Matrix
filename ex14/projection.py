import math
import sys
sys.path.append('.')

from Matrix import Matrix

if __name__ == '__main__':

    m0 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    # Field of view : PI / 2 <=> 90 deg
    # Ratio 1:1
    # Near : 1, Far : 10
    print(m0.projection(math.pi / 2, 1, 1, 10), end='')

