import math
def moork(a,b,l):
    p=0
    q=0
    day=1
    while(p<a):
        if q<len(l) and day!=l[q][0]:
            if int(math.ceil((a-p)/b))>l[q][0]-day:
                s=l[q][0]-day
                p=p+b*s
                if p>=a:
                    return day
                else:
                    day=l[q][0]
            else:
                day=day+int(math.ceil((a-p)/b))-1
                p=a
        elif q<len(l) and day==l[q][0]:
            p=p+l[q][1]
            if p>=a:
                return day
            else:
                day=day+1
                q=q+1
        else:
            s=a-p
            day=day+int(math.ceil(s/b))-1
            p=a
    return day
n=list(map(int,input().split()))
l=[]
for i in range(n[2]):
    a=list(map(int,input().split()))
    l=l+[[a[0],a[1]]]
    l.sort()
print(moork(n[0],n[1],l))
