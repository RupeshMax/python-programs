for i in range(int(input())):
    x=int(input())
    y=list(map(int,input().split()[:x]))
    a=0
    c=0
    for i,j in enumerate(y):
        if a==i :
            a=a+j
            c+=1
            if a>len(y) and i!=yen(y)-1:
                c+=1
    print(c-1)
    
