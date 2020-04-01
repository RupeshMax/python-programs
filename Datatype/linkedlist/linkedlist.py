
#linkedlist

class Node:
    def __init__(self):
        self.node=int(input("Enter the element:"))
        self.next=None
        
class List:
    def __init__(self):
        self.head=None

    def printlinkedlist(self):
        data=self.head
        while data:
            print(data.node)
            data=data.next
    

if __name__=="__main__":
    LL=[]
    list1=List()
    print("----------------Choose the any one---------------------")
    print("   1.Insert \n   2.Delete \n   3.update \n   4.Display \n   5.Exit")
    x=int(input("Option:"))
    print()
    while x<5:
        #-------------------Insertion-------------------
        
        if x==1:
            print("----------------Choose the which position---------------------")
            print(" 1.At Beginning \n 2.At Middle \n 3.At End")
            y=int(input("Insert the element _________"))
            if y==1:
                if list1.head==None:
                    newNode=Node()
                    list1.head=newNode
                    LL.insert(0,newNode.node)
                else:
                    BeginNode=Node()
                    address=list1.head
                    BeginNode.next=address
                    list1.head=BeginNode
                    LL.insert(0,BeginNode.node)

            if y==2:
                position=int(input("Enter the position:"))
                temp=list1.head
                for i in range(1,position):
                    temp=temp.next
                temp1=temp.next
                middleNode=Node()
                temp.next=middleNode
                middleNode.next=temp1
                LL.insert(position,middleNode.node)

            if y==3:
                endNode=Node()
                endAddress=list1.head
                while endAddress:
                    address=endAddress
                    endAddress=endAddress.next
                address.next=endNode
                LL.append(endNode.node)

        #-------------------Deletion-------------------
                
        if x==2:
            print("----------------Choose the which position---------------------")
            print("  1.At Beginning \n  2.At Middle \n  3.At End")
            y=int(input("Delete the element _________"))
            if y==1:
                if list1.head==None:
                    print("No Element to delete")
                else:
                    firstNode=list1.head.next
                    list1.head=firstNode
                    LL.pop(LL[0])

            if y==2:
                position=int(input("Enter the position:"))
                temp=list1.head
                for i in range(1,position):
                    temp=temp.next
                temp1=temp.next
                temp2=temp1.next
                temp.next=temp2
                LL.pop(LL[position])


            if y==3:
                endAddress=list1.head
                endNode=0
                while endAddress:
                    if endAddress.next!=None:
                        endNode=endAddress
                    endAddress=endAddress.next
                if endNode==0:
                    endAddress=None
                else:
                    endNode.next=None
                LL.pop()

        #-------------------Updation--------------------

        if x==3:
            position=int(input("Enter the position:"))
            temp=list1.head
            for i in range(1,position):
                temp=temp.next
            temp.node=(int(input("Enter the new element:")))
            LL[position-1]=temp.node

        #-------------------Displaying-------------------
                
        if x==4:
            list1.printlinkedlist()

        #-----------------Exit-----------------------

        if x==5:
            print("Sucessfully LinkedList Constructed")
            exit()

        print("\nLinked list [",*LL,"]")
        print()
        print("----------------Choose the any one---------------------")
        print("   1.Insert \n   2.Delete \n   3.update \n   4.Display \n   5.Exit")
        x=int(input("Option:"))
        print()
                    
                    
                    
                    
            
        
        
