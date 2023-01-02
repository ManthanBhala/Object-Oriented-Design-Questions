class Card:

    def __init__(self, cardNumber, pin, bankAccount):
        self.cardNumber = cardNumber
        self.pin = pin
        self.bankAccount = bankAccount

    def isCorrectPINEntered(self, pin):
        if (self.pin == pin):
            return True
        return False

    def getBankBalance(self):
        return self.bankAccount.getBalance()

    def withdrawAmount(self, amount):
        self.bankAccount.withdrawAmount(amount)

    def setBankAccount(self, bankAccount):
        self.bankAccount = bankAccount
