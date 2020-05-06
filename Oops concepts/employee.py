class Empolyee:
    def __init__(self):
        self.emp_name=input("name")
        self.emp_id=int(input("id"))
        self.emp_des=input("desigination")
        self.emp_salary=int(input("salaray"))
    def display_emp_list(self,r):
        print("Empolyee Name :",self.emp_name,"\nEmpolyee id :",self.emp_id,"\ndesigination :",
              self.emp_des,"\nSalary :",self.emp_salary,"\n level: ",r)
    def Level(self):
        if self.emp_salary>=20000:
            return 'Level A'
        elif self.emp_salary<=20000 and self.emp_salary>=15000:
            return 'Level B'
        elif self.emp_salary<=15000:
            return 'Level C'

n=int(input())
max1=0
l1=[]
for i in range(n):
    obj=Empolyee()
    if obj.emp_salary>max1:
        max1=obj.emp_salary
    l1.append(obj)
    obj.display_emp_list(obj.Level())
print(max1)
    




             
