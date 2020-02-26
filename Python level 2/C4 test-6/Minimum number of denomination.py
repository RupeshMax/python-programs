x=int(input())
for i in range(x):
    y=int(input())
    l1=[0,0,0,0,0,0,0,0]
    while y>0:
        if y>=500:
            y-=500
            l1[0]+=1
        elif y>=100:
            y-=100
            l1[1]+=1
        elif y>=50:
            y-=50
            l1[2]+=1
        elif y>=20:
            y-=20
            l1[3]+=1
        elif y>=10:
            y-=10
            l1[4]+=1
        elif y>=5:
            y-=5
            l1[5]+=1
        elif y>=2:
            y-=2
            l1[6]+=1
        elif y>=1:
            y-=1
            l1[7]+=1
    print("500:{}\n100:{}\n50:{}\n20:{}\n10:{}\n5:{}\n2:{}\n1:{}".format(l1[0],l1[1],l1[2],l1[3],l1[4],l1[5],l1[6],l1[7]))
