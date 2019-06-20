from __future__ import print_function


def add(matrix_a, matrix_b):
    try:
        rows = [len(matrix_a), len(matrix_b)]
        cols = [len(matrix_a[0]), len(matrix_b[0])]
    except TypeError:
        raise TypeError("Cannot input an integer value, it must be a matrix")

    if rows[0] != rows[1] & cols[0] != cols[1]:
        raise ValueError(f"operands could not be broadcast together with shapes "
                         f"({rows[0],cols[0]}), ({rows[1], cols[1]})")

    matrix_c = []
    for i in range(rows[0]):
        list_1 = []
        for j in range(cols[0]):
            val = matrix_a[i][j] + matrix_b[i][j]
            list_1.append(val)
        matrix_c.append(list_1)
    return matrix_c


def subtract(matrix_a, matrix_b):
    try:
        rows = [len(matrix_a), len(matrix_b)]
        cols = [len(matrix_a[0]), len(matrix_b)]
    except TypeError:
        raise TypeError("Cannot input an integer value, it must be a matrix")

    if rows[0] != rows[1] & cols[0] != cols[1]:
        raise ValueError(f"operands could not be broadcast together with shapes "
                         f"({rows[0], cols[0]}), ({rows[1], cols[1]})")

    matrix_c = []
    for i in range(rows[0]):
        list_1 = []
        for j in range(cols[0]):
            val = matrix_a[i][j] - matrix_b[i][j]
            list_1.append(val)
        matrix_c.append(list_1)
    return matrix_c


def scalar_multiply(matrix, n):
    return [[x * n for x in row] for row in matrix]


def multiply(matrix_a, matrix_b):
    matrix_c = []
    num_rows_a = len(matrix_a)
    num_cols_a = len(matrix_a[0])
    num_rows_b = len(matrix_b)
    num_cols_b = len(matrix_b[0])
    
    if num_cols_a != num_rows_b:
        raise ValueError(f'Cannot multiply matrix of dimensions ({num_rows_a},{num_cols_a}) '
                         f'and ({num_rows_b},{num_cols_b})')
                      
    for i in range(num_rows_a):
        list_1 = []
        for j in range(num_cols_b):
            val = 0
            for k in range(num_cols_b):
                val = val + matrix_a[i][k] * matrix_b[k][j]
            list_1.append(val)
        matrix_c.append(list_1)
    return matrix_c


def identity(n):
    return [[int(row == column) for column in range(n)] for row in range(n)] 


def transpose(matrix):
    return map(list, zip(*matrix))


def minor(matrix, row, column):
    minor = matrix[:row] + matrix[row + 1:]
    minor = [row[:column] + row[column + 1:] for row in minor]
    return minor


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    
    res = 0
    for x in range(len(matrix)):
        res += matrix[0][x] * determinant(minor(matrix, 0, x)) * (-1) ** x
    return res


def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        return None

    matrix_minor = [[] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix_minor[i].append(determinant(minor(matrix, i, j)))
    
    cofactors = [[x * (-1) ** (row + col) for col, x in enumerate(matrix_minor[row])] for row in range(len(matrix))]
    adjugate = transpose(cofactors)
    return scalar_multiply(adjugate, 1/det)


if __name__ == '__main__':
    mat_a = [[12, 10], [3, 9]]
    mat_b = [[3, 4], [7, 4]]
    mat_c = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34], [41, 42, 43, 44]]
    mat_d = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
    print('Add Operation, %s + %s = %s \n' %(mat_a, mat_b, (add(mat_a, mat_b))))
    print('Multiply Operation, %s * %s = %s \n' %(mat_a, mat_b, multiply(mat_a, mat_b)))
    print('Identity:  %s \n' %identity(5))
    print('Minor of %s = %s \n' %(mat_c, minor(mat_c , 1 , 2)))
    print('Determinant of %s = %s \n' %(mat_b, determinant(mat_b)))
    print('Inverse of %s = %s\n'%(mat_d, inverse(mat_d)))
