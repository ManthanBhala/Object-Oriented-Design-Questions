class TheatreController:

    def __init__(self):
        self.cityVsTheatre = {}
        self.allTheatre = []

    def addTheatre(self, theatre, city):
        self.allTheatre.append(theatre)
        if city not in self.cityVsTheatre:
            self.cityVsTheatre[city] = []
        self.cityVsTheatre[city].append(theatre)

    def getAllShow(self, movie, city):
        theatreVsShows = {}
        for theatre in self.cityVsTheatre[city]:
            theatreShows = []
            for show in theatre.getShows():
                if(show.getMovie().getMovieId() == movie.getMovieId()):
                    theatreShows.append(show)
            if(theatreShows != []):
                theatreVsShows[theatre] = theatreShows
        return theatreVsShows
    
    def getShowByName(self, showName, movie, city):
        theatreVsShows = self.getAllShow(movie, city)
        print(showName)
        for theatre in theatreVsShows.keys():
            if(int(showName[0]) == theatre.getId()):
                for show in theatreVsShows[theatre]:
                    if(showName[1] == show.getShowStartTime()):
                        return show
