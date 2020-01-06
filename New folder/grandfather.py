x=int(input())
l1,l2=[],[]
for i in range(x):
    y=input().split(" ")
    l1.append(y)
y=input()
print(l1)
for i in l1:
    if i[1]==y:
        a=i[0]
        break
for i in l1:
    if i[1]==a:
        l2.append(i[0])
print(l2)
print(len(l2))
