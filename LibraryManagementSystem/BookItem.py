from Book import Book

class BookItem(Book):
    def __init__(self, title, subject, publisher, language, authors, barcode, dueDate, status):
        super().__init__(title, subject, publisher, language, authors)
        self.barcode = barcode
        self.dueDate = dueDate
        self.status = status
    
    def updateStatus(self, status):
        self.status = status