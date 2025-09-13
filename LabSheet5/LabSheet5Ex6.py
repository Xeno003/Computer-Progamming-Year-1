import random
randomNum=random.randint(1,100)
#print(randomNum)
num=int(input("Try to guess the number: "))
while num!=randomNum:      
    print("You guessed incorrectly. Try again.")
    num=int(input())
print("Great! You guessed correctly.")

