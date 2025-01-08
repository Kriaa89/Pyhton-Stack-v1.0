class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance=0): 
        self.int_rate =int_rate
        self.balance= balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount): 
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"balance {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

account1 = BankAccount(0.1, 400)
account2 = BankAccount(0.1)

account1.deposit(50).deposit(100).deposit(200).withdraw(150).yield_interest().display_account_info()
account2.deposit(300).deposit(400).withdraw(100).withdraw(50).withdraw(200).withdraw(100).yield_interest().display_account_info()