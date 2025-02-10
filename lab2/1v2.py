class Matrix:
    def __init__(self, a, b, c, d):
        self.data = [[a, b], [c, d]]

    def __add__(self, other):
        if isinstance(other, Matrix):
            return Matrix(
                self.data[0][0] + other.data[0][0],
                self.data[0][1] + other.data[0][1],
                self.data[1][0] + other.data[1][0],
                self.data[1][1] + other.data[1][1],
            )
        else:  # Assume it's a scalar
            return Matrix(
                self.data[0][0] + other,
                self.data[0][1] + other,
                self.data[1][0] + other,
                self.data[1][1] + other,
            )

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Matrix):
            return Matrix(
                self.data[0][0] - other.data[0][0],
                self.data[0][1] - other.data[0][1],
                self.data[1][0] - other.data[1][0],
                self.data[1][1] - other.data[1][1],
            )
        else:  # Assume it's a scalar
            return Matrix(
                self.data[0][0] - other,
                self.data[0][1] - other,
                self.data[1][0] - other,
                self.data[1][1] - other,
            )

    def __rsub__(self, other):
        return -self + other

    def __matmul__(self, other):
        if isinstance(other, Matrix):
            return Matrix(
                self.data[0][0] * other.data[0][0] + self.data[0][1] * other.data[1][0],
                self.data[0][0] * other.data[0][1] + self.data[0][1] * other.data[1][1],
                self.data[1][0] * other.data[0][0] + self.data[1][1] * other.data[1][0],
                self.data[1][0] * other.data[0][1] + self.data[1][1] * other.data[1][1],
            )
        else:
            raise ValueError("Can only multiply by another Matrix.")

    def __neg__(self):
        return Matrix(
            -self.data[0][0],
            -self.data[0][1],
            -self.data[1][0],
            -self.data[1][1],
        )

    def invert(self):
        det = self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        if det == 0:
            raise ValueError("Matrix is not invertible.")
        return Matrix(
            self.data[1][1] / det,
            -self.data[0][1] / det,
            -self.data[1][0] / det,
            self.data[0][0] / det,
        )

    def __str__(self):
        return f"[[{self.data[0][0]}, {self.data[0][1]}],\n [{self.data[1][0]}, {self.data[1][1]}]]"

    def __repr__(self):
        return self.__str__()

# Example usage:
if __name__ == "__main__":
    matrix_1 = Matrix(4., 5., 6., 7.)
    matrix_2 = Matrix(2., 2., 2., 1.)

    print("Matrix 1:")
    print(matrix_1)

    print("Matrix 2:")
    print(matrix_2)

    matrix_3 = matrix_2 @ matrix_1
    print("Matrix 2 @ Matrix 1:")
    print(matrix_3)

    matrix_4 = matrix_2 + matrix_1
    print("Matrix 2 + Matrix 1:")
    print(matrix_4)

    matrix_5 = 6 + matrix_1
    print("6 + Matrix 1:")
    print(matrix_5)

    matrix_6 = matrix_1 - matrix_2
    print("Matrix 1 - Matrix 2:")
    print(matrix_6)

    matrix_7 = matrix_1.invert()
    print("Inverse of Matrix 1:")
    print(matrix_7)