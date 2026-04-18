class PiggyBank:
    def __init__(self, balance=0, volume=400):
        self.balance = balance
        self.volume = volume

    def add_coins(self, coins):
        if self.balance + coins > self.volume:
            raise ValueError('Копилка переполнена!')
        else:
            self.balance += coins

    def remove_coins(self, coins):
        if self.balance - coins < 0:
            raise ValueError('В копилке недостаточно монет!')
        else:
            self.balance -= coins

bank = PiggyBank()
print(bank.balance)

bank.add_coins(100)
print(bank.balance)

bank.remove_coins(10)
print(bank.balance)
