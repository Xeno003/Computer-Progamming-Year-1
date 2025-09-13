from math import sqrt
x=int(input("Enter number to output prime number to: "))
prime_numbers=[x for x in range(2,x+1)]
for i in range (2,int(sqrt(x)+1)):
   
    for j in range (i*i,x+1,i):
       
       prime_numbers[j - 2] = None
       
prime_numbers = [x for x in prime_numbers if x != None]
print(prime_numbers)        

        
