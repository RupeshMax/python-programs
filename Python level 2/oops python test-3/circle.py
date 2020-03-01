class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        r=self.radius
        print("Area is :{}".format(3.14*r*r))

    def perimeter(self):
        r=self.radius
        print("Perimeter is :",(2*3.14*r))

x=float(input())
obj=Circle(x)
obj.area()
obj.perimeter()
