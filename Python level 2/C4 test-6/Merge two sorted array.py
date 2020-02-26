l1,l2=[int(input()) for i in range(int(input()))],[int(input()) for i in range(int(input()))]
for i in l1:
     if i not in l2:l2.append(i)
     
print(*(sorted(l2)))
