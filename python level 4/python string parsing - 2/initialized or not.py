x=input().split(" ")
y=x[1].split(',')
for i in y:
    if '=' in i:
        print(i[:i.index('=')],"=",i[i.index('=')+1:])
    else:
        print(i,"is not initialized")

'''
================== testcase 1 ==================
int i=3,j=6,k
i = 3
j = 6
k is not initialized
>>> 
================== testcase 2 ==================
int i,j,k
i is not initialized
j is not initialized
k is not initialized
>>>
'''
