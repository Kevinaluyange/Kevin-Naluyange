#BANKING SYSTEM EXAMPLE

class Account:
    def get_interest_rate(self):
        return 10 

class SavingAccount(Account):
    def get_interest_rate(self):
        return 15     #overriding interest rate
    
my_account = Account()
my_savings = SavingAccount()
print("Account interest rate: ", my_account.get_interest_rate())
print("Savings interest rate: ", my_savings.get_interest_rate())