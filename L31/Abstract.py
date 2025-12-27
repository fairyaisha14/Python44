#Write a program to create a base class that consists of two functions - one to display a value, and another function is an abstract method. Next, create a subclass that consists of a method similar to the abstract method. Finally, showcase how Abstraction is being implemented in this example.

# Import necessary Modulws
from abc import ABC, abstractmethod

# Create Base class
class Absclass(ABC):

        # Function to print a value
    def print(self,x):
        print("Passed value: ", x)
        
        # Abstract Method
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")


# Create sub class 
class test_class(Absclass):
    def task(self):#
        print("We are inside test_class task")

# object of test_class created
test_obj = test_class()
test_obj.task()  
test_obj.print(100)  