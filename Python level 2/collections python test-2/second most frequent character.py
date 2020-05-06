from collections import Counter as c
x=c(input())
print(x)
l=[i for i in x.values()]
l.sort()
if max(l)==1:
    print('no')
else:
    a=max(l)
    while a==l[-1]:
        l.pop()
        if len(l)==0:
            break
    if len(l)==0:
        print('no')
    else:
        for i,j in sorted(x.items()):
            if max(l)==j:
                print(i)
                break
