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
        self.matrix = []

        # Matrix filling
        # Case for one column
        if isinstance(array[0], (int, float)):
            for row in array:
                self.matrix.append([row])
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
            self.matrix.append(row)


    # Print values of Matrix object
    def print(self, new_line=True):
        for row in self.matrix:
            print(row)
        if new_line:
            print()


    # Returns an array with shape [rows, columns]
    def shape(self):
        return [len(self.matrix), len(self.matrix[0])]


    # Returns an array version of the Matrix
    def to_array(self):
        array = []
        for col in self.matrix:
            row = []
            for val in col:
                row.append(val)
            array.append(row)
        return array


    # Returns a boolean if the Matrix is a square
    def is_square(self):
        if len(self.matrix[0]) == len(self.matrix):
            return True
        return False


    # Add a matrix to the current matrix
    def add(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                len_row_source = len(self.matrix[i])
                len_row_target = len(matrix[i])
                if len_row_source == len_row_target:
                    self.matrix[i][j] += matrix[i][j]
                else:
                    print(
                        '\033[31mAdd error : Invalid size between two matrices\033[0m')
                    return


    # Subtract a matrix to the current matrix
    def sub(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(self.matrix[i]) == len(matrix[i]):
                    self.matrix[i][j] -= matrix[i][j]
                else:
                    print(
                        '\033[31mAdd error : Invalid size between two matrices\033[0m')
                    return


    # Multiply a matrix with a scalar
    def scl(self, scalar):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] *= scalar