n=int(input("Enter the integer: "))           #for entering the number
div=n                                         #
if n > 100:
    print("You entered the wrong number.")
else:
    while div!=0:
        factor=n/div
        if n%div==0:
            print(factor,"is a factor of",n)
        div=div-1
