class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
    
    def get_details(self):
        print(f"Name: {self.name}, Salary: {self._salary}")
        return None

emp = Employee("Charlie", 50000)
emp.get_details()
