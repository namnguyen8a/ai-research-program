class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return self.__age

p = Person("Alice", 30)
# Attempting p.__age = 40 should not change the internal state
print(p.get_age())