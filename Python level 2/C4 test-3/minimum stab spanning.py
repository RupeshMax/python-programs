x=int(input())
l1,l2=[],[]
for i in range(x):
    y=input().split()
    l1.append(int(y[0]))
    l2.append(int(y[1]))
print(min(l2),max(l1))
'''
6
6 3
5 4
2 6
1 5
3 2
7 1

=>1 7
'''
