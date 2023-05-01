def smallDivisor(num):
  divisor = 2   
  while divisor <= num:     
      if num % divisor == 0:
        return divisor     
  divisor += 1
num = int(input("Enter a number: "))
print("The smallest divisor of", num, "is", smallDivisor(num))