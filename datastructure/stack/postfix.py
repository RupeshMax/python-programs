x="( a - ( b ) + ( a * b ) )"
#x="A * B + C * D"
x=x.split()
string=''
stack=[]
d={')':'('}
pro={'*':2,'/':2,'+':1,'-':1,'^':3}
for i in x:
    if i.isalnum():
        string+=(i+' ')
    else:
        if len(stack)==0:
            stack.append(i)
        elif i==')':
            a=stack[-1]
            while a!='(':
                string+=(a+' ')
                stack.pop()
                a=stack[-1]
            stack.pop()
        else:
            if i=='(':
                stack.append(i)
            elif pro[i]==pro[stack[-1]]:
                stack.pop()
                stack.append(i)
            elif '(' in stack:
                stack.append(i)
                
                
            elif pro[i]>pro[stack[-1]]:
                stack.append(i)
            
            else:
                string+=(stack[-1]+' ')
                stack.pop()
                stack.append(i)
for i in range(len(stack)):
    string+=(stack[-1]+' ')
    stack.pop()
print(string)
print(stack)
                
            
            
            

        
