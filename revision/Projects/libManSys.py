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
import json

class Student():

    def __init__(self, stdId, name, contact, branch, year):
        self.stdId = stdId
        self.name = name
        self.contact = contact
        self.branch = branch
        self.year = year


    def to_dict(self):
        return{
            "stdId": self.stdId,
            "name": self.name,
            "contact": self.contact,
            "year": self.year,
            "branch": self.branch
        }


class Books():

    def __init__(self,bookId, bname,author):
        self.bookId = bookId,
        self.bname = bname
        self.author=author

    def check_presence(self, bname,author):
        with open("books.json", "r") as f:
            books = json.load(f)

        for bookId, books in books.items():
            if(books["name"].lower() == bname.lower() and
               books["author"].lower() == author.lower()):
                
                print("Book Avaiable")
                return bookId
            else:
                 print("Book not found")
                 return None
            
    def operation(self, current_user,  bname, author ,action ):

        if current_user is None:
            return "PLeasr login first to borrow or return"

        bookId = self.check_presence(bname, author)

        with open("books.json", "r")as f:
            books = json.load(f)

        bookId = str(bookId)


       #borrow 
        if action == "borrow":
            if books[bookId]["available"]:
                books[bookId]["available"] = False
                message = "Book borrowed successfully"

            else:
                return "Book already borrowed"
            
        #return
        elif action == "returnn":
            books[bookId]["available"] =True
            message = "Book returned successfully"

        else:
            return "Invalid action"
        
        with open("books.json","w") as f:
            json.dump(books, f, indent=4)

        return message



accounts = {}
def load_students():
    try:
        with open("student.json", "r") as f:
            data = json.load(f)

        for stdId, info in data.items():
            accounts[int(stdId)] = Student(
                info["stdId"],
                info["name"],
                info["contact"],
                info["year"],
                info["branch"]
            )

    except FileNotFoundError:
        pass


def save_students():
    data = {}
    for stdId, student in accounts.items():
        data[stdId] = student.to_dict()

    with open("student.json","w") as f:
        json.dump(data, f, indent=4)




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
    save_students()
    print("Account Created ")


def login():
     
     stdId = int(input("Enter the Student ID:"))

     if stdId in accounts:
         print("Login Successful :")
         return accounts[stdId]
     else:
         print("Account not Found")
         return None
     

#main functionality

load_students()
current_user = None
book_system = Books(0,"","")

while True:
    print("\n---Library System---")
    print(
        "\n1.Register",
        "\n2.Login",
        "\n3. Borrow Book",
        "\n4.Return Book",
        "\n5.Exit"
    )
    choice = input("Enter Choice")

    if choice == "1":
        registration()
        print("\n Please login to continue")
        current_user = login()

    elif choice == "2":
        current_user = login()

    elif choice == "3":
        if current_user == None:
            print("Please Login first")
            continue
        
        bname = input("Enter Book Name:")
        author = input("Enter Author Name:")
        
        print(book_system.operation(current_user, bname, author, "borrow"))

    elif choice == "4":
        if current_user == None:
            print("Please Login first")
            continue
            
        bname = input("Enter Book Name:")
        author = input("Enter Author Name:")
        
        
        print(book_system.operation(current_user, bname, author, "returnn"))

    elif choice == "5":
        print("Have A GOOD dAY")
        break
        
    else:
        print("Invalid Choice")

    
              
        
        
    
        
         