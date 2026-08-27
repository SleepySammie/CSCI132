class BankAccount:
    def __init__(self, ownerName):
        self.ownerName = ownerName
        self.balance = 0

    def deposit(self, amount):
        if amount < 0 or amount == 0:
            print('Error- Deposit must be a positive amount, balance unchanged')
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print('Error- insufficient funds, balance unchanged')
        else:
            self.balance -= amount

    def getBalance(self):
        return (f'Balance: {self.balance}') 
    
def main():
    account = BankAccount('Priya')
    account.deposit(100)
    account.withdraw(30)
    account.withdraw(1000)
    account.deposit(-5)
    print(account.getBalance())

main()