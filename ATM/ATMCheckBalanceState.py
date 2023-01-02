from ATMState import ATMState

class ATMCheckBalanceState(ATMState):

    def displayBalance(self, atm, card):
        print("Your Balance is: " + str(card.getBankBalance()))
        self.exit(atm)

    def exit(self, atm):
        from ATMIdleState import ATMIdleState
        atm.setCurrentATMState(ATMIdleState())
        print("Exited")
        self.returnCard()

    def returnCard(self):
        print("Please collect your card")
