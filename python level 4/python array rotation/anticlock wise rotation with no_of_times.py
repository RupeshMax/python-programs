import copy
def rotate(start,end,a):
    for i in range(a,end+1):
        if i==a:
            ans[start][i]=l1[start][i+1]
            ans[end][i]=l1[end-1][i]
        elif i==end:
            ans[start][i]=l1[start+1][i]
            ans[end][i]=l1[end][i-1]
        else:
            ans[start][i]=l1[start][i+1]
            ans[end][i]=l1[end][i-1]

    for i in range(a+1,end):
            ans[i][start]=l1[i-1][start]
            ans[i][end]=l1[i+1][end]

x=int(input())
y=int(input())
z=int(input())
if x==y:
    
    ans=[[0]*x for i in range(x)]
    l1=[[int(input()) for j in range(y)] for i in range(x)]

    for i in l1:
        print(*i)

    
    for j in range(z):
        start,end=0,x-1
        for i in range(x//2):
            rotate(start,end,i)
            start+=1
            end-=1
        if x%2!=0:
            a=x//2
            ans[a][a]=l1[a][a]
        l1=copy.deepcopy(ans)

        print()
        
        for i in ans:
            print(*i)
else:
    print("Both x and y is not equal")

'''
======= Testcase -1 ======

3
3
1
2
3
4
5
6
7
8
9
1
2 3 4
5 6 7
8 9 1

3 4 7
2 6 1
5 8 9
>>> 
======= Testcase -2 ======
5
5
2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

2 3 4 5 10
1 8 9 14 15
6 7 13 19 20
11 12 17 18 25
16 21 22 23 24

3 4 5 10 15
2 9 14 19 20
1 8 13 18 25
6 7 12 17 24
11 16 21 22 23
>>>
'''
