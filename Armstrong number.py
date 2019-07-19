num=int(input("Enter the number :"))
x=(len(str(num)))
a=num
sum=0
while a > 0:
    digit = a % 10
    sum+=digit ** x
    a //= 10

if sum == num:
    print("Armstrong number")
else:
    print("not")
