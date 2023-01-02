from Account import Account

class Member(Account):
    def __init__(self, memberId, email, password, name, address, phone, booksCheckedout):
        super().__init__(memberId, email, password, name, address, phone)
        self.booksCheckedout = booksCheckedout
    
    def incrementBooksCheckedout(self):
        self.booksCheckedout += 1