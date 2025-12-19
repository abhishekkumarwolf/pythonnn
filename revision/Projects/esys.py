'''
Employee Management System
Develop an Employee Management System that models different types of employees in an organization.

Requirements
Base class: Employee
Child classes:
Engineer
Manager

Each employee should have:
ID
Name
Base salary

Salary calculation should differ for each role
 '''


class Emplyoee:

    def __init__(self, empId, base_salary):
        self.empId = empId
        self.base_salary = base_salary
 
     
    @staticmethod
    def attendence():
        return { "message : Attedence Submitted"}
    
    def cal_salary(self):
        return self.base_salary
    
    def display(self):
        print("\n Employee Details ")
        print(
            "\n Emplyoee Id :", self.empId,
            "\n NAme :", self.name,
            "\n Role :", self.department,
            "\n Degree: ", self.degree,
            "\nBase Salary :", self.base_salary,
            "\nFinal Salary: ", self.cal_salary()
        )   

class Engineer(Emplyoee):

    def __init__(self,empId, name,base_salary, degree, department):
        super().__init__(empId, base_salary)
        self.name = name
        self.degree = degree
        self.department = department
    
    
    def cal_salary(self):
        bonus = self.base_salary *0.30
        return self.base_salary + bonus

class Manager(Emplyoee):
    
    def __init__(self,empId, name,base_salary, degree, department):
        super().__init__(empId, base_salary)
        self.name = name
        self.degree = degree
        self.department = department
    
    
    def cal_salary(self):
        bonus = self.base_salary *0.60
        return self.base_salary + bonus
    

accounts = {}

def register_user():
    print("Employee Registration Portal:")

    name = input("Enter Your Name : ")
    empId = int(input("Enter Your Emplyoee ID : "))
    base_salary = int(input("Enter Your Base Salary :"))
    degree = input("Enter Your Qualification :")
    department = input("Enter Your Role :")


    if empId in accounts:
        print("User Already Exists")
        return None

    if department == "Engineer":
        user = Engineer(name, empId, base_salary, degree, "Engineer")
    elif department == "Manager":
        user = Manager(name, empId, base_salary, degree, "Manager")
    else:
        print("Invalid Position")
        return
        


    accounts[empId] = user
    print("Account Created")



def login():
    empId = int(input("Enter Your Employee ID to login :"))
    if empId in accounts:
        print("Login Successful :")
        return accounts[empId]
    else:
        print("Account Don't Exist")
        return None
    
    

register_user()
current_user = login()



if current_user:
    print("\nImformation about attendence :")
    current_user.attendence()
    current_user.display()
