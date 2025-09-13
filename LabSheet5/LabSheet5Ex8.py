x=float(input("Enter Number to be raised to power you want: "))
n=int(input("Enter the power you wanttne number to be raised to: "))
index=1
answer=x
while index<n:
    answer=answer*x
    index+=1
print("The answer is",answer)    

#why not 
#x=float(input("Enter Number to be raised to power you want: "))
#n=int(input("Enter the power you wanttne number to be raised to: "))
#answer=x**n
#print("The answer is",answer)
