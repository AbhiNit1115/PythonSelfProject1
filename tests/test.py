from copy import copy


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

list_1 = [1, 2, [3, 5], 4]
list_2 = copy(list_1)
list_2[3] = 7
list_2[2].append(6)

print(list_2)
print(list_1)

list1 = ["jhon", 23, (50, 60)]
