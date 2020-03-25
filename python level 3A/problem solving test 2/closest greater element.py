x=int(input())
l=sorted([int(input()) for i in range(x)])
l1=[int(input()) for i in range(x)]
for i in l1:
    for j in l:
        if i<j:
            print(j,end=" ")
            break
        elif j>=max(l):
            print(-1,end=" ")

'''
6
2
5
6
1
8
9
2
1
0
5
4
9
5 2 1 6 5 -1
'''
