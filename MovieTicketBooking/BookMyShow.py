from MovieController import MovieController
from TheatreController import TheatreController
from Movie import Movie
from Theatre import Theatre
from Show import Show
from Screen import Screen
from Seat import Seat
from Booking import Booking
from Enums import *

class BookMyShow:

    def __init__(self):
        self.movieController = MovieController()
        self.theatreController = TheatreController()
        self.initialize()

    def createMovies(self):
        avengers = Movie(1, "AVENGERS", 128)
        baahubali = Movie(2, "BAAHUBALI", 180)
        self.movieController.addMovie(avengers, CityNames.BENGALURU)
        self.movieController.addMovie(avengers, CityNames.DELHI)
        self.movieController.addMovie(baahubali, CityNames.BENGALURU)
        self.movieController.addMovie(baahubali, CityNames.DELHI)

    def createSeats(self):
        seats = []
        for i in range(40):
            seats.append(Seat(i, SeatCategory.SILVER))
        for i in range(40, 70):
            seats.append(Seat(i,SeatCategory.GOLD))
        for i in range(70, 100):
            seats.append(Seat(i, SeatCategory.PLATINUM))
        return seats

    def createTheatres(self):
        avengers = self.movieController.getMovieByName("AVENGERS")
        baahubali = self.movieController.getMovieByName("BAAHUBALI")

        inoxScreen = Screen(1, self.createSeats())
        inoxMorningShow = Show(1, avengers, inoxScreen, "8 hrs", range(100))
        inoxEveningShow = Show(2, baahubali, inoxScreen, "16 hrs", range(100))
        inoxShows = [inoxMorningShow, inoxEveningShow]
        inox = Theatre(1, CityNames.BENGALURU, inoxScreen, inoxShows)

        pvrScreen = Screen(1, self.createSeats())
        pvrMorningShow = Show(1, avengers, pvrScreen, "8 hrs", range(100))
        pvrEveningShow = Show(2, baahubali, pvrScreen, "16 hrs", range(100))
        pvrShows = [pvrMorningShow, pvrEveningShow]
        pvr = Theatre(2, CityNames.BENGALURU, pvrScreen, pvrShows)

        self.theatreController.addTheatre(inox, CityNames.BENGALURU)
        self.theatreController.addTheatre(pvr, CityNames.DELHI)

    def initialize(self):
        self.createMovies()
        self.createTheatres()

    def createBooking(self):
        userCity = input("Select Your City - " + " ".join([city.name for city in CityNames]) + ": ")
        city = CityNames[userCity]
        movies = self.movieController.getMoviesByCity(city)
        movieName = input("Select Your Movie - " + " ".join([movie.getMovieName() for movie in movies]) + ": ")
        movie = self.movieController.getMovieByName(movieName)
        theatreVsShows = self.theatreController.getAllShow(movie, city)
        print("Available Shows")
        for theatre, shows in theatreVsShows.items():
            print("Theatre-" + str(theatre.getId()) + ": " + " ".join([show.getShowStartTime() for show in shows]))
        showName = input("Enter Theatre No, Time: ").split(", ")
        show = self.theatreController.getShowByName(showName, movie, city)
        screen = show.getScreen()
        seats = screen.getSeats()
        print("Select Seats")
        for seat in seats:
            print("Seat No:", seat.seatId, seat.seatCategory.name)
        selectedSeats = [int(selectedSeat) for selectedSeat in input().split(" ")]
        booking = Booking(show, selectedSeats)
        booking.printBooking()
