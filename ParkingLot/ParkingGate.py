class ParkingGate:

    def __init__(self, floorNumber, gateNumber, isOpen):
        self.floorNumber = floorNumber
        self.gateNumber = gateNumber
        self.isOpen = isOpen

    def closeTheGate(self):
        self.isOpen = False