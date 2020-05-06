d={')':'('}
x=input()
l1,l2=[],[]
for i in x:
    if i not in d:
        l1.append(i)
    else:
        l1.append(i)
        a=l1[::-1]
        for j in a:
            if d[')']==j:
                l2.append(j)
                break
            else:
                l2.append(j)

print(*l1)
print(*l2[::-1])
            
            
    
        


        
