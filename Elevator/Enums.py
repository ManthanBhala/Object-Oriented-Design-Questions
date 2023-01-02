from enum import Enum

class Direction(Enum):
    UP = 'UP'
    DOWN = 'DOWN'

class ElevatorState(Enum):
    MOVING = 'MOVING'
    IDLE = 'IDLE'
