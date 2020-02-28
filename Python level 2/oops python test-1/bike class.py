class Bike:
    def __init__ (self,Brand,CC,Color,Fuel_Type,Engine_Type):
        self.Brand=Brand
        self.CC=CC
        self.Color=Color
        self.Fuel_Type=Fuel_Type
        self.Engine_Type=Engine_Type

    def display(self):
        print("Brand : {}\nCC : {}\nColor : {}\nFuel Type : {}\nEngine Type : {}\n".format(self.Brand,self.CC,self.Color,self.Fuel_Type,self.Engine_Type))
        


b1=Bike('Pulsar','150CC','Black','Petrol','BSIV')
b2=Bike('Jawa','349CC','Green','Petrol','BSIV')
b3=Bike('Harley Davidson','500CC','Black','Petrol','BSIV')
b4=Bike('Royal Enfield','350CC','Battle Green','Petrol','BSIV')
bike=[b1,b2,b3,b4]

print("Before Updation :\n")
for i in bike:
    i.display()

b2.CC='500CC'
b4.Color='White'

print("After Updation :\n")
for i in bike:
    i.display()
