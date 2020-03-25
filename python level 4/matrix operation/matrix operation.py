'''
0 1 1 1 0
0 0 0 0 0
1 1 1 1 1
1 1 1 1 1
0 1 0 0 0
0 0 1 1 1
'''

x=int(input())
y=int(input())
l1=[[int(input()) for i in range(y)] for j in range(x)]
ans=[]
count=0
for i in l1:
    for j in i:
        if j==1:
            count+=1
        else:
            if count>0:
                ans.append(count)
            count=0
if count>0:
    ans.append(count)
print(ans)
                
