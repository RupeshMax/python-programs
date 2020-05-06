x=input().split()
l=[]
for i in x:
    if i=='+':
        l.append(l[-1]+l[-2])
    elif i=='C':
        l.pop()
    elif i=='D':
        l.append(2*l[-1])
    else:
        l.append(int(i))

print(sum(l))
