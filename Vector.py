class Vector:
    def __init__(self, array) -> None:
        self.vector = []

        # Fill the coordinates in the vector
        for coord in array: 
            self.vector.append(coord)

    
    # Print values of Vector object
    def print(self):
        for i in range(len(self.vector)):
            if i == 0:
                print('[', end='')
            if i == len(self.vector) - 1:
                print(str(self.vector[i]) + ']')
            else:
                print(self.vector[i], end=', ')
        print()


    # Return size of the vector
    def shape(self):
        if isinstance(self.vector[0], (float, int)):
            return len(self.vector)


    # Add a vector to the current vector
    def add(self, vector):
        for i in range(len(vector)):
            if len(self.vector) == len(vector):
                self.vector[i] += vector[i]
            else:
                print(
                    '\033[31mAdd error : Invalid size between two vectors\033[0m')
                return

    # Subtract a vector to the current vector
    def sub(self, vector):
        for i in range(len(vector)):
            if len(self.vector) == len(vector):
                self.vector[i] -= vector[i]
            else:
                print(
                    '\033[31mAdd error : Invalid size between two vectors\033[0m')
                return

    # Multiply a vector with a scalar
    def scl(self, scalar):
        for i in range(len(self.vector)):
            self.vector[i] *= scalar