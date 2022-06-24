import sys


# Verify content provided in matrices
def is_valid(array):
    if len(array) < 1:
        print('\033[31mEmpty array.\033[0m')
        sys.exit(1)
    # Case for one single row
    if isinstance(array[0], (int, float)):
        for val in array:
            if not isinstance(val, (int, float)):
                print('\033[31mIncorrect value given (' +
                      str(val) + ').\033[0m')
                sys.exit(1)
        return 1
    elif not isinstance(array[0], list):
        print('\033[31mIncorrect type given.\033[0m')
        sys.exit(1)

    # Case for multiple rows
    for row in array:
        for val in row:
            if not isinstance(val, (int, float)):
                print('\033[31mIncorrect value given (' +
                      str(row) + ').\033[0m')
                sys.exit(1)


class Matrix():
    def __init__(self, array):
        is_valid(array)
        self.array = []

        # Matrix filling
        # Case for one column
        if isinstance(array[0], (int, float)):
            for row in array:
                self.array.append([row])
            return

        # Check if matrice given is valid
        length = len(array[0])
        for row in array:
            if length != len(row):
                print('\033[31mConstructor error : Invalid size input\033[0m')
                sys.exit(1)

        # Matrix filling
        # Case for multiple columns
        for i in range(len(array)):
            row = []
            for j in range(len(array[i])):
                row.append(array[i][j])
            self.array.append(row)


    # Print values of Matrix object
    def print(self, new_line=True):
        for row in self.array:
            print(row)
        if new_line:
            print()


    # Returns an array with shape [rows, columns]
    def shape(self):
        return [len(self.array), len(self.array[0])]


    # Returns a same sized array filled with 0
    def zeros(self):
        shape = self.shape()
        zeros = []
        for i in range(shape[0]):
            row = []
            for j in range(shape[1]):
                row.append(0)
            zeros.append(row)
        return zeros


    # Returns a boolean if the Matrix is a square
    def is_square(self):
        if len(self.array[0]) == len(self.array):
            return True
        return False


    # Add a matrix to the current matrix
    def add(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                len_row_source = len(self.array[i])
                len_row_target = len(matrix[i])
                if len_row_source == len_row_target:
                    self.array[i][j] += matrix[i][j]
                else:
                    print(
                        '\033[31mAdd error : Invalid size between two matrices\033[0m')
                    return


    # Subtract a matrix to the current matrix
    def sub(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(self.array[i]) == len(matrix[i]):
                    self.array[i][j] -= matrix[i][j]
                else:
                    print(
                        '\033[31mAdd error : Invalid size between two matrices\033[0m')
                    return


    # Multiply a matrix with a scalar
    def scl(self, scalar):
        for i in range(len(self.array)):
            for j in range(len(self.array[i])):
                self.array[i][j] *= scalar

    