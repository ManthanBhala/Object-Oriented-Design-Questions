from Search import Search
from Library import Library
from Constants import *
from BookLending import BookLending
from Enums import *

class LibraryManagementSystem:

    def __init__(self, library, search):
        self.library = library
        self.search = search

    def fetchLendingDetails(self, bookItem):
        None

    def checkoutBook(self, bookItem, member):
        if member.booksCheckedout >= MAX_BOOKS_ISSUED_TO_A_USER:
            print("User has already checked-out maximum number of books")
        else:
            bookLending = self.fetchLendingDetails(bookItem)
            if bookLending != None and bookLending.memberId != member.memberId:
                print("Book is reserved by another member")
            elif bookLending != None:
                bookLending.update_status(ReservationStatus.COMPLETED)
                member.incrementBooksCheckedout()
                bookItem.updateStatus(BookStatus.LOANED)

    def checkForFine(self, bookItem):
        book_lending = BookLending.fetch_lending_details(book_item_barcode)
        due_date = book_lending.get_due_date()
        today = datetime.date.today()
        if today > due_date:
            diff = today - due_date
            diff_days = diff.days
            Fine.collect_fine(self.get_member_id(), diff_days)
    
    def collectFine(self, memberId):
        None

    def returnBook(self, bookItem):
        self.check_for_fine(book_item.get_barcode())
        bookLending = BookReservation.fetch_reservation_details(book_item.get_barcode())
        if bookLending != None:
            # book item has a pending reservation
            book_item.update_book_item_status(BookStatus.RESERVED)
            bookLending.send_book_available_notification()
            book_item.update_book_item_status(BookStatus.AVAILABLE)

    def renewBook(self, bookItem):
        self.check_for_fine(book_item.get_barcode())
        bookLending = BookReservation.fetch_reservation_details(
        book_item.get_barcode())
        # check if self book item has a pending reservation from another member
        if bookLending != None and bookLending.get_member_id() != self.get_member_id():
            print("self book is reserved by another member")
            self.decrement_total_books_checkedout()
            book_item.update_book_item_state(BookStatus.RESERVED)
            bookLending.send_book_available_notification()
            return False
        elif bookLending != None:
            # book item has a pending reservation from self member
            bookLending.update_status(ReservationStatus.COMPLETED)

        BookLending.lend_book(book_item.get_bar_code(), self.get_member_id())
        book_item.update_due_date(datetime.datetime.now().AddDays(Constants.MAX_LENDING_DAYS))
        return True