import copy
def rotate(start,end,a):
    for i in range(a,end+1):
        if i==a:
            ans[start][i]=l1[start+1][i]
            ans[end][i]=l1[end][i+1]
        elif i==end:
            ans[start][i]=l1[start][i-1]
            ans[end][i]=l1[end-1][i]
        else:
            ans[start][i]=l1[start][i-1]
            ans[end][i]=l1[end][i+1]

    for i in range(a+1,end):
            ans[i][start]=l1[i+1][start]
            ans[i][end]=l1[i-1][end]

x=int(input())
y=int(input())
z=int(input())
if x==y:
    
    ans=[[0]*x for i in range(x)]
    l1=[[int(input()) for j in range(y)] for i in range(x)]

    for i in l1:
        print(*i)

    
    for j in range(z):
        start,end=0,x-1
        for i in range(x//2):
            rotate(start,end,i)
            start+=1
            end-=1
        if x%2!=0:
            a=x//2
            ans[a][a]=l1[a][a]
        l1=copy.deepcopy(ans)

        print()
        
        for i in ans:
            print(*i)
else:
    print("Both x and y is not equal")
