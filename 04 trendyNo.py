num=int(input("Enter the number :"))
list1=[num]
if(num<=99):
    print("enter the 3 digit number")
else:
    x=str(num)
    a=int(x[1])
    if (a % 3)==0:
        print("Trendy Number")
    else:
        print("Not trendy Number")
