class Circle:
    def area(self):
        area=3.14*r*r
        print("area of the circle",area)
    def perimeter(self):
        perimeter=2*3.14*r
        print("perimeter of the circle",perimeter)
obj=Circle()
r=int(input())
obj.perimeter()
obj.area()
              
