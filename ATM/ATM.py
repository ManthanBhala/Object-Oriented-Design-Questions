from ATMIdleState import ATMIdleState

class ATM:

    def __init__(self, noOfTwoThousandNotes, noOfFiveHundredNotes, noOfOneHundredNotes):
        self.currentATMState = ATMIdleState()
        self.atmBalance = noOfTwoThousandNotes*2000 + noOfFiveHundredNotes*500 + noOfOneHundredNotes*100
        self.noOfTwoThousandNotes = noOfTwoThousandNotes
        self.noOfFiveHundredNotes = noOfFiveHundredNotes
        self.noOfOneHundredNotes = noOfOneHundredNotes

    def setCurrentATMState(self, currentATMState):
        self.currentATMState = currentATMState

    def getCurrentATMState(self):
        return self.currentATMState

    def getAtmBalance(self):
        return self.atmBalance

    def getNoOfTwoThousandNotes(self):
        return self.noOfTwoThousandNotes

    def getNoOfFiveHundredNotes(self):
        return self.noOfFiveHundredNotes

    def getNoOfOneHundredNotes(self):
        return self.noOfOneHundredNotes

    def deductATMBalance(self, amount):
        self.atmBalance -= amount

    def deductTwoThousandNotes(self, number):
        self.noOfTwoThousandNotes -= number

    def deductFiveHundredNotes(self, number):
        self.noOfFiveHundredNotes -= number

    def deductOneHundredNotes(self, number):
        self.noOfOneHundredNotes -= number
