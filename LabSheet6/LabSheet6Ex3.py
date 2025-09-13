x=int(input("Enter number that needs to be checked: "))
Num_is_prime= True
import math
n=int(math.sqrt(x))
for i in range(2,n,1):
    if x%i==0:
        Num_is_prime=False
        break
if Num_is_prime==False:
    print("Number is not prime")
else:
    print("Number is prime")       


