class Employee:
    employee_count = 0
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
        Employee.employee_count += 1
    def display_employee_info(self):
        print("Employee information:\n-----------------------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Position: {self.position}")
    @classmethod
    def get_total_employees(cls):
        return cls.employee_count
employee1 = Employee("Yasaswini", 21, "Senior Data Analyst")
employee1.display_employee_info()
employee2 = Employee("Amber", 30, "Junior Data Analyst")
employee2.display_employee_info()
print(f"Total Employees: {Employee.get_total_employees()}")