def sumOfDigits(num):
  sum = 0  
  while (num != 0):     
      sum += num % 10     
      num = int(num / 10)
  print("The summed up number is", sum)   
  return True
  
num = int(input("Enter your number: ")) 
sumOfDigits(num)

