x=input()
a=set(x)
c=0
for i in a:
    c+=(x.count(i))-1
print(c)
