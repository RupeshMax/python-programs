m=int(input())
n=int(input())
mat=[[int(input()) for j in range(n)] for i in range(m)]
arr=[]
for i in range(m):
    for j in range(n):
        if mat[i][j]==1:
            ind=0
            for l in range(j,n):
                if mat[i][j]==1:
                    ind=1
                else:
                    break
            cnt=ind+1-j
            for p in range(i+1,m):
                temp=mat[p][j:ind+1]
                if sum(temp)==len(temp):
                    cnt+=len(temp)
                else:
                    arr.append(cnt)
                    break
print(max(arr))
