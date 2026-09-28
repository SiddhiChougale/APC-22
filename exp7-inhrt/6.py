class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance, interest_rate):
        BankAccount.__init__(self, account_no, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_no, balance, interest_rate, benefits):
        SavingsAccount.__init__(self, account_no, balance, interest_rate)
        self.benefits = benefits

    def display(self):
        interest = self.calculate_interest()

        print("Account No:", self.account_no)
        print("Balance:", self.balance)
        print("Interest Rate:", self.interest_rate, "%")
        print("Interest:", interest)
        print("Benefits:", self.benefits)
        print("----")


P1 = PremiumSavingsAccount(1001, 50000, 5, "Airport Lounge Access")

P1.display()
