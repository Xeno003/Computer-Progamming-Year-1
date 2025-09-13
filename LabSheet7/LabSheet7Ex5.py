intergerlist=[]
num=int(input("Enter interger(enter 0 when you when you want to stop): "))
while num!=0:
    intergerlist.append(num)
    num=int(input("Enter interger(enter 0 when you when you want to stop): "))
smallest=min(intergerlist)
largest=max(intergerlist)   
print(intergerlist)
print(smallest,"is the smallest value in the list")
print(largest,"is the largest value in the list")