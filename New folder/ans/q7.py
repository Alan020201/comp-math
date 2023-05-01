def matrix_creation(m, n):
  matrix = []   
  for i in range(0, m):
    row = []     
    for j in range(0, n):       
      element = int(input("Enter {:d} {:d}: ".format(i, j)))       
      row.append(element)
    matrix.append(row)     
  return matrix

m = 3
n = 3
a = matrix_creation(m, n) 
print(a)
