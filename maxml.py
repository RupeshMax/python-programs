x,l,l1=input(),[],[]
for i in range(len(x)-1):
    for j in range(i,len(x)):
        if x[j] not in l:l.append(x[j])
        else:break
    l1.append(len(l))
    l=[]
print(max(l1))
    
