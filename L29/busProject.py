class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity
        self.fare_price = self.set_default_fare()

    def set_default_fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)
        self.final_fare = self.calculate_final_fare()

    def calculate_final_fare(self):
        return self.fare_price * 1.10

    def display_final_fare(self):
        return f"Final Fare: ${self.final_fare}"

my_bus = Bus(40)
print(my_bus.display_final_fare())
