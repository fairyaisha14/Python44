def find_circumference(radius):
    return round(2 * 3.14 * radius, 2)

# Ask the user for input
radius = float(input("Enter the radius of the circle: "))
circumference = find_circumference(radius)

print("The circumference is:", circumference)
