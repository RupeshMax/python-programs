l=[int(input()) for i in range(int(input()))]
while len(l)>1:
    print(max(l),end=" ")
    l=l[(l.index(max(l)))+1:] 
print(l[0]) 
'''
6
16
5
3
17
4
2
17 4 2

6
16
17
4
3
5
2
17 5 2
'''
