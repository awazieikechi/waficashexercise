class User:
    
    def __init__(self, name):
        self.name = name
        self.amount = 0
        self.account_balance = 0
        self.active = True
        
    def activate(self):
         return self.active 
        
    def checkBalance(self):
        return self.account_balance
        
    def deposit(self, credit_amount):
        self.account_balance+=credit_amount
        return self.account_balance 
    
    def withdraw(self, debit_amount):
        if self.account_balance < 0:
            return "Transaction cannot continue due to insufficient balance"
        if (self.account_balance - debit_amount) < 0:
            return "Transaction cannot continue"
        self.account_balance -= debit_amount
        return self.account_balance 
        
    def transfer(from_account, to_account, amount):
        from_account.withdraw(amount)
        to_account.deposit(amount)

      