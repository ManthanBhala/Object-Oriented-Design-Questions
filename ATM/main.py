from BankAccount import UserBankAccount
from Card import Card
from User import User
from ATMCentre import ATMCentre

atmCentre = ATMCentre(3, 10, 20)

bankAccount = UserBankAccount(3000)
card = Card(884455667700, 9999, bankAccount)
user = User(card, bankAccount)

atmCentre.initialize(user)