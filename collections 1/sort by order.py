d={}
for i in range(int(input())):
    key=input()
    d[key]=int(input())
print(d)
z=input()
if z=='B':
    v=sorted(d.values())
    a=0
    for i in v:
        for k,v1 in d.items():
            if v1==i:
                print(k,v1)
                a+=1
elif z=='A':
    k=sorted(d.keys())
    a=0
    for i in k:
        for k1,v in d.items():
            if k1==i:
                print(k1,v)
                a+=1
elif z=='C':
    k=sorted(d.keys())
else:
    print("Program closed!!!..")
    
''':
'''
