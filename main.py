from bankaccount import BankAccount
from User import User

# firstAccount = BankAccount(1.003,500)
# secondAccount = BankAccount(1.003,0)

# firstAccount.deposit(50).deposit(30).deposit(20).make_withdrawal(50).yield_interest().display_account_info()
# secondAccount.deposit(85).deposit(40).make_withdrawal(15).make_withdrawal(7).make_withdrawal(8).make_withdrawal(5).yield_interest().display_account_info()

# BankAccount.printAllAccountsInfo()

lauraAccount = User("Laura Reyes", 123)

lauraAccount.deposit(500)

lauraAccount.display_user_balance()

lauraAccount.deposit(500)

lauraAccount.display_user_balance()