x=int(input())
y=x+1
for i in range(x+1,1,-1):
    a=i
    b=y-i
    for j in range(1,a):
        print("*",end=" ")
    for j in range(b):
        print(" ",end=(" "))
    print(" ",end="")
    for j in range(b):
        print(" ",end=(" "))
    for j in range(1,a):
        print("*",end=" ")
    print()
    
#second half

for i in range(1,x+1):
    for j in range(i):
        print("*",end=" ")
    for j in range(b):
        print(" ",end=(" "))
    print(" ",end="")
    for j in range(b):
        print(" ",end=(" "))
    b-=1
    for j in range(i):
        print("*",end=" ")
    print()

"""
3
* * *  * * * 
* *      * * 
*          * 
*          * 
* *      * * 
* * *  * * *

"""
