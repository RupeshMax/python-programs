x=int(input())
d={}
for i in range(x):
    y=input().split(":")
    if len(y[1])>5:
        z=y[1].split('$')
        for j in z:
            j=j.strip(" ").split(" ")
            if j[0] not in d:
                d[j[0]]=int(j[1])
            else:
                d[j[0]]+=int(j[1])
        print(d)
d1={}
for i,j in d.items():
    if j<1000:
        j=j*.40
        d1[i]=j

    if j>1000 and j<2000:
        t=999
        h=j-999
        t=t*.40
        j=(h*0.33)+t
        d1[i]=j

    if j>2000 and j<5000:
        t=999*0.40
        k=j-1999
        o=k*0.30
        p=j-999-k
        p=p*0.33
        j=p+t+o
        d1[i]=j

    if j>5000:
        j=j*0.20
        d1[i]=j

for i,j in d1.items():
    print(i,j)
