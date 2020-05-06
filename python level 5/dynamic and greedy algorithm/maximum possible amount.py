def game(l,n):
    t=[[0 for i in range(n)] for i in range(n)]
    for p in range(n):
        for j in range(p,n):
            i=j-p
            x=0
            if (i+2)<=j:
                x=t[i+2][j]
            y=0
            if (i+1)<=(j-1):
                y=t[i+1][j-1]
            z=0
            if i<=(j-2):
                z=t[i][j-2]
            t[i][j]=max(l[i]+min(x,y),l[j]+min(y,z))
    return t[0][n-1]

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split(" ")))
    print(game(l,n))
