#Level 1 --> Right and down
puzzle=[[0,1,0,0,0],
        [0,1,0,1,0],
        [0,0,0,1,0],
        [0,1,1,1,0],
        [0,0,0,0,0]]

size=len(puzzle)

ans=[[0]*size for i in range(size)]

def solve(r,c):
    if (r==size-1 and c==size-1) :
        ans[r][c]=1
        return True
    if r>=0 and c>=0 and r<size and c<size and ans[r][c]==0 and puzzle[r][c]==0:
        ans[r][c]=1
        if solve(r+1,c):
            return True
        if solve(r,c+1):
            return True
        ans[r][c]=0
        return False 

if solve(0,0)== True:
    for i in puzzle:
        print(i)
    print() 
    for j in ans:
        print(j)
else:
    print("No path")

'''
output:
[0, 1, 0, 0, 0]
[0, 1, 0, 1, 0]
[0, 0, 0, 1, 0]
[0, 1, 1, 1, 0]
[0, 0, 0, 0, 0]

[1, 0, 0, 0, 0]
[1, 0, 0, 0, 0]
[1, 0, 0, 0, 0]
[1, 0, 0, 0, 0]
[1, 1, 1, 1, 1]
'''
