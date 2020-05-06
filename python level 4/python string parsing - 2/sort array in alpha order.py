str=input()
x=int(input())
arr=input().split(" ")[:x]
for i in str:
    for j in arr:
        if i==j[0]:
            print(j,end=" ")
'''
=============== test case 1 ==============
zyxwvutsrqponmlkjihgfedcba
6
the crocodiles snapped at the boat
the the snapped crocodiles boat at 
>>>
'''
