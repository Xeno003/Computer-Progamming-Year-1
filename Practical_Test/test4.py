import random

noiselevel=[]
for i in range (12):
    cols=[]
    for j in range(12):
        noise=0
        cols.append(noise)
    noiselevel.append(cols)

for i in range(10):
    for j in range (10):
        noise=random.randint(1,10)
        noiselevel[j+1][i+1]=noise

for i in range(10):
    for j in range(10):
        print(noiselevel[i+1][j+1],"\t",end="")
    print()

maxnoise=int(input("Please enter the loudest noise allowed: "))
print()
noisetotal=[]
for i in range (10):
    cols=[]
    for j in range(10):
        num=0
        for a in range (-1,2,1):
            for b in range(-1,2,1):
                #if (j+a+1)>=0 and (i+b+1)>=0:
                num+=noiselevel[j+a+1][i+b+1]
        cols.append(num)
    noisetotal.append(cols)

print("Total noise for each apartement is:-")
for i in range(10):
    for j in range(10):
        print(noisetotal[i][j],"\t",end="")
    print()
print("\n")

listofones=[]
for i in range (10):
    cols=[]
    for j in range(10):
        if noisetotal[j][i]>maxnoise:
            cols.append(1)
        else:
            cols.append(0)    
    listofones.append(cols)

print("The apartments that exceed the threshold are:-")
for i in range(10):
    for j in range(10):
        print(listofones[i][j],"\t",end="")
    print()