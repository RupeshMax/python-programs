a=[100,1,4,3,2,99,200]
a.sort()
print(a)
l2,l1=[],[]
c=1
for i in range (len(a)):
    b=a[i]
    if b+1 in a:
        c+=1
        l1.append(c)
    else:
        c=1
#print(l1)
print(max(l1))

'''output
[1, 2, 3, 4, 99, 100, 200]
4
'''
