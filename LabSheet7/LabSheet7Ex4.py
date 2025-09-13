CharList=[]
wordcount=1
vowelcount=0
text=str(input("Enter the text: "))
CharList=[letter for letter in text]
print(CharList)
for letter in CharList:
    if letter==" ":
        wordcount=wordcount+1
    elif letter.lower() in ('a','e','i','o','u'):
        vowelcount=vowelcount+1
    elif letter.upper() in ('A','E','I','O','U'):
          vowelcount=vowelcount+1
print("Number is words is:",wordcount)          
print("Number of vowels is:",vowelcount)

