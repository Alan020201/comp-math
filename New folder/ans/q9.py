def matrixDiagonal(A):
    row_A = len(A)
    col_A = len(A[0])
    if row_A != col_A:
        return False 
    for i in range(row_A):
        for j in range(col_A):
            if i != j and A[i][j] != 0:
                return False        
    return True
matrix_A = [[1, 0, 0], [0, 4, 0], [0, 0, 7]]
matrix_B = [[1, 2, 4], [3, 6, 8], [9, 5, 2]]
if matrixDiagonal(matrix_A):
    print("1st Matrix is diagonal matrix.")
else:
    print("1st Matrix is not diagonal matrix.")
if matrixDiagonal(matrix_B):
    print("2nd Matrix is diagonal matrix.")
else:
    print("2nd Matrix is not diagonal matrix.")
