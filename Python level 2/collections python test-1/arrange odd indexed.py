x=int(input())
l1=[int(input()) for i in range(x)]
for i in range(1,x-1,2):
    if l1[i]<l1[i-1]:
        l1[i],l1[i-1]=l1[i-1],l1[i]
    if l1[i]<l1[i+1]:
        l1[i],l1[i+1]=l1[i+1],l1[i]
print(*l1)
    
        
