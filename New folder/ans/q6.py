def matrix_form(m, n):  
    for i in range(0, m):    
        for j in range(0, n):       
            print("* ", end = " ")     
            print("\n")
m = int(input("input row value: ")) 
n = int(input("input column value: ")) 
matrix_form(m, n)