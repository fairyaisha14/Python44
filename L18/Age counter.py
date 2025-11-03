try:
    user_input =int(input("Enter your age"))
    if user_input%2 == 0:
        print ("Your age is an even number")
    else:
        print("Your age is an odd number")
    
except ValueError:
    print("That is not a number")
