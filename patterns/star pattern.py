x=int(input())
for i in range(x):
    y=int(input())
    count=0
    for j in range(1,y+1):
        count1=j+count
        q=(y*2)-count1
        for space in range(1,q):
            print(end=" ")
        for k in range(count1):
            print("*",end="")
        print()
        count+=1
