x=input().split(" ")
l1=[]
for i in x:
    l=[]
    for j in i:
        if j.isnumeric():
            l.append(j)
    if len(l)>0:
        l1.append("".join(l))
print(l1)

            

'''
= testcase : 1
hai hello this is a 123 programming question for 2019
['123', '2019']
>>> 
=  testcase : 2
GSLV11 was launched in 19,2008
['11', '192008']
>>>
'''
