#Write a program to create a class with the named employee and create a constructor and destructor. Then, write a function to create an object for that class and delete the object. Make sure you call the function to get everything implemented!
# Create Clas
class Employee:
    #Initializing
    def __init__(self):
        print('Employee created')

    #Calling destructor
    def __del__(self):
        print("Destructer called")

def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj

print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')
