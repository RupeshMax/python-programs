for i in range(int(input())):
    l1,l2=[],[]
    q=(int(input()))
    z=input().split(" ")
    l1=list(map(int,z))
    y=len(l1)//2
    print(y)
    if y<=1:
        y+=1
    for j in range(y-1):
        if l1[j]>=l1[j+1]:
            l2.append('yes')
        else:
            l2.append('no')
    for j in range(y):
        if l1[-(j)]>=l1[-(j+1)]:
            l2.append('yes')
        else:
            l2.append('no')
    if 'no' not in l2:
        print('yes')
    else:
        print('no')
        
