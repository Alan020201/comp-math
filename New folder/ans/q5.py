def perfectNumber(num):
  sum = 0   
  for i in range(1, num):     
    if num % i == 0:
      sum += i
  if sum == num:    
    return True   
  else:     
    return False

num = int(input("Enter the number: ")) 
if perfectNumber(num):   
  print(num, "is the perfect number") 
else:   
  print(num, "is not the perfect number")