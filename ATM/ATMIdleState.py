from ATMState import ATMState
from ATMHasCardState import ATMHasCardState

class ATMIdleState(ATMState):

    def insertCard(self, atm, card):
        print("Card is inserted")
        atm.setCurrentATMState(ATMHasCardState())