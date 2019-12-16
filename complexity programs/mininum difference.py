x=int(input())
for i in range(x):
    y=int(input())
    z=input().split(" ")
    z=list(map(int,(z)))
    print(z)
    z.sort()
    l1=[]
    for i in range(len(z)-1):
        sub=z[i+1]-z[i]
        l1.append(sub)
    print(l1)
    print(min(l1))

'''
output:
2
5
2 4 5 7 9
[2, 4, 5, 7, 9]
[2, 1, 2, 2]
1
10
87 32 99 75 56 43 21 10 68 49
[87, 32, 99, 75, 56, 43, 21, 10, 68, 49]
[11, 11, 11, 6, 7, 12, 7, 12, 12]
6
'''
