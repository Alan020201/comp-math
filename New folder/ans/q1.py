import math
def f(x):  
     return math.sin(x)
def degree_to_radian(d):   
    return d * math.pi/180
d = int(input("Enter your number: ")) 
x = degree_to_radian(d) 
result = f(x) 
print(result)
