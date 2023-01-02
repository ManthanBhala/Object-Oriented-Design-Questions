from ElevatorCreator import ElevatorCreator

class ExternalButton:

    def pressButton(self, floor, direction):
        for elevatorController in ElevatorCreator.elevatorControllerList:
           elevatorId = elevatorController.elevatorCar.id
           if(elevatorId%2==1 and floor%2==1):
               elevatorController.submitExternalRequest(floor, direction)
           elif(elevatorId%2==0 and floor%2==0):
               elevatorController.submitExternalRequest(floor, direction)