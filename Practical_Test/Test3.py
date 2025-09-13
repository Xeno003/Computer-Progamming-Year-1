alphlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Numalphlist=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
f=open("text.txt",'r')
linefromfile=f.readlines()
for line in linefromfile:
    for word in line.split(" "):
         for letter in word.rstrip():
            #print(letter)
            alph=letter.lower()
            if alph in alphlist:
                x=alphlist.index(alph)
                Numalphlist[x]=Numalphlist[x]+1
print(Numalphlist)

histoNum=[]
for i in range(26):
    l=[]
    for j in range(10):
        l.append(0)
    histoNum.append(l)

for i in range (len(Numalphlist)):
    for j in range (0,Numalphlist[i]//10+1):
        histoNum[9-j][i]=(j+1)*10
    histoNum[9-j][i]=Numalphlist[i]%10

for i in range(26):
    for j in range(10):
        print(histoNum[i][j],"\t\t",end="")
    print()
for i in  range(len(Numalphlist)):
    print(Numalphlist[i],"\t\t",end="")
print()   
