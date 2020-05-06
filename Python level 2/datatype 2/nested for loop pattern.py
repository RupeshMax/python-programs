x=int(input())
a=96+x
for i in range(x,0,-1):
    print("--"*((i)-1),end="")
    for j in range((x+1)-i):
        if j==0:
            print(chr(a-j),end="")
        else:
            print("-"+chr(a-j),end="")
        c=a-j    

    for j in range(1,(x+1)-i):
        print("-"+chr(c+j),end="")
    print("--"*((i)-1))


for i in range(2,x+1):
    print("--"*((i)-1),end="")
    for j in range((x+1)-i):
        if j==0:
            print(chr(a-j),end="")
        else:
            print("-"+chr(a-j),end="")
        c=a-j    

    for j in range(1,(x+1)-i):
        print("-"+chr(c+j),end="")
    print("--"*((i)-1))

'''
5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

'''
