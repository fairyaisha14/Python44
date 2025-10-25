 #Write a program to understand how the value error exception works
#using a try and expect 
try:
    number = int(input("Enter a number: "))
    print("The number entered is", number)
#using value error
except ValueError as ex:
    print("Exception :", ex)
