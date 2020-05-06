x=int(input())
y=int(input())
l1=[[int(input()) for j in range(y)] for i in range(x)]
row=0
col=0
endrow=x
endcol=y

for i in l1:
    print(*i)
print()
while row<endrow and col<endcol:

    for i in range(col,endcol):
        print(l1[row][i],end=" ")

    row+=1

    for i in range(row,endrow):
        print(l1[i][endcol-1],end=" ")

    endcol-=1

    if row<endrow:

        for i in range(endcol-1,col,-1):
            print(l1[endrow-1][i],end= " ")

        endrow-=1

    if col < endcol:
        
        for i in range(endrow,row-1,-1):
            print(l1[i][col],end=" ")

        col+=1

        
        

                
    
    
    
