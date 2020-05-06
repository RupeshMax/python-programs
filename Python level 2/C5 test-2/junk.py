x=input().split(";")
l1,l2=[],[]
for i in x:
    if 'int' in i:
        i=i.replace('int','')
        l1.append(i)
    else:
        i=i.replace('char','')
        l2.append(i)
print("Integers")
for i in l1:
    i=i.replace(' ','')
    if ',' in i:
        a=i.split(",")
        for i in a:
            if len(i)==1:
                print("{}=junk".format(i))
            else:
                print(i)
    else:
        print(i)
print("Characters")
for i in l2:
    i=i.replace(' ','')
    if ',' in i:
        a=i.split(",")
        for i in a:
            if len(i)==1:
                print("{}=junk".format(i))
            else:
                print(i)
    else:
        print(i)

'''
int i,k=10;int a=-10;char b='c';
Integers
i=junk
k=10
a=-10
Characters
b='c'

'''
