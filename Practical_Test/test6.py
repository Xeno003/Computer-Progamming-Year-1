word_list=["university","oneumonia","microsoft","paracetamol","programming","institutional","infrastructure","inusiodal","partitioning","nevertheless"]
import random
a=random.randint(0,9)
sel_word=word_list[a]
letter_list=[]
guess_list=[]
for letter in sel_word:
    letter_list.append(letter)
    guess_list.append("_")
n=len(letter_list)

for i in range (0,3):
    x=random.randint(0,n-1)
    if guess_list[x]!=letter_list[x]:
        guess_list[x]=letter_list[x]
    else:
        x=random.randint(0,n-1)
        guess_list[x]=letter_list[x]   
print(guess_list)
count=0

while count<5:
    print("You have",5-count,"chances to guess the correct word")
    character=str(input("Enter a letter:"))
    for j in range(0,len(letter_list)):
        if character==letter_list[j]:
            guess_list[j]=character
            print("You have guess a letter correctly")
            print(guess_list)
        elif character not in letter_list:
            count+=1
            print("Incorrect letter")
            print(guess_list)
            break
    if guess_list==letter_list:
        print("Congrats you have guessed the word")
        count=100
if count!=100:
    print("You have been hanged")            
