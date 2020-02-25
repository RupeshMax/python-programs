x=int(input())
l1,l2,l3=[2],[0],[]
a,d,b=3,0,1
while len(l1)<x:
    for i in range(2,a):
        if a%i==0:
            break
    else:
        l1.append(a)
    a+=1
    c=d
    d=b
    b=d+c
    l2.append(d)
    
for i in range(len(l1)):
    l3.append(l1[i])
    l3.append(l2[i])

print(*l3)
    
'''
7
2 0 3 1 5 1 7 2 11 3 13 5 17 8

'''
