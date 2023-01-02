from enum import Enum

class TicketStatus(Enum):
    BOOKED = 'BOOKED'
    PASSED = 'PASSED'
    FAILED = 'FAILED'

class VehicleCategoryWithCost(Enum):
    TWOWHEELER = 10
    FOURWHEELER = 15

class PaymentCategory(Enum):
    UPI = 'UPI'
    CASH = 'CASH'
    CARD = 'CARD'