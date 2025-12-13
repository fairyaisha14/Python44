#Write a program to create a class Parrot and perform the following tasks - 1. Create a class variable species 2. Create a __init__ method that has instance variables - name and age 3. Create instances of class Parrot, passing arguments as well 4. Print Class variable by accessing it 5. Print Instance variables as well

# create class
class Parrot:

    # class attribute
    species = "bird"

    #instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot Class 
blu = Parrot("Blu",10)
woo = Parrot("Woo", 15)

#access the class attributes
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

# access the instance attributes
print("Blu {} is {} years old".format(blu.name, blu.age))
print("Woo {} is {} years old".format(woo.name, woo.age))