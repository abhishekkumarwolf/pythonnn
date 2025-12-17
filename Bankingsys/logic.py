class BankAccount:
    def __init__(self, accno, name, balance):
        self.accno = accno
        self.name = name
        self.balance = balance


    def credit(self, amount ):
        if amount < 0 :
            raise ValueError("Invalid depoist amount")
        self.balance += amount


    def debit(self, amount):
        
        if amount <= 0 :
            raise ValueError("Invalid withdrawl amount")
        
        if amount > self.balance:
            raise ValueError("Insufficient Balance")
        self.balance -= amount