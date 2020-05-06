a=input()+'z'
d=a[0]
e=''
c=''
for i in range(1,len(a)):
    if(a[i].isdigit()):
        c+=a[i]
    else:
        e+=int(c)*d
        d=a[i]
        c=''
print(e)

'''
a10b10
aaaaaaaaaabbbbbbbbbb
'''
