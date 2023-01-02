class Theatre:

    def __init__(self, theatreId, city, screens, shows):
        self.theatreId = theatreId
        self.city = city
        self.screens = screens
        self.shows = shows
    
    def getShows(self):
        return self.shows
    
    def getId(self):
        return self.theatreId
