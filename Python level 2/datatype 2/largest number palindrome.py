l,l1=[],[]
for i in range(int(input())):
    x=list(input())
    if x==x[::-1] and len(x)>1:l1.append(len(x)),l.append("".join(x))
print(l[l1.index(max(l1))])   
