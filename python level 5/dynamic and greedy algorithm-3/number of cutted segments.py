for i in range(int(input())):
    b=int(input())
    y=list(map(int,input().split()))
    l=[]
    for i in y:
        x=b
        c=0
        while x!=0:
            if x>=i:
                x-=i
                c+=1
            else:
                x=0
        l.append(c)
    print(max(l))
