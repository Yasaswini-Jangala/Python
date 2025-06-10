# dict1 = {'key1' : 15, 'key2' : [1, 2, 3, 4, 5], 'key3' : 'Mango'}
# print(f'dict1["key3"] -> {dict1['key3']}')
# print(f'dict1["key2"] -> {dict1['key2']}')
# print(f'dict1["key2"][0] -> {dict1['key2'][0]}')
# for key in dict1.keys():
#   print(key)
# for key in dict1.keys():
#   print(f'{key} : {dict1[key]}')
# keys_list = dict1.keys()
# values_list = dict1.values()
# items_list = dict1.items()
# print(keys_list)
# print(values_list)
# print(items_list)

# dict2 = {}
# print(f'type(dict2) -> {type(dict2)}')
# print(f'dict2 -> {dict2}')
# dict2['Key1'] = 1
# dict2['Key2'] = [5, 10, 15, 20, 25]
# dict2['Key3'] = 'Yasaswini'
# print(f'dict2 -> {dict2}')
# print(f'type(dict2) -> {type(dict2)}')

# products = ["Laptop", "Phone", "Tablet"]
# for index, item in enumerate(products):
#   print(f'index {index}, item {item}')
# print()
# for index, item in enumerate(products):
#   print(f'index {index+1}, item {item}')

# alphas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# for index, alpha in enumerate(alphas, start = 415):
#   print(f'{index} : {alpha}')

# students = {
#   415 : {"Name" : "Yasaswini", "Branch" : "ECE", "CGPA" : 7.4},
#   414 : {"Name" : "Alice", "Branch" : "CSE", "CGPA" : 7.0},
#   416 : {"Name" : "Bob", "Branch" : "IT", "CGPA" : 6.5},
#   417 : {"Name" : "Charlie", "Branch" : "AIML", "CGPA" : 6.0}
# }
# print(students)
# print()
# students[418] = {"Name" : "Enna", "Branch" : "EEE", "CGPA" : 7.0}
# print(students)
# print()
# students[415]["CGPA"] = 8.0
# print(students)
# print()
# del students[416]
# del students[414]["Branch"]
# # del students[420] -> Error as 420 is not present
# print(students)
# print()
# if "419" not in students:
#   students.setdefault("419", {"Name" : "David", "Branch" : "ECE", "CGPA" : 6.5})
# print(students)
# print()
# for student_id, student_info in students.items():
#   print(f'Student ID: {student_id}')
#   for key, value in student_info.items():
#     print(f'  {key}: {value}')
#   print()

# students_dictionary = students.copy()
# print(f'students_dictionary ->\n{students_dictionary}')
# print()

# no_of_Employees = int(input("Enter the number of Employees: "))
# employees = {}
# for i in range(no_of_Employees):
#   print(f"-------------------------------\nEnter the Details of Employee {i+1}\n------------------------------- ")
#   emp_id = input("  Enter the Employee ID: ")
#   emp_name = input("  Enter the Employee Name: ")
#   emp_salary = input("  Enter the Employee Salary: ")
#   emp_location = input("  Enter the Employee Loction: ")
#   emp_department = input("  Enter the Employee Department: ")
#   emp_gender = input("  Enter the Employee Gender: ")
#   employees[emp_id] = {"Name" : emp_name, "Salary" : emp_salary, "Location" : emp_location, "Department" : emp_department, "Gender" : emp_gender}
#   print()
# # for employee_id, employee_info in employees.items():
# #   print(f'Employee ID: {employee_id}')
# #   for key, value in employee_info.items():
# #     print(f'  {key}: {value}')
# #   print()
# print("Employee Details:")
# # for index, (employee_id, employee_info) in enumerate(employees.items(), start=1):
# #   print(f"----------------------\nDetails of Employee {index}\n----------------------")
# #   print(f'Employee ID: {employee_id}')
# #   print(f'  Name: {employee_info["Name"]}')
# #   print(f'  Sakary: {employee_info["Salary"]}')
# #   print(f'  Location: {employee_info["Location"]}')
# #   print(f'  Department: {employee_info["Department"]}')
# #   print(f'  Gender: {employee_info["Gender"]}')
# #   print()

# my_dict = {"a": 1, "b": 2}
# print(iter(my_dict))           # <dict_keyiterator object at memory_address> — iterates over keys
# print(iter(my_dict.keys()))    # <dict_keyiterator object at memory_address> — same as above, iterates over keys
# print(iter(my_dict.values()))  # <dict_valueiterator object at memory_address> — iterates over values
# print(iter(my_dict.items()))   # <dict_itemiterator object at memory_address> — iterates over (key, value) pairs

# no_of_Employees = int(input("Enter the number of employees: "))
# for i in range(no_of_Employees):
#   emp_id = input("Enter employee ID: ")
#   emp_name = input("Enter employee name: ")
#   emp_salary = float(input("Enter employee salary: "))
#   emp_location = input("Enter employee location: ")
#   emp_department = input("Enter employee department: ")
#   emp_gender = input(" Enter employee  gender")
#   employees[emp_id] = {"name": emp_name, "salary": emp_salary,"location": emp_location, "department": emp_department,"gender": emp_gender} 
# print("\nEmployee Details:")
# for emp_id, emp_info in employees.items():
#   print(f"Employee ID: {emp_id}")
#   print(f" \n Name: {emp_info['name']}\t Salary: {emp_info['salary']}\t Location: {emp_info['location']}\t Department: {emp_info['department']}\t Gender: {emp_info['gender']}  ")
#   print()

# employees = {
#   "A1" : {"Name" : "Yasaswini", "Department" : "Testing", "Location" : "Hyderabad", "Gender" : "Female", "Salary" : 2_00_000},
#   "A2" : {"Name" : "Alice", "Department" : "Testing", "Location" : "Chennai", "Gender" : "Male", "Salary" : 1_75_000},
#   "A3" : {"Name" : "Bob", "Department" : "Data Analyst", "Location" : "Pune", "Gender" : "Other", "Salary" : 1_50_000},
#   "A4" : {"Name" : "Charlie", "Department" : "Data Analyst", "Location" : "Hyderabad", "Gender" : "Other", "Salary" : 1_25_000},
#   "A5" : {"Name" : "David", "Department" : "Testing", "Location" : "Pune", "Gender" : "Male", "Salary" : 2_00_000}, 
#   "A6" : {"Name" : "Ethana", "Department" : "Developer", "Location" : "Pune", "Gender" : "Female", "Salary" : 1_00_000},
#   "A7" : {"Name" : "Famina", "Department" : "Developer", "Location" : "Chennai",  "Gender" : "Other", "Salary" : 1_50_000},
#   "A8" : {"Name" : "George", "Department" : "Developer", "Location" : "Hyderabad",  "Gender" : "Male", "Salary" : 2_00_000},
#   "A9" : {"Name" : "Hema", "Department" : "Testing", "Location" : "Hyderabad",  "Gender" : "Female", "Salary" : 1_50_000},
#   "A10" : {"Name" : "Iyana", "Department" : "Testing", "Location" : "Chennai",  "Gender" : "Other", "Salary" : 1_75_000},
#   "A11" : {"Name" : "Jyothi", "Department" : "Data Analyst", "Location" : "Banglore",  "Gender" : "Female", "Salary" : 1_50_000},
#   "A12" : {"Name" : "Kaira", "Department" : "Testing", "Location" : "Banglore",  "Gender" : "Female", "Salary" : 1_25_000},
#   "A13" : {"Name" : "Lara", "Department" : "Testing", "Location" : "Hyderabad",  "Gender" : "Female", "Salary" : 1_00_000},
#   "A14" : {"Name" : "Misha", "Department" : "Developer", "Location" : "Hyderabad",  "Gender" : "Female", "Salary" : 1_00_000},
#   "A15" : {"Name" : "Nadia", "Department" : "Testing", "Location" : "Hyderabad",  "Gender" : "Female", "Salary" : 1_75_000}
# }

# # Find the Number of employees in each department
# print()
# print("Find the Number of Employees in each Department")
# department_count = {} # dictionary
# for emp_info in employees.values():
#   department = emp_info["Department"]
#   if department in department_count:
#     department_count[department] += 1
#   else:
#      department_count[department] = 1
# print("\nNumber of Employees in each Department:")
# for department, count in department_count.items():
#  print(f"  {department}: {count} Employee(s)") 

# # Find the total number of male and female employees.
# print()
# print("Find the total number of Male and Female employees.")
# gender_count = {"Male": 0, "Female": 0, "Other": 0}
# for emp_info in employees.values():
#     gender = emp_info["Gender"].capitalize()
#     if gender in gender_count:
#         gender_count[gender] += 1
#     else:
#         gender_count["Other"] += 1
# print("\nGender-Wise Employee Count:")
# for gender, count in gender_count.items():
#   print(f"  {gender}: {count}")

# # Find the total number employees in each location
# print()
# print("Find the Total Number of Employees in each Location")
# location_count = {}
# for emp_info in employees.values():
#   loc = emp_info["Location"]
#   location_count[loc] = location_count.get(loc, 0) + 1
# print("\nEmployees Count per Location:")
# for location, count in location_count.items():
#   print(f"  {location}: {count}")

# # Calculate the Average Salary of Employees in each Department.
# print()
# print("Calculate the Average Salary of Employees in each Department")
# dept_salary = {}
# dept_count = {}
# for emp_info in employees.values():
#   dept = emp_info["Department"]
#   dept_salary[dept] = dept_salary.get(dept, 0) + emp_info["Salary"]
#   dept_count[dept] = dept_count.get(dept, 0) + 1
# print("\nAverage Salary per Department:")
# for dept in dept_salary:
#   avg_salary = dept_salary[dept] / dept_count[dept]
#   print(f"  {dept}: ₹{avg_salary:.2f}")

# # List all Employees in a given Department.
# print()
# print("List all Employees in a given Department")
# search_dept = input("Enter department name to search: ")
# found = False
# print(f"\nEmployees in {search_dept} Department:")
# for emp_info in employees.values():
#   if emp_info["Department"].lower() == search_dept.lower():
#     print(f"  {emp_info['Name']}")
#     found = True
# if not found:
#     print("  No Employees found in this Department.")

# # Show the Employee with the Highest Salary.
# print()
# print("Show the Employee with the Highest Salary")
# max_salary = -1
# top_employee = None
# for emp_id, emp_info in employees.items():
#   if emp_info["Salary"] > max_salary:
#     max_salary = emp_info["Salary"]
#     top_employee = (emp_id, emp_info)
# if top_employee:
#     print(f"\nHighest Paid Employee:\n  ID: {top_employee[0]}")
#     print(f"  Name: {top_employee[1]['Name']}, Salary: ₹{top_employee[1]['Salary']}")

# # Display Employees sorted by Salary in Descending Order.
# print()
# print("Display Employees sorted by Salary in Descending Order")
# print("\nEmployees sorted by salary (high to low):")
# sorted_emps = sorted(employees.items(), key=lambda item: item[1]['Salary'], reverse=True)
# for emp_id, emp_info in sorted_emps:
#   print(f"  {emp_info['Name']} - ₹{emp_info['Salary']}")

# # Display Employees sorted by Salary in Ascending Order.
# print()
# print("Display Employees sorted by Salary in Ascending Order")
# print("\nEmployees sorted by salary (high to low):")
# sorted_emps = sorted(employees.items(), key=lambda item: item[1]['Salary'])
# for emp_id, emp_info in sorted_emps:
#   print(f"  {emp_info['Name']} - ₹{emp_info['Salary']}")