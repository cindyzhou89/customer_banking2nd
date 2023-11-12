from Account import Account

class cd_account(Account):

    def __init__(self, balance, interest_rate, months):
        Account.__init__(self, balance, interest_rate)
        self.months = months
        # Initialize the attributes for the CarExtras class.

    def months(self):
        return self.months

    def create_cd_account(self,balance, interest_rate, months):
        interest_earned = float(self.balance * (self.interest / 12) * months)
        myNewBalance = self.balance + interest_earned
        self.set_balance(myNewBalance)
        return float(interest_earned)
    
    def set_months(self, months):
    
        self.months = months