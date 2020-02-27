x,y,c=input(),input(),0
if len(x)>len(y):a,b=x,y
else:a,b=y,x
for i in a:
    if i in b:
        c+=1
print(len(a)-c)
    
