class Employee:

    def __init__(self, n, d):
        self.name = n
        self.dept = d

    def emp_details(self):
        print("Employee Name is:", self.name)
        print("Employee Dept is:", self.dept)


class Company:
    @staticmethod
    def company_emp(c):
        print("Company's Employee Name is:", c.name)
        print("Company's Dept name is:", c.dept)
        c.emp_details()


emp = Employee("Jhon", "IT")
Company.company_emp(emp)
