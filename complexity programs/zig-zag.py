l1=[]
for i in range(int(input())):
    l1.append(int(input()))
print(l1)
for i in range(1,len(l1)):
    if i%2==0:
        if l1[i-1]<l1[i]:
            l1[i-1],l1[i]=l1[i],l1[i-1]
    elif i%2!=0:
        if l1[i-1]>l1[i]:
            l1[i-1],l1[i]=l1[i],l1[i-1]
print(l1)
