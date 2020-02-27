for i in range(int(input())):
    l1=[input().split(",") for j in range(int(input()))]
    for k in range(len(l1)-1):
        if int(l1[k][2])<int(l1[k+1][2]):
            l1[k],l1[k+1]=l1[k+1],l1[k]
    print(*l1)

'''
2
2
1,ram,17,AP
1,ravi,56,AP
['1', 'ravi', '56', 'AP'] ['1', 'ram', '17', 'AP']
2
1,leela,07,AP
1,sita,12,AP
['1', 'sita', '12', 'AP'] ['1', 'leela', '07', 'AP']
'''
