from itertools import permutations,combinations
n=int(input())
x=list(map(int,input().split(" ")[:n]))
y=int(input())
a=y//min(x)
print(a)
l1=[]
for i in range(a):
    l1.extend(x)
print(l1)
l2=[]
for i in range(a,1,-1):
    per=set(permutations(l1,i))
    for i in per:
        if sum(i)==y and sorted(i) not in l2:
            l2.append(sorted(i))
print(l2)
        
