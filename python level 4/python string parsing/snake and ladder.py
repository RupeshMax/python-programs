
class QueueEntry(object): 
    def __init__(self, v = 0, dist = 0): 
        self.v = v 
        self.dist = dist 
  

def getMinDiceThrows(move, N): 
    visited = [False] * N 
    queue = [] 
    visited[0] = True   
    queue.append(QueueEntry(0, 0)) 
  
    qe = QueueEntry() 
    while queue: 
        qe = queue.pop(0) 
        v = qe.v 
        
        if v == N - 1: 
            break

        j = v + 1
        while j <= v + 6 and j < N: 
        
            if visited[j] is False: 

                a = QueueEntry() 
                a.dist = qe.dist + 1
                visited[j] = True
  
                a.v = move[j] if move[j] != -1 else j 
  
                queue.append(a) 
  
            j += 1
  
    return qe.dist 
  

N = 100
moves = [-1] * N

x=input().split(",")
for i in x:
    y=i.split(":")
    moves[int(y[0])]=int(y[1])

x=input().split(",")
for i in x:
    y=i.split(":")
    moves[int(y[0])]=int(y[1])

  
print("Min Dice throws required is {0}". 
       format(getMinDiceThrows(moves, N))) 
  
