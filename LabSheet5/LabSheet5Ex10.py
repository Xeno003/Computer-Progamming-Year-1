investment=float(input("Enter the amount you are investing: "))
rate=(float(input("Enter the rate you are investing at: ")))/100
year=0
double=investment*2
while (investment < double):
    investment=investment*(1+rate)
    year+=1    
print("The investment will be",investment,"in",year,"years.")