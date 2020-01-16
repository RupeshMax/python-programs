for i in range(int(input())):
    l1=[]
    for j in range(1,int(input())+1):
        l1.append(int(bin(j)[2:].count('1')))
    print(sum(l1))
