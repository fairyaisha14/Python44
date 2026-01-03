class Circle:
    def __init__(self, radius):
        self.radius = radius  

    def area(self):
        return 3 * (self.radius ** 2) 

    def perimeter(self):
        return 2 * 3 * self.radius  

def main():
    radius = float(input("Enter the radius of the circle: "))
    
    circle = Circle(radius)
    
    print("Area:", circle.area())
    print("Perimeter:", circle.perimeter())

if __name__ == "__main__":
    main()
