import re
x=input().split(" ")
c=[]
for i in x:
    v=[]
    x=i.split("@")
    if len(x)==2:
        y=x[1].split(".")
        v.append(x[0])
        v.extend(y)
        c.append(v)
for i in c:
    print(*i)

'''
>>> 
=== testcase -1 ===
rupeasf@ffff.com fwdfw@sff.com wrg3rgg@gbfvf.com
rupeasf ffff com
fwdfw sff com
wrg3rgg gbfvf com
>>>
'''
