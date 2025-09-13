alphlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
chosen_alph=[]
for i in range (7):
    char=str(input("Please enter a letter: "))
    chosen_alph.append(char)
print(chosen_alph)
word=str(input("Try to make the longest word with letter chosen: "))
word_list=[]
for letter in word:
    word_list.append(letter)
print(word_list)
f=open("d:\\University\\Coding\\Practical_Test\\words.txt",'r')
linefromfile=f.readline()
longest=[]
while linefromfile!="":
    comp_list=[]
    letter_list=[]
    check=0
    for line in linefromfile:
        for word in line:
            for letter in word.rstrip():
                letter_list.append(letter)
            if len(letter_list)<=(len(chosen_alph)):
                
       
                for letter in word.rstrip():
                    if letter in chosen_alph:
                            comp_list.append(letter)
                            check=1
                    if check==0:
                        break       
       
    if len(comp_list)>len(longest):
        longest=comp_list
        longestword=linefromfile
    linefromfile=f.readline()
print(longestword)       





