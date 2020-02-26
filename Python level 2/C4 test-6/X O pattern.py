x,y=int(input()),int(input())
for i in range(y):
    for j in range(x):
        a=min(i,j,x-j-1,y-i-1)
        if a%2==0:
            print('X',end="")
        else:
            print("O",end="")
    print()
'''
4
5
XXXX
XOOX
XOOX
XOOX
XXXX

6
7
XXXXXX
XOOOOX
XOXXOX
XOXXOX
XOXXOX
XOOOOX
XXXXXX
'''
