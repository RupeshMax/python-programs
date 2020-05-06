def pop(x):
    stack.pop()

def push(x):
    stack.append(x)
    
l,l1=[input(),input()],[]
for i in l:
    stack=[]
    for j in i:
        if j=='#':
            pop(j)   
        else:
            push(j)
    l1.append(stack)
print(True if l1[0]==l1[1] else False)
        
