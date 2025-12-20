import json

class Emplyoee:

    def __init__(self, empId, base_salary):
        self.empId = empId
        self.base_salary = base_salary

    def to_dict(self):
        return {
            "empId": self.empId,
            "name": self.name,
            "base_salary": self.base_salary,
            "degree": self.degree,
            "department": self.department
        }

    @staticmethod
    def attendence():
        return {"message": "Attendance Submitted"}

    def cal_salary(self):
        return self.base_salary

    def display(self):
        print("\nEmployee Details")
        print(
            "Employee Id:", self.empId,
            "\nName:", self.name,
            "\nRole:", self.department,
            "\nDegree:", self.degree,
            "\nBase Salary:", self.base_salary,
            "\nFinal Salary:", self.cal_salary()
        )


class Engineer(Emplyoee):

    def __init__(self, empId, name, base_salary, degree, department):
        super().__init__(empId, base_salary)
        self.name = name
        self.degree = degree
        self.department = department

    def cal_salary(self):
        return self.base_salary + (self.base_salary * 0.30)


class Manager(Emplyoee):

    def __init__(self, empId, name, base_salary, degree, department):
        super().__init__(empId, base_salary)
        self.name = name
        self.degree = degree
        self.department = department

    def cal_salary(self):
        return self.base_salary + (self.base_salary * 0.60)


accounts = {}


def save_to_json():
    data = {}
    for empId, user in accounts.items():
        data[empId] = user.to_dict()

    with open("employees.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Data saved to JSON")


def load_from_json():
    try:
        with open("employees.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return

    for empId, info in data.items():
        if info["department"] == "Engineer":
            user = Engineer(
                int(info["empId"]),
                info["name"],
                info["base_salary"],
                info["degree"],
                info["department"]
            )
        else:
            user = Manager(
                int(info["empId"]),
                info["name"],
                info["base_salary"],
                info["degree"],
                info["department"]
            )

        accounts[int(empId)] = user

    print("Data loaded from JSON")


def register_user():
    print("\nEmployee Registration Portal")

    name = input("Enter Name: ")
    empId = int(input("Enter Employee ID: "))
    base_salary = int(input("Enter Base Salary: "))
    degree = input("Enter Qualification: ")
    department = input("Enter Role (Engineer/Manager): ")

    if empId in accounts:
        print("User already exists")
        return

    if department == "Engineer":
        user = Engineer(empId, name, base_salary, degree, department)
    elif department == "Manager":
        user = Manager(empId, name, base_salary, degree, department)
    else:
        print("Invalid Role")
        return

    accounts[empId] = user
    save_to_json()
    print("Account created")


def login():
    empId = int(input("\nEnter Employee ID to login: "))
    if empId in accounts:
        print("Login successful")
        
        return accounts[empId]
    else:
        print("Account not found")
        return None



load_from_json()
register_user()
current_user = login()
current_user.attendence()


if current_user:
    current_user.attendence()
    current_user.display()
