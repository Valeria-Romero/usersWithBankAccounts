from bankaccount import BankAccount

class User:

    allBankAccounts  = []
    def __init__(self, accountOwner, accountNumber):
        self.accountOwner = accountOwner
        self.accountNumber = accountNumber
        self.balance = BankAccount(interestRate=1.003, balance=0)
        User.allBankAccounts.append(self)

    def make_withdrawal (self, amount):
        if amount <= self.balance:
            self.balance.make_withdrawal(amount)
        else:
            print("We cannot process your withdrawal")
            print(f"You current have {self.balance.balance}.")
            print(f"And you are trying to withdraw {amount}")

    def display_user_balance(self):
        print(f"User: {self.accountOwner}, Balance: ${self.balance.balance}.")

    def deposit (self, amount):
        self.balance.deposit(amount)

    def transfer_money(self,amount,other_user):
        self.balance -= amount
        other_user.balance += amount
        self.display_user_balance()
        other_user.display_user_balance()