class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
class Car(Vehicle):
    def __init__(self, make, model,year):
        super().__init__(make, model) 
        self.year=year
ob1=Car("mersedes","sclass",2020)
ob2=Car("nissan","navarra",2019)
ob3=Car("bmw","m5 f90",2024)
print(ob1.make,ob1.model,ob1.year)
print(ob2.make,ob2.model,ob2.year)
print(ob3.make,ob3.model,ob3.year)