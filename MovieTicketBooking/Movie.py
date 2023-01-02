class Movie:
    def __init__(self, movieId, movieName, movieDurationInMinutes):
        self.movieId = movieId
        self.movieName = movieName
        self.movieDurationInMinutes = movieDurationInMinutes
    
    def getMovieId(self):
        return self.movieId
    
    def getMovieName(self):
        return self.movieName
    
    def getMovieDurationInMinutes(self):
        return self.movieDurationInMinutes