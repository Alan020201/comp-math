def matrix_addition(A, B):     
    row_a = len(A)     
    col_a = len(A[0])
    row_b = len(B)     
    col_b = len(B[0])
    C = [[0 for j in range(0, col_a)] for i in range(0, row_a)]
    if row_a == row_b and col_a == col_b:       
        for i in range(0, row_a):         
            for j in range(0, col_a):           
                C[i][j] = A[i][j] + B[i][j]       
        return C    
    else:       
        return None

A = [[2, 3], [4, 5]]
B = [[3, 4], [2, 3]] 
C = matrix_addition(A, B) 
print(C)
