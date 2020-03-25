from collections import Counter as c 
x=c(list(input()))
l=set(sorted(x.values()))
if len(l)==1:
    print('No')
else:
    c=0
    l.remove(max(l))
    l=list(l)
    for i,j in x.items():
        if l[-1]==j:
            print(i)
            c=1
            break
    if c==0:print('no')
