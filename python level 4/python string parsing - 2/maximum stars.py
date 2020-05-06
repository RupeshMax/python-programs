x=input().split(" ")
l1=[]
for i in range(int(x[0])):
    y=input().split(" ")[:int(x[1])]
    l1.append(y)
'''
x=[4,4]
l1=[['*', 'r', '*', '*'], ['m', 'a', 'z', '*'], ['l', '*', 'f', 'k'], ['*', '*', '*', 'd']]
'''
d={}
for i in range(len(l1)):
    for j in range(len(l1[i])):
        if l1[i][j]!='*':
            count=0
            if j-1>=0 and l1[i][j-1]=='*':
                count+=1
            if j+1<int(x[1]) and l1[i][j+1]=='*':
                count+=1

                
            if i+1<int(x[0]):
                if l1[i+1][j]=='*':
                    count+=1
                if j+1<int(x[1]) and l1[i+1][j+1]=='*':
                    count+=1
                if j-1>=0 and l1[i+1][j-1]=='*':
                    count+=1
                
            if i-1>=0:
                if l1[i-1][j]=='*':
                    count+=1
                if j+1<int(x[1]) and l1[i-1][j+1]=='*':
                    count+=1
                if j-1>=0 and l1[i-1][j-1]=='*':
                    count+=1

                
            if l1[i][j] not in d:
                d[l1[i][j]]=count
            else:
                d[l1[i][j]]+=count
ans=[]
values=max(d.values())
for i,j in d.items():
    if j==values:
        ans.append(i)
print(min(ans))

'''
======== Testcase - 1 =======
4 4
* r * *
m a z *
l * f k
* * * d
f
>>>
'''
                
