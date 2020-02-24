y=int(input())
x=sorted(input().split()[:y])
if x.count('0')+x.count('1')==len(x):
    print(*x)
else:
    print("Invalid Input")

'''
5
1 0 0 0 1

=> 0 0 0 1 1

5
1 0 2 0 1

=> Invalid input
'''
