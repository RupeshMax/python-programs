class Officer:
    def __init__(self):
        self.name=input("name  :")
        self.age=int(input("age   :"))
        self.city=input("city  :")
        self.phone=int(input("phone :"))
n=int(input())
officerlist=[]
for i in range(n):
    print("Enter the",i+1,"branch officer details")
    print()
    obj=Officer()
    officerlist.append(obj)
    print()

print("----Displaying all the Branch Officer's name and age----")
for i in officerlist:
    print("{:<10} {:<10}".format(i.name,i.age))
print("\n----Branch Officer's city----")
for i in officerlist:
    print(i.city)
print("----the contact number of the person Abinanth----")
for i in officerlist:
    if i.name=="Abinanth":
        print(i.phone)
print("----Finding the class name----")
print(Officer.__name__)
print("----Displaying all the Branch Officers details----")

print("\n{:<10} {:<10} {:<10} {:<10}".format("Name","Age","City","Phone"))
for i in officerlist:
    print("{:<10} {:<10} {:<10} {:<10}".format(i.name,i.age,i.city,i.phone))

