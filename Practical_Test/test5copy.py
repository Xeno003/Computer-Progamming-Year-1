bac_list=[]
for i in range (12):
    cols=[]
    for j in range (12):
        cols.append(0)
    bac_list.append(cols)

import random
for i in range (10):
    for j in range (10):
        num=random.randint(0,1)
        bac_list[j+1][i+1]=num

for i in range(10):
    for j in range(10):
        print(bac_list[i+1][j+1],"\t",end="")
    print()
n=int(input("Please enter number of cycles: "))                                               
for k in range (n):
    print("Cycle",k+2)
    for i in range (10): 
        for j in range (10):
            sum=0
            for a in range (-1,2,1):
                for b in range(-1,2,1):
                    sum+=bac_list[j+a+1][i+b+1]
            sum=sum-bac_list[j+1][i+1]
            if sum<=2:
                bac_list[j+1][i+1]=0
            elif sum==3:
                bac_list[j+1][i+1]=1
            elif sum>=4:
                if bac_list[j+1][i+1]==1:
                   bac_list[j+1][i+1]=0
                else:
                    bac_list[j+1][i+1]=1
    for i in range(10):
        for j in range(10):
            print(bac_list[i+1][j+1],"\t",end="")
        print()