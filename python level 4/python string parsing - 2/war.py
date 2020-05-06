D={'H':5,'E':10,'A':3,'C':1}
d={'h':5,'e':10,'a':3,'c':1}
s=0
p=0
for i in range(int(input())):
    x=list(input())
    count=0
    temp=0
    temp1=0
    for i in x:
        if i=='.':
            count+=1
        elif i=='X' or i=='x':
            count+=2
        elif temp>0:
            s+=(temp*count)
            count=0
            temp=0
        elif temp1>0:
            p+=(temp1*count)
            count=0
            temp1=0
        if i in D:
            temp=D[i]
        elif i in d:
            temp1=d[i]
print(s)
print(p)

'''
============= testcase 01 ============
2
H...A..xC..E...a..h..c..e..$
H..........A......$
127
38
>>>
'''
        
            
