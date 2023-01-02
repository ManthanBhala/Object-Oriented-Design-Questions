from ATMState import ATMState
from ATMSelectOperationState import ATMSelectOperationState

class ATMHasCardState(ATMState):

    def __init__(self):
        super().__init__()
        print("Enter your card pin number ")

    def authenticatePin(self, atm, card, pin):
        if(card.isCorrectPINEntered(pin)):
            atm.setCurrentATMState(ATMSelectOperationState())
        else:
            print("Invalid PIN Number")
            self.exit(atm)

    def exit(self, atm):
        from ATMIdleState import ATMIdleState
        atm.setCurrentATMState(ATMIdleState())
        print("Exited")
        self.returnCard()

    def returnCard(self):
        print("Please collect your card")
