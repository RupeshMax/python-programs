l1=[]
for i in range(int(input())):
    l1.append([input(),int(input())])
x=input()
print(l1)
print("Input String",end=" ")
for i in range(len(l1)):
    if l1[i][0].lower()==x.lower():
        print(l1[i][0])
        print(l1[i][1])
        
