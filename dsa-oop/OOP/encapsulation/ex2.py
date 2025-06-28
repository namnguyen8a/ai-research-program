class BankAccount:
    def __init__(self, name, balance):
        self.name = name 
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
        return None
    
    def withdraw(self, amount):
        if amount > self.__balance:
            return None
        self.__balance -= amount
        return None
    
    def get_balance(self):
        return self.__balance
    
account = BankAccount("Bob", 500)
account.deposit(100)
try:
    account.__balance = 9999 # This should not work
except AttributeError:
    pass # Expected behavior
print(account.get_balance())