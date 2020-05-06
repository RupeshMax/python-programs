for i in range(int(input())):
    y=(input())
    z=input().split()
    a=0
    for i in range(int(z[0])+1,int(z[1])-1):
        a+=str(i).count(y)
    print(a)
    
'''
2
1
10 20

=>9

3
250 500

=>145
'''
