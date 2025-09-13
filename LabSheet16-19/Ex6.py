list_names=[]
list_maths=[]
list_physics=[]
n=int(input("Enter the number of students: "))
for i in range(n):
    stud_name=str(input("Enter the student's name: ")).strip()
    list_names.append(stud_name)
    maths_mark=float(input("Enter his/her mark in Mathematics: "))
    list_maths.append(maths_mark)
    physics_mark=float(input("Enter his/her mark in Physics: "))
    list_physics.append(physics_mark)
search_stud_name=str(input("Enter the student's name you want to search: ")).strip()
for i in range(len(list_names)):
    if list_names[i]==search_stud_name:
        print(f"{list_names[i]} scored {list_maths[i]} in Mathematics and {list_physics[i]} in Physics")
    