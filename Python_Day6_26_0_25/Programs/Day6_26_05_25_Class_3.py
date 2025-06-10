class Department:
    department_count = 0
    def __init__(self, dept_name, dept_id, hod, location):
        self.dept_name = dept_name
        self.dept_id = dept_id
        self.hod = hod
        self.location = location
        Department.department_count += 1
    def get_department_info(self):
        return {
            "Department Name": self.dept_name,
            "ID": self.dept_id,
            "HOD": self.hod,
            "Location": self.location
        }
    @classmethod
    def get_total_departments(cls):
        return cls.department_count
department_info_list = []
num_depts = int(input("Enter the number of departments: "))
for i in range(num_depts):
    print(f"\nEnter details for Department {i+1}:")
    name = input("Enter Department Name: ")
    dept_id = input("Enter Department ID: ")
    hod = input("Enter HOD Name: ")
    location = input("Enter Department Location: ")
    dept = Department(name, dept_id, hod, location)
    department_info_list.append(dept.get_department_info())
print("\n--- All Department Info Stored in List ---")
for dept_info in department_info_list:
    print(f"Department Name : {dept_info['Department Name']}")
    print(f"ID             : {dept_info['ID']}")
    print(f"HOD            : {dept_info['HOD']}")
    print(f"Location       : {dept_info['Location']}\n")
print(f"Total Departments in the Organization: {Department.get_total_departments()}")