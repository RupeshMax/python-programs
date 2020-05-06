l1,l2=[],[]
for j in range(int(input())):
    l1.append(int(input()))
for i in l1:
    l2.append(l1.count(i))
if(max(l2)-(j+1)//2)+1 >0:
    print((max(l2)-(j+1)//2)+1)
else:
    print(-1)

