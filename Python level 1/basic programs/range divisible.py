x=int(input())
y=int(input())
z=int(input())
l1=[]
for i in range(x,y+1):
    if i%z==0:
        l1.append(i)
print(len(l1))
