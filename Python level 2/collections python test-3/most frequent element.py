from collections import Counter as c
d,l1=c([int(input()) for i in range(int(input()))]),[]
for k,v in d.items():
    if v==max(d.values()):l1.append(k)
print(sorted(l1)[0])
