'''
Student Management System

Create a Student Management System to store and manage student academic information.

Each student must have:
Student ID
Name
Marks in multiple subjects

System should:
Calculate total and average marks
Assign grades
Display student report

'''
class Students:

    def __init__(self, stdId, name,marks):
        self.stdId = stdId
        self.name = name
        self.marks =marks

 
    def assign_grades(self): 
        print("\n-- Student :", self.name, " Grades obtained--")
        for m in self.marks:

            if m >90:
                grade1 = "A"
                
            elif m >80:
                grade1 = "B"
                
            elif m >70:
                grade1 = "C"
                
            elif m >60:
                grade1 = "D"
            else:
                grade1 = "Failed"  
            print("Mark:", m," ->", grade1)

    
    def total(self):
        sum1 = 0
        for i in self.marks:
            sum1 += i
        return sum1
    
    def average(self):
        avg = self.total()/3
        return avg
    
    def display(self):
        print("Student Name :", self.name)
        print("Total :", self.total())
        print("Average : ", self.average())



accounts ={}

def register_user():
    print("New USer Registration :")
    name = input("Enter your name: ")
    stdId = int(input("Enter your Student id: "))
    marks = []

    for i in range(3):
        mark = int(input(f"Enter marks {i+1} :"))
        marks.append(mark)
    

    if stdId in accounts:
        print("Already Existed ")
        return
    
    user = Students(name, stdId, marks)
    accounts[stdId] = user
    print("Account created ")


def login():
    stdId = int(input("Enter Student Id to login :"))
    if stdId in accounts:
        print("\nLogin Succesful ")
        return accounts[stdId]
    else:
        print("Account not found")
        return None
    

register_user()
current_user = login()


if current_user:
        print("\n\n---Student Academic Record --")
        current_user.display()
        current_user.assign_grades()
else:
    print("Record not found")

        
    





