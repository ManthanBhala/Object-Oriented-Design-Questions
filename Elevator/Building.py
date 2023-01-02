from Floor import Floor
from ElevatorCar import ElevatorCar
from ElevatorController import ElevatorController
from ElevatorCreator import ElevatorCreator
from Display import Display
from Enums import *
from InternalButton import InternalButton
from ElevatorDoor import ElevatorDoor

class Building:

    def __init__(self):
        self.floorList = [Floor(0), Floor(1), Floor(2), Floor(3), Floor(4), Floor(5)]
        display = Display(0, Direction.UP)
        buttons = InternalButton([0, 1, 2, 3, 4, 5])
        elevatorState = ElevatorState.IDLE
        currentFloor = 0
        elevatorDirection = Direction.UP
        elevatorDoor = ElevatorDoor()
        self.elevatorCar1 = ElevatorCar(1, display, buttons, elevatorState, currentFloor, elevatorDirection, elevatorDoor)
        self.controller1 = ElevatorController(self.elevatorCar1)
        self.elevatorCar2 = ElevatorCar(2, display, buttons, elevatorState, currentFloor, elevatorDirection, elevatorDoor)
        self.controller2 = ElevatorController(self.elevatorCar2)
        ElevatorCreator.addElevatorController(self.controller1)
        ElevatorCreator.addElevatorController(self.controller2)
    
    def operate(self):
        self.floorList[2].submitExternalRequest(Direction.UP)
        self.floorList[4].submitExternalRequest(Direction.DOWN)
