import copy     
matrix=[[1,1,0,2,1],
        [1,0,1,1,1],
        [1,0,0,2,1]]

ans=[[0,0,0,0,0],
     [0,0,0,0,0],
     [0,0,0,0,0]]

def rot(i,j):
    if i-1>=0 and i+1<len(ans):
        if matrix[i+1][j]==1:
            ans[i+1][j]=2
        if matrix[i-1][j]==1:
            ans[i-1][j]=2
    if i==0 and j+1<len(ans[1]):
        if matrix[i][j+1]==1:
            ans[i][j+1]=2

    if j-1>=0 and j+1<len(ans[1]):
        if matrix[i][j+1]==1:
            ans[i][j+1]=2
        if matrix[i][j-1]==1:
            ans[i][j-1]=2
    if j==0 or i+1<len(ans):
        if matrix[i+1][j]==1:
            ans[i+1][j]=2

x=1
c=0
while x!=0:
             
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==2:
                ans[i][j]=2
                rot(i,j)
    x=0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==1:
                if ans[i][j]==0:
                    ans[i][j]=1
                    x+=1
    c+=1
    if matrix==ans:
        c-=1
    else:
        matrix=copy.deepcopy(ans)  
    

for i in ans:
    print(*i)
print(c)     
                
            
