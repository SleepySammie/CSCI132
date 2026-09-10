# Created class BankAccount with parameter ownerName initialized balance at 0
class BankAccount:
    def __init__(self, ownerName):
        self.ownerName = ownerName
        self.balance = 0

    # Created deposit method that validates amount making sure it is not less than 0 or equal to 0, adds amount to balance
    def deposit(self, amount):
        if amount < 0 or amount == 0:
            print(f'Error- Deposit must be a positive amount, balance unchanged\n')
        else:
            self.balance += amount

    # Created withdraw method that validates amount making sure it is not greater than the balance, subtracts amount from balance
    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Error- insufficient funds, balance unchange\n')
        else:
            self.balance -= amount

    # Created getBalance method returns the balance
    def getBalance(self):
        return (f'Balance: {self.balance}\n') 

# Defined main and called the following methods as instructed
def main():
    account = BankAccount('Priya')
    account.deposit(100)
    account.withdraw(30)
    account.withdraw(1000)
    account.deposit(-5)
    print(account.getBalance())
    
main()