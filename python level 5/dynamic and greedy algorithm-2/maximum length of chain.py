a=int(input())
for i in range(0,a):
    b=int(input())
    d=input().split()
    j=1
    c=0
    l=[]
    for i in range(0,len(d)):
        if(j<len(d)):
            if(int(d[i])<int(d[j])):
                c=c+1
                l.append(c)
                j=j+1
            else:
                c=0
                j=j+1
    print(max(l))
