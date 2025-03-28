class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds! Available balance: ${self.balance}")
        elif amount <= 0:
            print("Withdrawal amount must be positive!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def check_balance(self):
        print(f"Account balance: ${self.balance}")

# Example:-
account = BankAccount("Alice", 500)

account.check_balance()   
account.deposit(200)      
account.withdraw(100)     
account.withdraw(700)     
account.check_balance()   
