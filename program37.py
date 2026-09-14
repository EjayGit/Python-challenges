# Add 2 matrices.

# Input matrices
matrix1 = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
matrix2 = [
 [9, 8, 7],
 [6, 5, 4],
 [3, 2, 1]
]


def addMatrices(mat1, mat2):
    # Check size of matrices are equal.
    if len(mat1) != len(mat2) and len(mat1[0]) != len(mat2[0]):
        return 'Matrices must be the same size'

    matrix = []
    for y in range(0, len(mat1)):
        row = []
        for x in range (0, len(mat1[0])):
            row.append(mat1[y][x] + mat2[y][x])
        matrix.append(row)
    return matrix

print(addMatrices(matrix1, matrix2))