for i in range(int(input())):
    y=input().split()
    z=(input().split())[:int(y[0])]
    print(*(z[int(y[1]):]+z[:int(y[1])]))
'''
2
5 3
1 2 3 4 5 6

=>4 5 1 2 3

5 2
1 2 3 4 5

=>3 4 5 1 2
'''
