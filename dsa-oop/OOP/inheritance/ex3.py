class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def get_annual_salary(self):
        return self._salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self._bonus = bonus
    
    def get_annual_salary(self):
        return self._salary + self._bonus

mgr = Manager("David", 80000, 15000)
print(mgr.get_annual_salary())