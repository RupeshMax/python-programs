#level 4 --> Four end Maze
import copy
puzzle=[[0,1,0,0,0],
        [0,1,0,1,0],
        [0,0,0,1,0],
        [0,1,1,1,0],
        [0,0,0,0,0]]

size=len(puzzle)

ans=[[0]*size for i in range(size)]

def solve(r,c):
    global dis
    if (r==size-1 and c==size-1) or (r==0 and c==0) or (r==0 and c==size-1) or (r==size-1 and c==0):
        dis+=1
        ans[r][c]=1
        no_dis.append(dis)
        shortpath=no_dis.index(min(no_dis))
        solution.append(copy.deepcopy(ans))
        for j in solution[shortpath]:
            print(j)
        print()
        ans[r][c]=0
        dis-=1
        return False
    if r>=0 and c>=0 and r<size and c<size and ans[r][c]==0 and puzzle[r][c]==0:
        dis+=1
        ans[r][c]=1
        if solve(r+1,c):
            return True
        if solve(r-1,c):
            return True
        if solve(r,c+1):
            return True
        if solve(r,c-1):
            return True
        ans[r][c]=0
        dis-=1
        return False 
    return False

solution,no_dis=[],[]
dis=0
if solve(2,2)== False:
    if no_dis!=[]:
        for i in puzzle:
            print(i)
        print()
        shortpath=no_dis.index(min(no_dis))
        print("Shortest path:",no_dis[shortpath])
        print()
        for j in solution[shortpath]:
            print(j)
        print()
    else:
        print("No path")
'''
output:
[0, 1, 0, 0, 0]
[0, 1, 0, 1, 0]
[0, 0, 0, 1, 0]
[0, 1, 1, 1, 0]
[0, 0, 0, 0, 0]

Shortest path: 5

[0, 0, 1, 1, 1]
[0, 0, 1, 0, 0]
[0, 0, 1, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
'''
