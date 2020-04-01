def pop(x):
    global c
    if stack[-1]==d[x]:
        stack.pop()
    else:
        c=1

def push(x):
    stack.append(x)
    
d,c,x={')':'(',']':'[','}':'{'},0,input()
stack=[]
for i in range(len(x)):
    if len(stack)==0:
        stack.append(x[i])
    elif x[i] in d:
        pop(x[i])
    else:
        c=1    
    if c==1:
        push(x[i])
        c=0

if len(stack)==0:
    print("Balance")
else:
    print("Unbalance")

'''
======== testcase -1 ========
)([]
Unbalance
>>> 
======== testcase -2 ========
[[]())[]]]]
Unbalance
>>> 
======== testcase -3 ========
[[[(())]]]
Balance
'''
