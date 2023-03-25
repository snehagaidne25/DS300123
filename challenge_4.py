class account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance


class savings_account(account):
    def __init__(self, title=None, balance=0, interest_rate=0):
        super().__init__(title,balance)
        self.interest_rate = interest_rate

account =  savings_account('Ram',50000,5)
print(account.title,account.balance,account.interest_rate)
