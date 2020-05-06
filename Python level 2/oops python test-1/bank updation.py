class bank:
    def __init__(self,name,address,acc_no,phone_no,balance):
        self.name=name
        self.address=address
        self.acc_no=acc_no
        self.phone_no=phone_no
        self.balance=7000

x=1
while x<5:
    print("1.Enter Customer Credentials\n2.Withdraw\n3.Deposit\n4.GetBalance\n5.exit")
    x=int(input("enter Choice"))
    if x==1:
        name=input()
        address=input()
        acc_no=int(input())
        phone_no=int(input())
        balance=0
        obj=bank(name,address,acc_no,phone_no,balance)
    elif x==2:
        amount=int(input())
        if amount>20000:
            print("Withdraw cannot be more than limit 20,000")
        else:
            obj.balance-=amount
            print("Withdraw Successfull")
    elif x==3:
        amount=int(input())
        obj.balance+=amount
        print("Deposit Successfull!!")
    elif x==4:
        print("CurrentAvailable Balance",obj.balance)
    elif x==5:
        print("Session Closed Thank You!!!")
        
'''
1.Enter Customer Credentials
2.Withdraw
3.Deposit
4.GetBalance
5.exit
enter Choice1
rupesh
3 new nagar
354645135
3212323231
1.Enter Customer Credentials
2.Withdraw
3.Deposit
4.GetBalance
5.exit
enter Choice2
5000
Withdraw Successfull
1.Enter Customer Credentials
2.Withdraw
3.Deposit
4.GetBalance
5.exit
enter Choice3
8000
Deposit Successfull!!
1.Enter Customer Credentials
2.Withdraw
3.Deposit
4.GetBalance
5.exit
enter Choice4
CurrentAvailable Balance 10000
1.Enter Customer Credentials
2.Withdraw
3.Deposit
4.GetBalance
5.exit
enter Choice3
25000
Deposit Successfull!!
1.Enter Customer Credentials
2.Withdraw
3.Deposit
4.GetBalance
5.exit
enter Choice2
21000
Withdraw cannot be more than limit 20,000
1.Enter Customer Credentials
2.Withdraw
3.Deposit
4.GetBalance
5.exit
enter Choice4
CurrentAvailable Balance 35000
1.Enter Customer Credentials
2.Withdraw
3.Deposit
4.GetBalance
5.exit
enter Choice5
Session Closed Thank You!!!

'''
