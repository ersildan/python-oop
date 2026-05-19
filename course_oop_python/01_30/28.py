class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('На счете недостаточно средств')
        else:
            self.balance -= amount

    def transfer(self, account, amount):
        if amount > self.balance:
            raise ValueError('На счете недостаточно средств')

        account.deposit(amount)
        self.balance -= amount

account = BankAccount(100)
# account.withdraw(150) # ValueError

account1 = BankAccount(100)
account2 = BankAccount(200)
account1.transfer(account2,50)
print(account1.get_balance()) # 50
print(account2.get_balance()) # 250