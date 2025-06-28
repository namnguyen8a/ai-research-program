class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors
    
    def get_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Doors: {self.num_doors}"

my_car = Car("Ford", "Mustang", 2)
print(my_car.get_details())
