class Player:
    def __init__(self, name, currentPosition):
        self.name = name
        self.currentPosition = currentPosition
    
    def getName(self):
        return self.name
    
    def getCurrentPosition(self):
        return self.currentPosition
    
    def setCurrentPosition(self, newPosition):
        self.currentPosition = newPosition