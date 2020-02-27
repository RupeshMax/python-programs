l1=[]
x=list(input())
for i in range(len(x)):
    if x[i].isalnum():
        l1.append(x[i])
        x[i]=0
a=l1[::-1]
b=0
for i in range (len(x)):
    if x[i]==0:
        x[i]=a[b]
        b+=1
print(*x)
        
