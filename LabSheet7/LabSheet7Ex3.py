FloatList=[]
for i in range (12):
    num=float(input("Enter a float value: "))
    FloatList.append(num)
average=(sum(FloatList))/12
print(FloatList)
print("The average of this list is",average)
