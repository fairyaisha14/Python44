#Write a program to check how the exceptions and finally statement works
try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma :"))
    result = num1 / num2
    print("Result is", result)
#using multiple except block for different type of error
except ZeroDivisionError:
    print("Division by zero is error")

except SyntaxError:
    print("Comma is missin. Enter numbers separated by a comma like this 1,2")

except:
    print("Wrong Input")

else:
    print("No exeptions")

finally:
    print("This will execute no matter what")