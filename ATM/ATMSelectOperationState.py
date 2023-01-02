from ATMState import ATMState
from ATMCheckBalanceState import ATMCheckBalanceState
from ATMCashWithdrawalState import ATMCashWithdrawalState
from TransactionType import TransactionType

class ATMSelectOperationState(ATMState):

    def __init__(self):
        super().__init__()
        self.showOperations()

    def showOperations(self):
        print("Please select the Operation ")
        i = 0
        for transactionType in TransactionType:
            i += 1
            print(str(i) + ': ' + transactionType.value)

    def selectOperation(self, atm, txnType):
        if(txnType == TransactionType.CASH_WITHDRAWAL.value):
            atm.setCurrentATMState(ATMCashWithdrawalState())
        elif(txnType == TransactionType.BALANCE_CHECK.value):
            atm.setCurrentATMState(ATMCheckBalanceState())
        else:
            print("Invalid Option")
            self.exit(atm)

    def exit(self, atm):
        from ATMIdleState import ATMIdleState
        atm.setCurrentATMState(ATMIdleState())
        print("Exited")
        self.returnCard()

    def returnCard(self):
        print("Please collect your card")
