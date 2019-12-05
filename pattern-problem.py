n=int(input())
c=n-1
for i in range(0,n):
    for j in range(c):
        print(end=' ')
    c-=1
    a=65+i
    for k in range(i+1):
        print("*",end='')
    print(end=" ")
    for l in range(i+1):
        print(chr(a),end='')
        a+=1
    print()
c=n-1
q=c
for i in range(0,n):
    y=1+2*i
    x=5
    if(i!=0):
        for k in range(i):
            print(end=' ')
    for j in range(c+1):
        print(x,end='')
        x-=1
    c-=1
    print(end=" ")
    for l in range(q+1):
        print(y,end='')
        y+=2
    q-=1
    print()    
