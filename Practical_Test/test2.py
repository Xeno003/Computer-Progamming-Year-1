f=open("text.txt",'r')
import random
linefromfile=f.readline()
line=1
my2dlist=[]
while(linefromfile!=""):
    list_text=(linefromfile.split(' '))
    cols=[]
    for i in range (len(list_text)):
        cols.append()
    my2dlist.append(list_text)
    my2dlist.append(cols)
    e=open("encryption.txt",'a')
    for i in range (len(list_text)):
        s=str(my2dlist[1][i])
        e.write(s + ',')   
    line+=1     
    linefromfile=f.readline()    
print("encryption.txt")
