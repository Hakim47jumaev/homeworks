class Car:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def show_info(self):
        print(f"make: {self.make} , model : {self.model}")
class ElectroCar(Car):
    def __init__(self, make, model,battery_size):
        super().__init__(make, model)
        self.battery_size=battery_size
    def show_info(self):
        print( super().show_info(),f" batteery-size : {self.battery_size}")

ecar=ElectroCar("tesla,","model s",300)
print(ecar.show_info())