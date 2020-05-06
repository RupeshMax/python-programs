n=input().split()
n=[int(i) for i in n]
tower=[]
tower.append(input())
for i in range(n[0]):
    tower.append(list(input())[:n[1]])
    if tower[i].count(".")==0:
        print("Impossible")
        exit()
tower.append(input())

#tower=[["B",".","."],["X",".","."],[".","X","."],[".",".","T"]]
d=0
min_dist=[]
p=[0,0]

def monsters(tow):
    B=tow[:1:1]
    T=tow[-1]
    tow=tow[1:len(tow)-1]
    for i in range(len(tow)):
        if i%2==0:
            tow[i]=tow[i][1:]+tow[i][:1:]
        else:
            tow[i]=tow[i][len(tow[i])-1:]+tow[i][:len(tow[i])-1]
    #print()
    B.extend(tow)
    B.append(T)
    #print("mosters func")
    #print(B)
    #print()
    return  B

def Save_Princess(r,c,d):
    global tower
    pr=0
    pc=0
    #print(d,r,c)
    if r==n[0]-1 and c==n[1]-1:
        d+=1
        min_dist.append(d)
        if d not in min_dist:
            return False
        else:
            return True
    if pr==r and pc==c:
        d+=1
    else:
        pr,pc=r,c

    if r>=0 and c>=0 and r<(n[0]) and c<(n[1]) and tower[r][c]!='X':
        tower=monsters(tower)
        if Save_Princess(r,c+1,d+1):
            return True

        if Save_Princess(r+1,c,d+1):
            return True

        if d < n[1] and Save_Princess(r,c,d+1) :
            return True
        return False
    #print("outer false")
    return False




d=0
#for i in monsters(tower):
#    print(i)
if Save_Princess(0,0,d+1)==False:
    print("Impossible")
else:
    if min_dist==[]:
        print("Impossible")
    else:
        print(min(min_dist))
