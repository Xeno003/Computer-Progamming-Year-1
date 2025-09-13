try:
    TestMark = int(input("Enter the test mark of the student: "))
    ExamMark = int(input("ENter the exm mark of the student: "))
    grade="0"

    TotalMark = TestMark+ExamMark
    if TotalMark>=70:
        if TestMark>=15 and ExamMark>50:
            grade="A"

        else: 
            grade="B"
    elif TotalMark>=65 and TotalMark<70:
        if ExamMark>50:
            grade="B"
        else:
            grade="C"
    elif TotalMark>=60 and TotalMark<65:
        if ExamMark>50:
            grade="C"
        else:
            grade="D"
    elif TotalMark>=50 and TotalMark<60:
        grade="D"
    elif TotalMark>=40 and TotalMark<50:
        grade="E"
    else:
        grade="F"
    print(f"The total mark is {TotalMark}")
    print(f"The grade is {grade}")   
except ValueError as err:
    print("please input a proper mark")

