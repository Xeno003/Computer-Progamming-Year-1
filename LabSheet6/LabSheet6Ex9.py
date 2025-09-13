x=int(input("How many number you would input: "))
even_count=0
odd_count=0
for i in range (1,x+1,1):
    num=int(input("Enter number: "))
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Number of even numbers:",even_count)
print("Number of odd numbers:",odd_count)