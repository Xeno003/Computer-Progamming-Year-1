listA=[]
listB=[]
x=int(input("Please enter the number of value you will enter: "))
for i in range(x):
    numA=int(input("Enter number to input in list A: "))
    listA.append(numA)
    numB=int(input("Enter number to  inout in list B: "))
    listB.append(numB)
sumA=sum(listA)
sumB=sum(listB)
print("The sum of the  two list is:",(sumA+sumB))   