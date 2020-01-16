
sno=0
chart=[]
while(1):
    option=int(input("1.To purchase2.view items 3.Generate Bill 4.exit"))
    if option==1:
        num_item=int(input())
        for i in range(num_item):
            name=input()
            product=int(input())
            price=int(input())
            total=product*price
            sno+=1
            items=[sno,name,product,price,total]
            chart.append(items)
        print(chart)
    if option==2:
        print("{:<8}{:<8}{:<8}{:<8}{:<8}".format('S.no','name','product','price','total price'))
        for i in range(len(chart)):
            print("{:<8}{:<8}{:<8}{:<8}{:<8}".format(chart[i][0],chart[i][1],chart[i][2],chart[i][3],chart[i][4]))
        print()
    if option==3:
        amount=[]
        for i in range(len(chart)):
            amount.append(chart[i][4])
        total_amount=(sum(amount))
        print("Total amount",total_amount)   
        if total_amount<500:
           payable=(total_amount)-(total_amount*2)/100
           discount=(total_amount*2)/100
           print("discount",discount)
           print("Amount payable",payable)
    if option==4:
        break
            
    
            
