num=int(input("Enter the number:"))
i=0
first=0
second=1
list1=[]
while (i<num):
    if (i<=1):
        next=i
    else:
        next = first+second
        first=second
        second=next
    list1.append(next)
    i += 1
print(*list1)
