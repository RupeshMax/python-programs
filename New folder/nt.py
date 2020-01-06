from collections import namedtuple as nt
x=int(input())
y=input().split()
print(y)
y[2]=nt(y[2],y[:])
#print(list(y[2]))
l=[]
for i in range(x):
    z=input().split()
    s=y[2](z[0],z[1],z[2],z[3])
    l.append(s)
sm=0
for i in l:
    sm+=int(i.mask)
print(sm//x)
