class MovieController:

    def __init__(self):
        self.cityVsMovies = {}
        self.allMovies = []

    def addMovie(self, movie, city):
        self.allMovies.append(movie)
        if city not in self.cityVsMovies.keys():
            self.cityVsMovies[city] = []
        self.cityVsMovies[city].append(movie)
    
    def getMovieByName(self, movieName):
        for movie in self.allMovies:
            if(movie.getMovieName() == movieName):
                return movie
        return "Movie Not Found"
    
    def getMoviesByCity(self, city):
        return self.cityVsMovies[city]