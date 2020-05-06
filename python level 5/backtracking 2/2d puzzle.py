def exist(board, word):
    if len(word) > len(board) * len(board[0]):
        return False
    visited = set()

    def dfs(i,j,index):
        if index == len(word):
            return True
        
        visited.add((i,j))
        for x,y in ((i+1,j),(i,j+1),(i-1,j),(i,j-1)):
            if 0<=x<len(board) and 0<=y<len(board[0]) and (x,y) not in visited:
                if board[x][y] == word[index]:
                    if dfs(x,y,index+1):
                        return True
        visited.remove((i,j))
        return False
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0]:
                if dfs(i,j,1):
                    return True
    return False
    
board =[
 ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word="ABCCED"
print(exist(board, word))
