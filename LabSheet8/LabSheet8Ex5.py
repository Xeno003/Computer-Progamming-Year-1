ele_list=[]
largest=""
x=str(input("Enter data to input in the list: "))
#x=str(input("Enter number to input in the list: "))
while x!="#":
#while x!=o:
    ele_list.append(x)
    x=str(input("Enter next data to input in the list: "))
    smallest=ele_list(1)

for i in range (0,len(ele_list)):
    if ele_list(i)>largest:
        largest=ele_list
    elif ele_list(i)<smallest:
        smallest=ele_list(i)
#maxterm=max(ele_list)
#minterm=min(ele_list)


