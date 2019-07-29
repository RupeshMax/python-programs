num=input("Enter the number:")
y=[]
list1=num.split()
list1.sort(reverse=True)
print(list1)
for i in list1:
    x = list(map(int,str(i)))
    y.append(x)
print(y)
#y.sort(key = lambda a: a[0],reverse=True)
print(y)
#for i in range(len(y)):
 #   if (y[i][0]==y[i+1][0]):
  #      if(len
for i in y:
    for j in i:
        print(j,end="")
