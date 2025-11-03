import math

def trig_calculator():
    print("Welcome to the Trigonometric Angle Calculator!")
    print("Choose a function: sin, cos, or tan")
    func = input("Function: ").strip().lower()

    value = float(input("Enter the value (in degrees): "))
    radians = math.radians(value)

    if func == "sin":
        result = math.sin(radians)
    elif func == "cos":
        result = math.cos(radians)
    elif func == "tan":
        result = math.tan(radians)
    else:
        print("Invalid function. Please choose sin, cos, or tan.")
        return

    print(f"{func}({value}°) = {round(result, 4)}")

trig_calculator()