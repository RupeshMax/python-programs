x=int(input())
d={}
for i in range(x):
    y=(input())
    d[y]=int(input())
z=input()
if z=="A":
    for k,v in sorted(d.items()):
        print(k,v)
elif z=="B":
    for k,v in sorted(d.items(),key=lambda x:x[1]):
        print(k,v)
elif z=="C":
    for k,v in sorted(d.items(),key=lambda x:len(x[0])):
        print(k,v)
