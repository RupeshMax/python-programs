number=int(input("Enter the number:"))
if ((number <= 10) or (number >= 99)):
    print("enter the number between 10 to 99")
else:
    num=str(number)
    a=int(num[0])+int(num[1])
    b=int(num[0])*int(num[1])
    x=int(a)+int(b)
    if (x==number):
        print("Special Number")
    else:
        print("Not a Special Number")
