x=input().replace(' ','').split(";")
x=[i.split(":") for i in x]
print(x)
d={}
count=0
for i in x:
    for j in i:
        if j[-5] not in d:
            d[j[-5]]=int(j[-1])
            count+=1
        elif d[j[-5]]<int(j[-1]):
            d[j[-5]]=int(j[-1])
            count+=1

print(count)
            
        
