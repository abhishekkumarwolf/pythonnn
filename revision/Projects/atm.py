'''
 ATM Machine Simulation

Simulate the working of an ATM Machine using OOP principles.
User authentication using PIN

Functions:
Check balance
Withdraw cash
Deposit cash
Maintain transaction history
Enforce daily withdrawal limits

OOP Concepts
Abstraction
Encapsulation    
Validation logic 
'''
import json

class User:

    def __init__(self, userId, name, balance, pin):
        self.userId = userId
        self.name = name
        self.balance = balance
        self.pin = pin

    def to_dict(self):
        return {
            "userId": self.userId,
            "name": self.name,
            "balance": self.balance,
            "pin": self.pin
        }

    def check_balance(self):
        return {"Balance": self.balance}
    
class transaction_history:

    def __init__(self,  userId, balance, amount, date):
        self.userId = userId
        self.balance = balance
        self.amount = amount
        self.date = date