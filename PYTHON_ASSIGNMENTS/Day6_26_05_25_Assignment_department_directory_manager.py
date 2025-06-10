class Department:
    dept_count = 0
    def __init__(self, dept_id, name, hod, location):
        self.dept_id = dept_id
        self.name = name
        self.hod = hod
        self.location = location
        Department.dept_count += 1
    def display(self):
        print(f"ID: {self.dept_id}  |  Name: {self.name}  |  HOD: {self.hod}  |  Location: {self.location}")
    @classmethod
    def display_total(cls):
        print(f"\nTotal departments in the organisation: {cls.dept_count}\n")
num_depts = int(input("How many departments? "))
departments = []
for i in range(1, num_depts + 1):
    print(f"\nEnter details for department {i}:")
    dept_id = input("  ID: ")
    name = input("  Name: ")
    hod = input("  Head of Department: ")
    location = input("  Location: ")
    dept_obj = Department(dept_id, name, hod, location)
    departments.append(dept_obj)
print("\n──── Department Directory ────")
for dep in departments:
    dep.display()
Department.display_total()