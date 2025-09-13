num=[1,2,3,4,5]
print(num)
for i in range(0,5):
    number=int((input("Enter the contects of the list: ")))
    num.insert(i,number)
    num.remove(num[i+1])
print("The list is:",num)    

