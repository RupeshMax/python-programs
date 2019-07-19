lower=int(input("Enter the lower number"))
upper=int(input("Enter the upper number"))
list1=[]
for num in range(lower,upper + 1):
    if num>1:
        for j in range(2,num):
            if (num%j)==0:
                break
        else:
            list1.append(num)
 
print(*list1)
print(list1[-1])


        
