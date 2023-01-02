class Screen:

    def __init__(self, screenId, seats):
        self.screenId = screenId
        self.seats = seats
    
    def getScreenId(self):
        return self.screenId
    
    def getSeats(self):
        return self.seats