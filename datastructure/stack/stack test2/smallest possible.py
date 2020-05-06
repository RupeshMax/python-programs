x=input()
y=int(input())
stack=[]
c=0
for i in x:
    if stack:
        if i<stack[-1]:
            stack.pop()
            stack.append(i)
            c+=1
        else:
            c+=1
    else:
        stack.append(i)

    if c==y:
        a=x.index(i)
        break
for i in range(a+1,len(x)):
    stack.append(x[i])
print(stack)
