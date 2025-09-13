import random 
x=random.randint(1,9)
num=int(input("Try to guess the number: "))
while num!=x:      
    print("Wrong Number!")
    num=int(input("Try Again: "))
print("Well guessed")