class Show:

    def __init__(self, showId, movie, screen, showStartTime, unbookedSeatIds):
        self.showId = showId
        self.movie = movie
        self.screen = screen
        self.showStartTime = showStartTime
    
    def getMovie(self):
        return self.movie
    
    def getScreen(self):
        return self.screen
    
    def getShowStartTime(self):
        return self.showStartTime