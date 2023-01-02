class UserBankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdrawAmount(self, amount):
        self.balance -= amount
    
    def getBalance(self):
        return self.balance
