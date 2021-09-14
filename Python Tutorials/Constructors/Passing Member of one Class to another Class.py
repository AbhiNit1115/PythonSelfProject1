# Passing Member of one Class to another Class

class Employee:
    # Constructor
    def __init__(self, n, d):
        self.name = n
        self.dept = d

    def emp_details(self):  # Instance Method
        print("Employee Name is:", self.name)
        print("Employee Dept is:", self.dept)


# Create another class from which we want to access
class Company:
    @staticmethod  # create a static method post this create object of class which we want to access
    def company_emp(c):
        print("Company's Employee Name is:", c.name)  # accessing variables from class Employee
        print("Company's Dept name is:", c.dept)  # accessing variables from class Employee
        c.emp_details()  # accessing methods from class Employee


# Creating object of Employee class
emp = Employee("Abhi", "IT")  # create object of class
Company.company_emp(emp)  # pass the above created object(emp) as reference to static method of Company class
