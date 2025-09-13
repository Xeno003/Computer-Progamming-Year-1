num=0
index=1
sum=0
while index<=20:
    num+=1
    if (num%2)==0:
        sum+=num
        index+=1
print("The sum of the first fifty even numbers is",sum)
