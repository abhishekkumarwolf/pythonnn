

class Student :
    college_name = " Heritage Institute of techmology"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1  = Student("Abhishek", 34 )

#create student class that takes name and marks of 3 sybject
#as arguments in constructors, then create a method to print
#the average


class Students:

    def __init__(self,name, mark1, mark2, mark3):
        self.name = name
        self.mark1 =mark1
        self.mark2 =mark2
        self.mark3 =mark3


    def get_avg(self):
        sum = self.mark1 + self.mark2 + self.mark3
        return sum/3
    




s1 = Students("Abhishek", 90, 89 ,96 )

#Abstraction
#Hiding the implementation details of a class and only showing the essential features to users

class Cars:
    def __init__(self):
        self.acc =False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.brk = True
        self.cluth = True

        print("Car has started")

car1 = Cars()


#Encapsulation
#Wrapping data and function into a single unit(object)

'''
Create Acoount class with 2 attributes - balance and account no
create methods for debit, credit and printing the balance
'''
class Account:

    def __init__(self , accno, bal ):
        self.accno = accno
        self.bal = bal

    def credit(self , amount):
        self.bal += amount
        print("Credied Amount ", amount)
        
    def debit(self , amount):
        self.bal -= amount
        print("Deducted Amount :", amount)
    
    def balance(self):
        print("Your Bank Balance: ", self.bal)

user1 = Account( 1234, 1000)
user1.credit(5000)
user1.debit(200)


#Inheritance

class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")

class ToyotaCar(Car):

    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("prius")

'''
Define a circle class to create a circle with radius r using
the constructor, Define an Area() method of the class which calculate
the area of the circle same to perimeter
'''

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius**2
    
    def perimeter(self):
        return 2*3.14*self.radius
    
circle1 = Circle(22)

'''
Define a Employee class with attributes role department and salary
this class has also showdetails() method

create an Engineer classs that inherits the prperties from employee
and has additional attributes age and gender
'''


class Employees:

    def __init__(self,name, role, department, salary):
        self.name = name
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print(
              "Name : ",self.name,
              "\nRole :", self.role,
              "\nDepartment : ",self.department,
              "\nSalary :",self.salary
              )
        
class Engineer(Employees):

    def __init__( self, name, role, department, salary, gender, age ):
        super().__init__(name, role, department, salary)
        self.gender = gender
        self.age = age
        

    def showDetails(self):
        super().showDetails()
        print(
            "Gender:", self.gender,
            "\nAge: ", self.age   

        )     

    


emp1 = Employees("Mohan", "SDE", "none", "30,000" )
emp2 = Engineer("Abhishek", "Data Sceinctist", "none", "70,000" ,"male","21") 
emp2.showDetails()
emp1.showDetails()
        