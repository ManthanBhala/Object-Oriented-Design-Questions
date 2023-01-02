class Booking:

    def __init__(self, show, bookedSeats):
        self.show = show
        self.bookedSeats = bookedSeats
        self.payment = 100 * len(bookedSeats)
    
    def printBooking(self):
        print("BOOKING SUCCESSFUL")
        print("Movie:", self.show.getMovie().getMovieName())
        print("Screen:", self.show.getScreen().getScreenId())
        print("Time:", self.show.getShowStartTime())
        print("Amount:", self.payment)
        print("Seats:", self.bookedSeats)