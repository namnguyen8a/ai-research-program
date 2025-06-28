class BankAccount:
    def __init__(self, account_holder_name, initial_balance):
        self.__initial_balance = initial_balance
        self.account_holder_name = account_holder_name
    
    def deposit(self, amount):
        self.__initial_balance += amount
        return None
    
    def withdraw(self, amount):
        if amount > self.__initial_balance:
            print(f"Invalid! Amount of money must be smaller than or equal {self.__initial_balance}")
            return None
        self.__initial_balance -= amount
        return None
    
    def get_balance(self):
        return self.__initial_balance

account = BankAccount("John Doe", 100)
account.deposit(50)
account.withdraw(80)
account.withdraw(100) # This should fail
print(account.get_balance())