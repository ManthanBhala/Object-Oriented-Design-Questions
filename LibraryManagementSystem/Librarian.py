from Account import Account

class Librarian(Account):
    def __init__(self, memberId, email, password, name, address, phone):
        super().__init__(memberId, email, password, name, address, phone)