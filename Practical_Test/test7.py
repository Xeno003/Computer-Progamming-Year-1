alphlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_']
import random 
import math
text_2d=[]
text_list=[]
num_list=[]
encryption_list=[]
f=open("d:\\University\\Coding\\Practical_Test\\text.txt",'r')
linefromfile=f.readlines()
for line in linefromfile:
    for word in line.split(" "):
         text_list.append('_')
         for letter in word.rstrip():
              text_list.append(letter)
text_list.remove('_')          
print(text_list)
a=int(math.sqrt(len(text_list)))+1
index=0
for i in range(a):
    cols=[]
    for j in range(a):
        if index<len(text_list):
            t=text_list[index]
            cols.append(t)
        else:
            cols.append(' ')    

        index+=1
    text_2d.append(cols)

for i in range(a):
    for j in range(a):
        print(text_2d[i][j],"\t",end="")
    print()
print(len(text_list))

for i in range(a):
    cols=[]
    cols2=[]
    for j in range(a):
        x=random.randint(1,99)
        cols.append(x)
        cols2.append('*')
    num_list.append(cols)
    encryption_list.append(cols2)

for i in range(a):
    for j in range(a):
        print(num_list[i][j],"\t",end="")
    print()        

for i in range(a):
    for j in range(a):
        if num_list[i][j]>26:
            y=(num_list[i][j]/26)
            u=int(y)*26
            k=num_list[i][j]-u
        else:
            k=num_list[i][j]

        if text_list.index(text_2d[i][j])>k:
            k=text_list        
