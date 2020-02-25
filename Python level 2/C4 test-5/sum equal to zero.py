x=int(input())
for i in range(x):
    l1=[]
    y=int(input())
    z=input().split()[:y]
    z=list(map(int,z))
    for i in z:
        if i<0:
            z.remove(i)
            l1.append(i)
    a=0
    for i in z:
        a+=i
        #print(a+l1[0])
        for j in l1:
            if a+j==0:
                print("True")
    print(z,l1)
