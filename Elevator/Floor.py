from ExternalButton import ExternalButton

class Floor:

    def __init__(self, floorNumber):
        self.floorNumber = floorNumber
        self.externalButton = ExternalButton()

    def submitExternalRequest(self, direction):
        self.externalButton.pressButton(self.floorNumber, direction)
