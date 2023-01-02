from ElevatorCreator import ElevatorCreator

class InternalButton:

    def __init__(self, availableButtons):
        self.availableButtons = availableButtons
    
    def pressButton(self, destination, elevatorCar):
        for elevatorController in ElevatorCreator.elevatorControllerList:
            if(elevatorCar == elevatorController.elevatorCar):
                elevatorController.submitInternalRequest(destination)
                break
