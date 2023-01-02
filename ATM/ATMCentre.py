from ATM import ATM
from TransactionType import TransactionType

class ATMCentre:

    def __init__(self, noOfTwoThousandNotes, noOfFiveHundredNotes, noOfOneHundredNotes):
        self.atm = ATM(noOfTwoThousandNotes, noOfFiveHundredNotes, noOfOneHundredNotes)
    
    def initialize(self, user):
        card = user.getCard()
        self.atm.getCurrentATMState().insertCard(self.atm, card)
        self.atm.getCurrentATMState().authenticatePin(self.atm, card, int(input()))
        txnType = input()
        self.atm.getCurrentATMState().selectOperation(self.atm, txnType)
        if(txnType == TransactionType.CASH_WITHDRAWAL.value):
            self.atm.getCurrentATMState().cashWithdrawal(self.atm, user.card, int(input()))
        elif(txnType == TransactionType.BALANCE_CHECK.value):
            self.atm.getCurrentATMState().displayBalance(self.atm, card)
        else:
            self.atm.getCurrentATMState().exit(self.atm)