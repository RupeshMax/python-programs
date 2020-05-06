x=input()
l1=list(x)
y=x.split(" ")
l2=[]
for i in range(len(l1)):
      if " "==l1[i]:
            l2.append(i)
a="".join(y)
b=list(a)
b=b[::-1]
for i in range(len(l2)):
      b.insert(l2[i]," ")
print("".join(b))
