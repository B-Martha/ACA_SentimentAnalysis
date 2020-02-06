n = 3
mat = [[0 for x in range(n)] for x in range(n)]
inv_mat = [[0 for x in range(n)] for x in range(n)]


def display_matrix(matrix):
    for x in range(len(matrix)):
        print(*matrix[x])


def input_matrix(matrix):
    for x in range(3):
        matrix[x] = [int(x) for x in input().split()]


def cofactor(matrix, i, j):
    temp = [[0 for p in range(len(matrix) - 1)] for p in range(len(matrix) - 1)]
    x = y = row = col = 0
    while row < len(matrix):
        while col < len(matrix):
            if row != i and col != j:
                temp[x][y] = matrix[row][col]
                y += 1
                if y == n - 1:
                    y = 0
                    x += 1
            col += 1
        row += 1
        col = 0
    return temp


def determinant(matrix):
    det = 0
    sign = 1
    if len(matrix) == 1:
        return matrix[0][0]
    for t in range(len(matrix)):
        det += sign * matrix[0][t] * determinant(cofactor(matrix, 0, t))
        sign *= -1
    return det


def adjoint(matrix):
    temp = [[0 for x in range(len(matrix))] for x in range(len(matrix))]
    sign = 1
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            temp[y][x] = sign * determinant(cofactor(matrix, x, y))
            sign *= -1
    return temp


def scalar_multiply(matrix, scalar):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            matrix[x][y] *= scalar
    return matrix


print("Enter the matrix below:")
input_matrix(mat)
if determinant(mat) == 0:
    print("The matrix is not invertible")
else:
    print("The inverse of this matrix is:")
    inv_mat = scalar_multiply(adjoint(mat), (1/determinant(mat)))
    display_matrix(inv_mat)
