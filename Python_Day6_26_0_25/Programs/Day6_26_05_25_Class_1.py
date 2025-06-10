class Employee:
    def __init__(self, name, salary):
        self.name = "Yasaswini"
        self.age = 21
        self.position = "Data Analyst"
    def display_employee_info(self):
        print("Employee information:\n-----------------------")
        print(f"Name: {self.name}\nAge: {self.age}\nPosition: {self.position}")
employee1 = Employee("Yasaswini", 10_00_000)
employee1.display_employee_info()