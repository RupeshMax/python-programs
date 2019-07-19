x=int(input("Enter the number:"))
i=0
j=0
k=1
while (i<x):
    if (i<=1):
        next=i
    else:
        next = j+k
        j=k
        k=next
    print(next)
    i += 1
