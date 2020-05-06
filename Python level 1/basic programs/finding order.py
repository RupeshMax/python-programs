x=input().split(" ")
x=list(map(int,x))
l1,l2=[],[]
for i in range(x[0]):
    l1.append(input())
for i in range(x[1]):
    l2.append(input())
for i in range(len(l2)):
    count=0
    for j in range(len(l1)):
        if l2[i]==l1[j]:
            print(j+1,end=" ")
            count+=1
    if count==0:
        print(-1)
    else:
        print()
