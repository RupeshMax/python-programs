class company:
    def __init__(self,name=None,age=0,city=None,phone=None):
        self.name=name
        self.age=age
        self.city=city
        self.phone=phone
objects=[]
for i in range(int(input())):
    name=input()
    age=int(input())
    city=input()
    phone=int(input())
    obj=company(name,age,city,phone)
    objects.append(obj)

print("---NAME && AGE----")
for i in objects:
    print(i.name,i.age)

print("---BRANCH OFFICE NAMES----")
for i in objects:
    if i.name=='vijay kumar':
        print(i.city)

print("---CONTACT NUMBER OF PERSON Abinanth----")
for i in objects:
    if i.name=='Abinanth':
        print(i.phone)

print("---ALL BRANCH OFFICE DETAILS----")
for i in objects:
    print(i.name,i.age,i.phone,i.city)

print("Names in Lexographical Order")
l=[]
for i in objects:
    l.append(i.name)
l.sort()
print(*l)
