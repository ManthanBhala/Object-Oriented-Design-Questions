from ParkingFloor import ParkingFloor
from ParkingGate import ParkingGate
from ParkingSpace import ParkingSpace
from TicketService import TicketService
from ParkingService import ParkingService
from Enums import *
from ParkingSpot import ParkingSpot
from Vehicle import Vehicle

parkingSpots = []
parkingSpots.append(ParkingSpot(1, VehicleCategoryWithCost.TWOWHEELER))
parkingSpots.append(ParkingSpot(2, VehicleCategoryWithCost.TWOWHEELER))
parkingSpots.append(ParkingSpot(4, VehicleCategoryWithCost.FOURWHEELER))

parkingEntryGates = []
parkingEntryGates.append(ParkingGate(1, 1, True))
parkingEntryGates.append(ParkingGate(1, 2, True))

parkingExitGates = []
parkingEntryGates.append(ParkingGate(1, 3, True))
parkingEntryGates.append(ParkingGate(1, 4, True))

parkingFloor = ParkingFloor(1, parkingSpots, parkingEntryGates, parkingExitGates)

parkingSpace = ParkingSpace()
parkingSpace.addParkingFloor(parkingFloor)

ticketService = TicketService()
parkingService = ParkingService(parkingSpace, ticketService)

vehicle1 = Vehicle("Dl12 CR", VehicleCategoryWithCost.TWOWHEELER)
vehicle2 = Vehicle("Dl14 CR", VehicleCategoryWithCost.FOURWHEELER)

ticket1 = parkingService.bookParking(101, 1, vehicle1)
ticket2 = parkingService.bookParking(102, 2, vehicle2)
ticketService.getTicketsCollection()

fare1 = parkingService.freeParking(ticket1)
ticketService.getTicketsCollection()