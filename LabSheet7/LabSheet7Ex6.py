studentidlist=[]
marklist=[]
for i in range (1,100):
    studentidlist.append(i+700)
    marklist.append(0)
for x in range (1,100):
    studentid=int(input("Enter the student's ID: "))
    mark=float(input("Enter student's mark: "))
    while mark not in range(0,101):
        mark=float(input("Please enter valid student's mark: "))
    indexi=studentidlist.index(studentid)
    marklist[indexi]=mark
maxindex=marklist.index(max(marklist))
minindex=marklist.index(min(marklist))
maxmark=marklist[maxindex]
minmark=marklist[minindex]
maxstud=studentidlist[maxindex]
minstud=studentidlist[minindex]
print(studentidlist)
print(marklist)
print( maxmark,"is the highest mark in the coursework, scored by",maxstud)
print(minmark,"is the lowest mark in the coursework, scored by",minstud)