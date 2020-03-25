d={'}':'{',']':'[',')':'('}
for i in range(int(input())):
    x=list(input())
    l=[]
    for i,j in enumerate(x):
        if i==0:
            l.append(j)
        else:
            if j in d:
                if d[j]==l[-1]:
                    l.pop()
            else:
                l.append(j)
    print('balance' if len(l)==0 else 'unbalance')


'''
= testcase 1
[()]{}{[()()]()}
balance
[(])
unbalance
{()}[]
balance
>>>
'''
