list_id=[]
list_marks=[]
num=int(input("Enter the number of student to enter:"))
for i in range(num):
    id=int(input("Enter Id: "))
    marks=float(input())
    while (id<701 or id>799):
        id=int(input("You entered an invalid ID, Please try again: "))
        marks=float(input())    
        while (marks < 0 or marks > 100):
            marks = float(input("Enter marks"))
        list_id.append(id)
        list_marks.append(marks)

index_min = 0
index_max = 0

min = list_marks[0]
max = list_marks[0]

for i in range(1, len(list_marks)):
    if list_marks[i] < min:
        min = list_marks[i]
        index_min = i
    if list_marks[i] > max:
        max = list_marks[i]
        index_max = i

print("Max - sid: " + list_id[index_max] , "score mark" + max)
print("Min - sid: " + list_id[index_min] , "score mark" + min)