class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient balance."

    def check_balance(self):
        return f"Balance for {self.owner}: ${self.balance}"

    def transfer(self, recipient, amount):
        if amount <= self.balance:
            self.balance -= amount
            recipient.deposit(amount)
            return f"Transferred ${amount} to {recipient.owner}. New balance: ${self.balance}"
        else:
            return "Insufficient balance for the transfer."


owner1 = input("Enter the owner of the first bank account: ")
balance1 = float(input("Enter the initial balance for the first bank account: "))
account1 = BankAccount(owner1, balance1)

owner2 = input("Enter the owner of the second bank account: ")
balance2 = float(input("Enter the initial balance for the second bank account: "))
account2 = BankAccount(owner2, balance2)

print(account1.check_balance())
print(account1.deposit(100))
print(account1.withdraw(50))

print(account2.check_balance())
print(account2.deposit(200))
print(account2.withdraw(75))

transfer_amount = float(input("Enter the amount to transfer from Account 1 to Account 2: "))
transfer_result = account1.transfer(account2, transfer_amount)
print(transfer_result)
print(account1.check_balance())
print(account2.check_balance())
