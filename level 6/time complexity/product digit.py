import math
n=int(input())
s=999999999999999999999
i=1
s1=[]
while i<s and i<math.sqrt(n):
    if n%i==0:
        k=n//i + n//(n//i)
        if k<s:
            s=k
    i+=1
print(s)
