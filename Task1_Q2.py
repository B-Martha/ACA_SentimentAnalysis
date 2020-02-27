N = 3  #Here N is no. of rows in the matrix

mat = [[0 for x in range(N)] for x in range(N)]
inv_mat = [[0 for x in range(N)] for x in range(N)]


def display_matrix(matrix):
    #Displays matrix in a simple manner.
    for x in range(len(matrix)):
        print(*matrix[x], sep = '\t')


def input_matrix(matrix):
    #Inputs the matrix
    for x in range(3):
        matrix[x] = [int(x) for x in input().split()]


def scalar_multiply(matrix, scalar):
    # Multiplies entire matrix by a scalar
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            matrix[x][y] *= scalar
    return matrix


def cofactor(matrix, i, j):
    # Returns cofactor of the matrix
    temp = [[0 for p in range(len(matrix) - 1)] for p in range(len(matrix) - 1)]
    x = y = row = col = 0
    while row < len(matrix):
        while col < len(matrix):
            if row != i and col != j:   #remove ith row and jth col
                temp[x][y] = matrix[row][col]
                y += 1
                if y == N - 1:
                    y = 0
                    x += 1
            col += 1
        row += 1
        col = 0
    return scalar_multiply(temp, ((-1)**(i+j)))


def determinant(matrix):
    # Returns determinant of general n*n matrix recursively
    det = 0
    sign = 1
    if len(matrix) == 1:
        return matrix[0][0]
    for t in range(len(matrix)):
        det += sign * matrix[0][t] * determinant(cofactor(matrix, 0, t))
    return det


def adjoint(matrix):
    # Returns adjoint of the matrix
    temp = [[0 for x in range(len(matrix))] for x in range(len(matrix))]
    sign = 1
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            temp[y][x] = sign * determinant(cofactor(matrix, x, y))
    return temp


print("Enter the matrix below:")
input_matrix(mat)
if determinant(mat) == 0:
    print("The matrix is not invertible")
else:
    print("This matrix is invertible")
    print("The inverse of this matrix is:")
    inv_mat = scalar_multiply(adjoint(mat), (1/determinant(mat)))
    display_matrix(inv_mat)
