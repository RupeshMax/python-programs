def operations(n,c):
    n1=n//2
    c+=(n-2*n1)+1
    n=n1
    
    if n<=2:
        c+=n
        return c 
    return operations(n,c)

for i in range(int(input())):
    n=int(input())
    c=0
    print(operations(n,c))
    
