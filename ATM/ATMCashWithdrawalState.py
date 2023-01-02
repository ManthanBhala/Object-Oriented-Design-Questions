from ATMState import ATMState

class ATMCashWithdrawalState(ATMState):

    def __init__(self):
        super().__init__()
        print("Please enter the Withdrawal Amount")

    def cashWithdrawal(self, atm, card, withdrawAmount):
        if(atm.getAtmBalance() < withdrawAmount):
            print("Insufficient fund in the ATM Machine")
            self.exit(atm)
        elif(card.getBankBalance() < withdrawAmount):
            print("Insufficient fund in the your Bank Account")
            self.exit(atm)
        else:
            card.withdrawAmount(withdrawAmount)
            atm.deductATMBalance(withdrawAmount)
            print("Withdrawal Amount: " + str(withdrawAmount))
            self.exit(atm)

    def exit(self, atm):
        from ATMIdleState import ATMIdleState
        atm.setCurrentATMState(ATMIdleState())
        print("Exited")
        self.returnCard()

    def returnCard(self):
        print("Please collect your card")
