for i in range(int(input())):
    y=int(input())
    z=list(map(int,input().split(" ")[:y]))
    count=0
    a=z[0]
    l1,l2=[a],[]

    for i in range(1,len(z)):
        if a>z[i]:
            l1.append(z[i])
        else:
            l1.append(z[i])
            l2.append(l1)
            a=z[i]
            l1=[a]
    l2.append(l1)
    print(l2)
    l3=[]
    for i in ((l2)):
        if len(i)<=2:
            l3.append(0)
        else:
            while i[-1]<i[-2]:
                i.pop(-1)
            a=min([i[0],i[-1]])
            for j in range(1,len(i)-1):
                count+=a-i[j]
            l3.append(count)
    print(max(l3))
        
'''
1
6
5 10 9 6 9 0
[[5, 10], [10, 9, 6, 9, 0]]
3

2
6
6 7 9 6 9 3
3
6 9 9
[[6, 7], [7, 9], [9, 6, 9], [9, 3]]
3
[[6, 9], [9, 9], [9]]
0
'''
