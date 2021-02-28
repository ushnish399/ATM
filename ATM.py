class Atm(object):
    def __init__(self, name,  cardNumber, pinNumber, balance, cash):
        self.name=name
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
        self.balance=balance
        self.cash=cash

    def changeName(self, name):
        self.name=name

    def balanceEnquiry(self, balance):
        self.balance=balance
    
    def cashWithdrawl(self, cash):
        self.cash=cash
    
card=Atm("ushnish", 9998887776666, 999, 50000, 25000)

card.balanceEnquiry(51000)
card.changeName("goose")
card.cashWithdrawl(2600)

print(card.name)
print(card.cash)
print(card.balance)





    