#Write a program to create a class Vehicle and perform the following tasks - 1. Create an __init__ method with arguments - max_speed and mileage 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car 3. Print the values of max_speed and mileage by using the object

#create class
class Vehicle:

    # create init method
    def __init__(self, max_speed, mileage):
        
        #bind the arguments
        self.max_speed = max_speed
        self.mileage = mileage

#Object creation
modelX = Vehicle(240,18)

 #access the variable inside init method
print("Model Max Speed:",modelX.max_speed)
print("Model Milage:", modelX.mileage)
