def count(l,m,n):
    if n==0:
        return 1
    if n<0:
        return 0
    if m<=0 and n>=1:
        return 0
    return count(l,m-1,n)+count(l,m,n-l[m-1])
for i in range(int(input())):
    
    x=int(input())
    s=input().split(" ")
    l=[int(i) for i in s]
    n=int(input())
    m=len(l)
    print(count(l,m,n))
