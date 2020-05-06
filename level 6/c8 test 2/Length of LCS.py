x,y=input(),input()
a,c=0,0
for i in range(len(x)):
    for j in range(a,len(y)):
        if x[i]==y[j]:
            c+=1
            a=j
            break
print("Length of LCS is ",c)
