from queue import PriorityQueue, Queue
from Enums import Direction

class ElevatorController:

    def __init__(self, elevatorCar):
        self.upMinPQ = PriorityQueue()
        self.downMaxPQ = PriorityQueue()
        self.pendingJobs = Queue()
        self.elevatorCar = elevatorCar

    def submitExternalRequest(self, floor, direction):
        if(self.elevatorCar.elevatorDirection == direction):
            if(direction == Direction.DOWN and self.elevatorCar.currentFloor >= floor):
                self.downMaxPQ.put(floor)
            elif(direction == Direction.UP and self.elevatorCar.currentFloor <= floor):
                self.upMinPQ.put(floor)
            else:
                self.pendingJobs.put(floor)
        else:
            if(direction == Direction.DOWN):
                self.downMaxPQ.put(floor)
            else:
                self.upMinPQ.put(floor)

    def submitInternalRequest(self, floor):
        if(self.elevatorCar.currentFloor >= floor):
            self.downMaxPQ.put(floor)
        else:
            self.upMinPQ.put(floor)

    def controlElevator(self):
        while(self.elevatorCar.elevatorDirection == Direction.UP):
            self.elevatorCar.move()
