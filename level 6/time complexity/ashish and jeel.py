for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    if n==1:
        print("Ashish")
        continue
    a=0
    b=s[-1]
    A=[0]*(n-1)
    B=[0]*(n-1)
    c=0
    for i in range(n-1):
        if s[i]>a:
            a=s[i]
        if s[n-1-i]<b:
            b=s[n-1-i]
        A[i]=a
        B[n-2-i]=b
    for i in range(n-1):
        if A[i]<B[i]:
            c+=1
    if (c%2)==0:
        print("Ashish")
    else:
        print("Jeel")
