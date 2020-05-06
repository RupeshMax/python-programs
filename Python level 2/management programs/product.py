
store=[]
while(1):
    print("enter 1.insert 2.update 3.delete 4.seach 5.view 6.exit")
    x=int(input())
    if x>6:
        print("valid number")
    elif x==1:
        item_id=int(input())
        item_name=input()
        quantity=int(input())
        price=int(input())
        expiry=input()
        manu_data=input()
        product=[item_id,item_name,quantity,price,expiry,manu_data]
        store.append(product)
        print(store)
    elif x==2:
        item_id=int(input())
        for i in range(len(store)):
            if item_id==store[i][0]:
                #j=store.index(i)
                store.pop(i)
                print(store)
                item_id=int(input())
                item_name=input()
                quantity=int(input())
                price=int(input())
                expiry=input()
                manu_data=input()
                product=[item_id,item_name,quantity,price,expiry,manu_data]
                store.append(product)
                print(store)
    elif x==3:
        item_id=int(input())
        for i in range(len(store)):
            if item_id==store[i][0]:
                #j=store.index(i)
                store.pop(i)
                print(store)
    elif x==4:
        item_id=int(input())
        for i in range(len(store)):
            if item_id==store[i][0]:
                for j in range(len(store[i])):
                    print(store[i][j],end=" ")
                print()
    elif x==5:
        col=['ID','NAME','QTY','PRICE','EXPY','MAFX']
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(col[0],col[1],col[2],col[3],col[4],col[5]))
        for i in range(len(store)):
            print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(store[i][0],store[i][1],store[i][2],store[i][3],store[i][4],store[i][5]))
    elif x==6:
        break

"""enter 1.insert 2.update 3.delete 4.seach 5.view 6.exit
1
101
soap
20
30
10-1-19
12-2-20
[[101, 'soap', 20, 30, '10-1-19', '12-2-20']]
enter 1.insert 2.update 3.delete 4.seach 5.view 6.exit
1
102
powder
30
20
11-2-19
20-3-18
[[101, 'soap', 20, 30, '10-1-19', '12-2-20'], [102, 'powder', 30, 20, '11-2-19', '20-3-18']]
enter 1.insert 2.update 3.delete 4.seach 5.view 6.exit
2
102
[[101, 'soap', 20, 30, '10-1-19', '12-2-20']]
102
salt
32
45
11-2-19
20-3-18
[[101, 'soap', 20, 30, '10-1-19', '12-2-20'], [102, 'salt', 32, 45, '11-2-19', '20-3-18']]
enter 1.insert 2.update 3.delete 4.seach 5.view 6.exit
3
102
[[101, 'soap', 20, 30, '10-1-19', '12-2-20']]
enter 1.insert 2.update 3.delete 4.seach 5.view 6.exit
4
101
101 soap 20 30 10-1-19 12-2-20 
enter 1.insert 2.update 3.delete 4.seach 5.view 6.exit
5
ID         NAME       QTY        PRICE      EXPY       MAFX      
101        soap       20         30         10-1-19    12-2-20   
enter 1.insert 2.update 3.delete 4.seach 5.view 6.exit
6
"""
        
        
        
