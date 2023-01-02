from Enums import TicketStatus
from ParkingTicket import ParkingTicket

class TicketService:

    ticketsCollection = {}

    def getTicket(self, ticketId, vehicle, parkingEntryGateNumber, parkingSpot):
        ticket = ParkingTicket(ticketId, vehicle, parkingEntryGateNumber, parkingSpot, TicketStatus.BOOKED)
        self.ticketsCollection[ticketId] = ticket
        return ticket

    def getParkingFare(self, ticket):
        farePrice = ticket.vehicle.vehicleCategoryWithCost.value
        self.ticketsCollection.pop(ticket.ticketId)
        return farePrice

    def getTicketsCollection(self):
        for ticketId, ticket in self.ticketsCollection.items():
            print(ticketId, ticket.vehicle.vehicleNumber, ticket.parkingEntryGateNumber)