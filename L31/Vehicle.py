class BMW: # BTW all of this is not realI am just guessing
    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed

    def display(self):
        print('My display of max speed is :', self.max_speed)
        print('My display of fuel type is :', self.fuel_type)

class Ferrari:
    def __init__(self,fuel_type, max_speed):
        self.max_speed = max_speed
        self.fuel_type = fuel_type
    
    def display(self):
        print('My display of max speed is :', self.max_speed*2)
        print('My display of fuel type is :', self.fuel_type)

oBMW = BMW('Diesel', 200) 
oFerrari = Ferrari('Petrol', 250)  

for car in (oBMW, oFerrari):
    car.display()