from enum import Enum

class BookFormat(Enum):
    HARDCOVER = 'HARDCOVER'
    PAPERBACK = 'PAPERBACK'


class BookStatus(Enum):
    AVAILABLE = 'AVAILABLE'
    RESERVED = 'RESERVED'
    LOANED = 'LOANED'
    LOST = 'LOST'


class ReservationStatus(Enum):
    PENDING = 'PENDING'
    CANCELED = 'CANCELED'


class AccountStatus(Enum):
    ACTIVE = 'ACTIVE'
    CLOSED = 'CLOSED'
    CANCELED = 'CANCELED'
    BLACKLISTED = 'BLACKLISTED'