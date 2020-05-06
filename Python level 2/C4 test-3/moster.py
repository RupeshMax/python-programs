x=input().split()
y=[list(input())]
l1=[]
for i in range(int(x[0])):
    a=list(input())
    y.append(0)
    if len(y)%2==0:
        y.remove(y[-1])
        a=a[1:]+a[:1]
        y.append(a)
    else:
        y.remove(y[-1])
        a=a[-1:]+a[:-1]
        y.append(a)        
y.append(list(input()))

for i in range(len(y)):
    print(''.join(y[i]))

'''
6 3
B..
X..
X..
.X.
.X.
..X
..X
..T
B..
..X
.X.
X..
..X
.X.
X..
..T

'''
