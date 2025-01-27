class Vehicle:
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def describe(self):
        return f"This is a {self.bodystyle} vehicle."

class Car(Vehicle):
    def __init__(self, bodystyle, make, model):
        super().__init__(bodystyle)
        self.make = make
        self.model = model

    def describe(self):
        return f"This car is a {self.make} {self.model} ({self.bodystyle})."

# Create a car object
car = Car("sedan", "Toyota", "Corolla")
print(car.describe())
