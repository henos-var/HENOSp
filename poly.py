class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Bird(Animal):
    def move(self):
        return f"{self.name} is flying! 🕊️"

class Fish(Animal):
    def move(self):
        return f"{self.name} is swimming! 🐟"

class Snake(Animal):
    def move(self):
        return f"{self.name} is slithering! 🐍"

class Vehicle:
    def __init__(self, model):
        self.model = model
    
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        return f"{self.model} is driving! 🚗"

class Airplane(Vehicle):
    def move(self):
        return f"{self.model} is flying! ✈️"

class Boat(Vehicle):
    def move(self):
        return f"{self.model} is sailing! ⛵"

# Create instances
animals = [
    Bird("Robin"),
    Fish("Nemo"),
    Snake("Viper")
]
vehicles = [
    Car("Tesla Model S"),
    Airplane("Boeing 747"),
    Boat("Sailfish")
]
# Demonstrate polymorphism
print("=== Animals Moving ===")
for animal in animals:
    print(animal.move())
print("\n=== Vehicles Moving ===")
for vehicle in vehicles:
    print(vehicle.move())