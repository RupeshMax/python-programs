import copy
def rotate(start,end,a,y):
    for i in range(a,y):
        if i==a:
            ans[start][i]=l1[start][i+1]
            ans[end][i]=l1[end-1][i]
        elif i==y-1:
            ans[start][i]=l1[start+1][i]
            ans[end][i]=l1[end][i-1]
        else:
            ans[start][i]=l1[start][i+1]
            ans[end][i]=l1[end][i-1]

    for i in range(a+1,u-1):
            ans[i][start]=l1[i-1][start]
            ans[i][y-1]=l1[i+1][y-1]

x=int(input())
q=int(input())
z=int(input())  

ans=[[0]*q for i in range(x)]
l1=[[int(input()) for j in range(q)] for i in range(x)]


for i in l1:
    print(*i)

    
for j in range(z):
    start,end,y=0,x-1,q
    u=x
    for i in range(x//2):
        rotate(start,end,i,y)
        start+=1
        end-=1
        y-=1
        u-=1
    if x==y and x%2!=0:
        a=x//2
        ans[a][a]=l1[a][a]
    l1=copy.deepcopy(ans)

print()
        
for i in ans:
    print(*i)


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
======= Testcase -3 ======
4
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
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20

3 4 5 10 15
2 9 14 13 20
1 8 7 12 19
6 11 16 17 18
>>> 
'''
