'''
Design a Bank Account Management System using Object-Oriented Programming concepts.
The system should allow users to create bank accounts, perform transactions, and check balances securely.

Prevent withdrawal if balance is insufficient
'''
class Bank_account:

    def __init__(self, name, accno, bal):

        self.name = name
        self.accno = accno
        self.bal = bal
                

                
    def credit(self, amount):
        self.bal += amount
        print("\nMoney Credited :", amount, "\nBank Balance :", self.bal)



    def debit(self, amount):

        if amount < 0:
            print("Invalid Amount: ")
    
        elif  amount > self.bal:
            print("Insufficient Balance..")
    
        else:
            self.bal -= amount
            print("\nMoney Debited :", amount)




    def show_details(self):
        print("\nName : ", self.name)
        print("Account Number: ", self.accno)
        print("Bank Balance :",self.bal)



accounts ={}

def register_user():
    name = input("Enter Your name: ")
    accno = int(input("Enter Your Account Number :"))

    if accno in accounts:
        print("User Already Existed: ")
        return
    
    user = Bank_account(name, accno,0)
    accounts[accno] = user
    print("Account created :")

def login():
    accno = int(input("Enter the Account numbe to login :"))
    if accno in accounts:
        print("Login Succesful: ")
        return accounts[accno]
    else:
        print("Account not Found: ")
        return None
    




register_user()
current_user = login()

if current_user:
    while True:
        print("\n----Bank Menu----")
        print("1. Deposit ")
        print("2. Credit ")
        print("3. Check Balance ")
        print("4. Logout ")

        choice = int(input("Choose Option :"))

        if choice == 1:
            amt = int(input("Enter the amount to Depoist"))
            current_user.debit(amt)

        elif choice == 2:
            amt = int(input("Enter the amount to Credit"))
            current_user.credit(amt)

        elif choice == 3:
            print("Balance Details")
            current_user.show_details()

        elif choice == 4:
            print("Logout successful")
            break
        else:
            print("Invalid Choice")

    



    
