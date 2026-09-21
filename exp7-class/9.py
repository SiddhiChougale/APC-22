class ATM:
    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Money deposited")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Money withdrawn")
        else:
            print("Insufficient balance")

    def account_details(self):
        print("Name:", self.name)
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)


a = ATM("Rahul", 12345, 10000)

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Account Details")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        a.check_balance()

    elif choice == 2:
        amount = float(input("Enter amount: "))
        a.deposit(amount)

    elif choice == 3:
        amount = float(input("Enter amount: "))
        a.withdraw(amount)

    elif choice == 4:
        a.account_details()

    elif choice == 5:
        print("Thank you")
        break

    else:
        print("Invalid choice")
