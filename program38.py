# Multiply 2 matrices together.

# Example matrices
matrix1 = [[1, 2, 3],
           [4, 5, 6]]
matrix2 = [[7, 8],
           [9, 10],
           [11, 12]]

def matMul(mat1, mat2):
    # Check the dimensions are correct
    if len(mat1) != len(mat2[0]) and len(mat1[0]) != len(mat2):
        return 'Matrices must be the correct dimensions.'
    matrix = []
    for y in range(0,len(mat1)):
        row = []
        for x in range(0, len(mat2[0])):
            col = []
            for z in range(0, len(mat1[0])):
                col.append(mat1[y][z] * mat2[z][x])
            row.append(sum(col))
        matrix.append(row)
    return matrix

print(matMul(matrix1, matrix2))
