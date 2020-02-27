for i in range(int(input())):
    l1=[sum(list(map(int,input().split()))) for j in range(int(input()))]
    for i in range(len(l1)):
        print(l1.index(min(l1))+1)
        l1[l1.index(min(l1))]=max(l1)+1
