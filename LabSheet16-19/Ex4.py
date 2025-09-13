List1=[]
List1Reversed=[]
n=int(input("How many entries will you make? "))
for i in range(n):
    num=int(input("Enter what you want to into the list: "))
    List1.append(num)
List1.reverse()
print(List1)