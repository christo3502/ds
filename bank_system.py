class bankAccount:

    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawn:", amount)
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def display(self):
        print("\n----Account Details----")
        print("Account Number : ", self.account_number)
        print("Account Holder : ", self.account_holder)
        print("Balance : ", self.balance)

account_number = int(input("Enter your account number : "))
account_holder = input("Enter your account holder name : ")
balance = float(input("Enter your account balance : "))
    
account1 = bankAccount(account_number, account_holder, balance)

deposit_amount = float(input("Enter the amount to deposit : "))
account1.deposit(deposit_amount)

withdraw_amount = float(input("Enter the amount to withdraw : "))
account1.withdraw(withdraw_amount)

account1.display()