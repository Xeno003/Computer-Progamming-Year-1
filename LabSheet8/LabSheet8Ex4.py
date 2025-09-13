data_list=[]
list_data=[]
x=str(input("Enter data to input inside the list: "))

while x!="#":
    data_list.append(x)
    x=str(input("Enter next data to input inside the list(Enter # to stop): "))

data_list.reverse()
print("The list in reverse is",data_list)

