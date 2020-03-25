from collections import Counter as c
x=c(str(int(input())))
l=max(x.values())
l1,l2=[],[]
for i,j in x.items():
    if l==j:
        l1.append(int(i))
print(max(l1))

'''
= testcase 1
122366
6
>>> 
= testcase 2
5
5
>>> 
= testcase 3
1223385
3
>>> 
