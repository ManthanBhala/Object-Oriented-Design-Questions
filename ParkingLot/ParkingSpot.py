class ParkingSpot:

    def __init__(self, spotNumber, vehicleCategory):
        self.spotNumber = spotNumber
        self.vehicleCategory = vehicleCategory
        self.isEmpty = True
        self.vehicle = None
    
    def freeParkingSpot(self):
        self.isEmpty = True
    
    def setVehicle(self, vehicle):
        self.vehicle = vehicle
    
    def setSpaceAvailableForParking(self, spaceAvailableForParking):
        self.isEmpty = spaceAvailableForParking
    
