l=[]
for i in range(int(input())):
    l.append(int(input()))
a=l[0]
l1,l2=[],[a]
for i in range(1,len(l)):
    if a<=l[i]:
        a=l[i]
        l2.append(l[i])
        if len(l2)>2:
            l1.append(l2)
        l2=[a]
    else:
        l2.append(l[i])
#l1.append(l2)
print(l1)
count=0
for i in l1:
    a=i[0]
    for j in range(len(i)-1):
        count+=a-i[j]
print(count)
if len(l2)>2:
    while l2[0]>l2[-1]:
        l2.pop(0)
        if min(l2)==l2[-1]:
            l2.pop()
    a=l2[0]
    for j in range(len(l2)-1):
        count+=a-l2[j]
print(l2)
print(count)
        
