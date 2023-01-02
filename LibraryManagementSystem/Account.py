from Enums import AccountStatus

class Account:

    def __init__(self, memberId, email, password, name, address, phone):
        self.memberId = memberId
        self.email = email
        self.password = password
        self.name = name
        self.address = address
        self.phone = phone
        self.status = AccountStatus.ACTIVE