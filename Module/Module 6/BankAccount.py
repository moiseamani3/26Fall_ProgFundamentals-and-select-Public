import math 
class BankAccount:
    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

        

Mike_account = BankAccount("Mike", 500)
print(f"{Mike_account.owner_name}'s initial balance: ${Mike_account.balance}")

Mike_account.deposit(200)
print(f"{Mike_account.owner_name}'s balance after deposit: ${Mike_account.balance}")

Mike_account.withdraw(1000)  # Attempt to withdraw more than the balance
print(f"{Mike_account.owner_name}'s balance after withdrawal: ${Mike_account.balance}")



