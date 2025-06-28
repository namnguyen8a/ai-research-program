class CoffeeMachine:
    def __init__(self):
        self.__water_level = 1000
        self.__beans_level = 500
    
    def make_coffee(self):
        if self.__water_level > 50 and self.__beans_level > 20:
            self.__water_level -= 50
            self.__beans_level -= 20
            return "Enjoy your coffee"
        return "Not enough water or beans."

machine = CoffeeMachine() # Assume it requires 50 water, 20 beans
# Simulate making coffee until resources run out
for _ in range(20):
    machine.make_coffee()
print(machine.make_coffee())