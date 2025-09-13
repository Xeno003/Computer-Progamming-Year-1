List1=[1,2,3,4,5,6,7,8,9,10]
List2=[23,56,67,78,3,98,42,12,4,34]
if len(List1)==len(List2):
    SumTotal=0
    SumList1=0
    SumList2=0
    for i in range (len(List2)):
        SumList1+=List1[i]
        SumList2+=List2[i]
    SumTotal=SumList1+SumList2
print(f" The sum for List1 is {SumList1}\n The sum for List2 is {SumList2}\n And their total is {SumTotal}")
        
