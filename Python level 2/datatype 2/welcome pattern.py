n=input().split(" ")
x=int(n[0])
y=int(n[1])
z=(y//2)-1
for i in range(1,x*2,2):
    if i<x:
        #print('-'*(z)+('.|.'*i)+('-'*(z)))
        print(('.|.'*a).center(y,'-'))
        z-=3
        a=i
    elif i>x:
        z+=3
        #print('-'*(z)+('.|.'*a)+('-'*(z)))
        print(('.|.'*a).center(y,'-'))
        a-=2
        #print(i)
    else:
        #print('-'*((y-7)//2)+'WELCOME'+'-'*((y-7)//2))
        print("WELCOME".center(y,'-'))
'''
==================== Testcase 1 ===================
3 9
---.|.---
-WELCOME-
---.|.---
>>> 
==================== Testcase 2 ===================
9 27
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
>>> 
==================== Testcase 3 ===================
7 21
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------

'''