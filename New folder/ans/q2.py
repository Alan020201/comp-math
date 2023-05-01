def sum_of_list_elements(numberList):
  sum = 0   
  for i in range(0, len(numberList)): 
    sum = sum + numberList[i]   
    return sum
listSize = int(input("Enter size of the list: ")) 
numberList = [] 
for i in range(0, listSize):   
    listNumbers = int(input("Enter {:d} list element: ".format(i)))   
    numberList.append(listNumbers) 
    print(numberList)
result = sum_of_list_elements(numberList) 
print("Sum of {:d} list elements is ",result)   
