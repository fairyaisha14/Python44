#Write a program to create a class with following variables and methods - 1. Private variable named privateVar that contains an integer value 2. Create a private function privMeth that prints a message 3. Create a function hello that prints the value of privateVar 4. Create an object for the class and call all the functions.

# Class creation
class myClass:

    # private variable
    __privateVar = 27

    #private method
    def __privMeth(self):
        print("I'm inside class myClass")
    
    #Function to print value of private variable
    def hello(self):
        print("Private Variable value: ",myClass.__privateVar)


# Object creation and method call
foo = myClass()
foo.hello()
foo.__privMeth
