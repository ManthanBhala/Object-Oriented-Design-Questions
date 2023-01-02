from Enums import Direction

class ElevatorCar:

    def __init__(self, id, display, buttons, elevatorState, currentFloor, elevatorDirection, elevatorDoor):
        self.id = id
        self.display = display
        self.buttons = buttons
        self.elevatorState = elevatorState
        self.currentFloor = currentFloor
        self.elevatorDirection = elevatorDirection
        self.elevatorDoor = elevatorDoor

    def move(self, direction, destination):
        startFloor = self.currentFloor
        if(direction == Direction.UP):
            for i in range(startFloor, destination+1):
                self.currentFloor = i
                self.display.setDisplay(self.currentFloor, self.elevatorDirection)
                self.display.showDisplay()
        else:
            for i in range(startFloor, destination-1, -1):
                self.currentFloor = i
                self.display.setDisplay(self.currentFloor, self.elevatorDirection)
                self.display.showDisplay()
