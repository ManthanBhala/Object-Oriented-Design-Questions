class ParkingService:

    def __init__(self, parkingSpace, ticketService):
        self.parkingSpace = parkingSpace
        self.ticketService = ticketService

    def bookParking(self, ticketId, parkingEntryGateNumber, vehicle):
        parkingSpotBooked = None
        parkingFound = False
        for parkingFloor in self.parkingSpace.getParkingFloors():
            for parkingEntryGate in parkingFloor.parkingEntryGates:
                if(parkingEntryGate.gateNumber == parkingEntryGateNumber and parkingEntryGate.isOpen):
                    for parkingSpot in parkingFloor.parkingSpots:
                        if(parkingSpot.vehicleCategory == vehicle.vehicleCategoryWithCost and parkingSpot.isEmpty):
                            parkingSpotBooked = parkingSpot
                            parkingSpot.setVehicle(vehicle)
                            parkingSpot.setSpaceAvailableForParking(False)
                            parkingFound = True
                            break
                if(parkingFound):
                    break
            if(parkingFound):
                break
        return self.ticketService.getTicket(ticketId, vehicle, parkingEntryGateNumber, parkingSpotBooked)

    def freeParking(self, ticket):
        parkingFreed = False
        for parkingFloor in self.parkingSpace.getParkingFloors():
            for parkingEntryGate in parkingFloor.parkingEntryGates:
                if(parkingEntryGate.gateNumber == ticket.parkingEntryGateNumber):
                    for parkingSpot in parkingFloor.parkingSpots:
                        if(parkingSpot.spotNumber == ticket.parkingSpot.spotNumber):
                            parkingSpot.freeParkingSpot()
                            parkingFreed = True
                            break
                if(parkingFreed):
                    break
            if(parkingFreed):
                break
        return self.ticketService.getParkingFare(ticket)