x=int(input())
y=[0 for i in range(x)]
for i in range(1,x+1):
    for j in range(0,x):
        if (j+1)%i==0:
            if y[j]==0:y[j]=1
            elif y[j]==1:y[j]=0
print(y.count(1))
'''
5

=>2

3
 => 1
 '''
