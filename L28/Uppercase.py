# Write a program to create a class IOString which consists of a constructor that gives a default value to variable str1. Next up create a method that gets a string as input from the user. Create another method that will print the string in the upper case. Next up create an object and call methods to get everything implemented
# create class
class IOString():

    #constructer to set default value
    def __init__(self):
        self.str1 = ""

        #function to get input from user 
    def get_String(self):
        self.str1 = input("Enter String : ")

        #function to print the string in upper case
    def print_String(self):
        print("Result is:", self.str1.upper())

#Object creation
str1 = IOString()

#Call functions
str1.get_String()
str1.print_String()