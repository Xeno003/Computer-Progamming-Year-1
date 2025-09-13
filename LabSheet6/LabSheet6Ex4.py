for x in range (25,51,1):
    prime=True
    for i in range(2,x,1):
        if x%i==0:
            prime=False
    if prime==True:
        print(x,end=" ")        