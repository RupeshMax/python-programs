x=int(input())
count=0
for i in range(1,x+1):
    for j in range(i):
        count+=1
        print(count,end=" ")
    print()
