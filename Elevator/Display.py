class Display:

    def __init__(self, floor, direction):
        self.floor = floor
        self.direction = direction
    
    def setDisplay(self, floor, direction):
        self.floor = floor
        self.direction = direction

    def showDisplay(self):
        print("Floor: ", self.floor)
        print("Going ", self.direction.value)
