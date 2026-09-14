# Transpose a matrix.

# Input matrix
matrix = [
 [1, 2, 3],
 [4, 5, 6]
]

def transposeMatrix(mat):
    # Check dimensions of matrix
    rows = len(mat)
    cols = len(mat[0])

    tMatrix = []
    for x in range(0, len(mat[0])):
        row = []
        for y in range(0, len(mat)):
            row.append(mat[y][x])
        tMatrix.append(row)
    return tMatrix

print(transposeMatrix(matrix))