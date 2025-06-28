class Animal:
    def eat(self):
        print("This animal is eating")
        return None

class Dog(Animal):
    def bark(self):
        print("Woof")
        return None
    
d = Dog()
d.eat()
d.bark()