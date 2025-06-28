class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.mileage = 0
        self.is_running = False
    
    def start_engine(self):
        self.is_running = True
        print("Engine started")
        return None
    
    def stop_engine(self):
        self.is_running = False
        print("Engine stopped")
        return None
    
    def drive(self, kilometers):
        if self.is_running == True:
            self.mileage += kilometers
            return self.mileage
        return None

my_car = Car("Toyota", "Corolla")
my_car.drive(50) # Should not add mileage
my_car.start_engine()
my_car.drive(120)
my_car.stop_engine()
my_car.drive(30) # Should not add mileage
print(my_car.mileage)
    