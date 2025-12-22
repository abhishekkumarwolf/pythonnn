'''
 Library Management System

Build a Library Management System to manage books and borrowing operations.

Library should:
Store list of books
Track issued and available books

Members should:
Borrow books
Return books
Prevent issuing unavailable books

OOP Concepts:
Object interaction
Composition
Encapsulation

'''

class Student():

    def __init__(self, stdId, name, contact, branch, year):
        self.stdId = stdId
        self.name = name
        self.contact = contact
        self.branch = branch
        self.year = year


class Books():

    def __init__(self,bookId, name):
        self.bookId = bookId,
        self.name = name



accounts = {}

def registration():

    print("----Library Registration----\n ")
    stdId = int(input("Enter Your Student ID :"))
    name = input("Enter Your Name:")
    contact = input("Enter Your Phone Number: ")
    Year = int(input("Enter Your Passing Year :"))
    branch = input("Enter Your Branch Name :")
    

    if stdId in accounts:
        print("User Already Exist")
        return
    
    user = Student(stdId, name, contact, Year, branch)
    accounts[stdId] = user
    print("Account Created ")


def login():
     
     stdId = int(input("Enter the Student ID:"))

     if stdId in accounts:
         print("Login Successful :")
         return accounts[stdId]
     else:
         print("Account not Found")
         return None
         