x=input().split("/")
l,l1=[],[]
for i in x:
    if i=='..':
        if len(l)==0: continue
        else:l.pop()
    else:l.append(i)
for i in l:
    if i==".":
        l.remove(i)
s=""
for i in l:
    if(i!=""):s+='/'+i
print(s)
