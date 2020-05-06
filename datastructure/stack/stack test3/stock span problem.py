x=list(map(int,input().split()))
x=x[::-1]
l=[]
for i in range(len(x)-1):
    c=1
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            c+=1
        else:
            break
    l.append(c)
l.append(1)
print(l[::-1])
