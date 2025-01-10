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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.balance}")
        return self


user=User("ali","alihajji@gmail.com")
user.make_deposit(100).make_deposit(200).make_withdrawal(50).display_user_balance()


user2 = User("yessine","yessinekriaa@gmail.com")
user2.make_deposit(500).make_deposit(100).make_withdrawal(50).display_user_balance()
