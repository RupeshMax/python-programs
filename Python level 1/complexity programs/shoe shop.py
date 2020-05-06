from collections import Counter as cs
x=int(input())
y=input().split(" ")
y=cs(y)
z=int(input())
l1,l2=[],[]
for i in range(z):
    q=input().split(" ")
    l1.append(q[0])
    l2.append(q[1])
l3,l4=[],[]
for i in l1:
    if i not in l3:
        l3.append(i)
l5=[]
for i in l3:
    l4=[]
    for j in range(len(l1)):
        if i==l1[j]:
            l4.append(l2[j])
    for j in range(y[i]):
        l5.append(int(l4[j]))
print(sum(l5))
                
                
                
