x=int(input())
y=input().split()[:x]
print(y)
a=y[0]
for i in range(1,len(y)):
    if a[0]==y[i][-1]:
        print(y[i],a,1)
    elif a[-1]==y[i][0]:
        print(a,y[i],-1)
