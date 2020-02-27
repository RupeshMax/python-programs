l1,l2,l3,l4=[],[],[],[]
for i in range(int(input())):
    l1.append(input().split())
for i in range(int(input())):
    l2.append(input().split())

for i in range(len(l1)):
    a="".join(l1[i])
    for j in range (len(l2)):
        b="".join(l2[j])
        if b in a:
            l3.append(l1[i])
            break
count=0
if len(l3)!=len(l2):
    print("False")
else:
    for i in range(len(l3)):
        a="".join(l3[i])
        b="".join(l2[i])
        if b in a:
            l4.append(a.index(b))
        else:
            count+=1
    s=set(l4)
    if len(s)==1 and count==0:
        print("True")
    else:
        print("False")

'''
4
1 1 1 5
2 2 3 6
2 2 3 5
3 3 3 3
3
2 2 3
3 3 3
2 2 3
1 1 1 5
2 2 3 6
2 2 3 5
3 3 3 3
2 2 3
3 3 3
2 2 3
[['2', '2', '3', '6'], ['2', '2', '3', '5'], ['3', '3', '3', '3']]
False

3
1 1 1
2 2 3
2 2 3
3
2 3 3
2 3 3
3 3 3
1 1 1
2 2 3
2 2 3
2 3 3
2 3 3
3 3 3
[]
False

3
1 1 1
2 2 3
2 2 3
2
2 3
2 3
1 1 1
2 2 3
2 2 3
2 3
2 3
[['2', '2', '3'], ['2', '2', '3']]
True
'''
    
    
