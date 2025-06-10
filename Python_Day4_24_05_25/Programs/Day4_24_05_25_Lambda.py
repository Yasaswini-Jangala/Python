# add_10 = lambda x : x+10
# x = int(input("Enter a value to add 10: "))
# print(add_10(x))

# multiply = lambda x, y : x * y
# x, y = map(int, input("Enter 2 numbers to perform Multiplication: ").split())
# print(multiply(x, y))

# check_even = lambda x : "Even" if x % 2 == 0 else "Odd"
# x = int(input("Enter a number to check whether it is Odd or Even: "))
# print(check_even(x))

# numbers = [1, 2, 3, 4, 5]
# y = int(input("Enter a number to Multiply with the values in the list: "))
# result = map(lambda x : x * y, numbers)
# print(list(result))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = int(input("Enter a number to check if it is greater than the values in the list: "))
# result = filter(lambda x : x > y, numbers)
# print(list(result))

# people = [('Alice', 30), ('Bob', 40), ('Charlie', 50)]
# sorted_people = sorted(people, key = lambda person : person[1])
# print(sorted_people)

# people = [('Alice', 30), ('Bob', 40), ('Charlie', 50)]
# print('\n'.join(f'{name}, {age}' for name, age in sorted(people, key=lambda p: p[1])))

# employees = [
#   {'name' : 'Alice', 'salary' : 50000},
#   {'name' : 'Bob', 'salary' : 45000},
#   {'name' : 'Enna', 'salary' : 50000},
#   {'name' : 'Fiona', 'salary' : 60000},
#   {'name' : 'David', 'salary' : 30000},
#   {'name' : 'Charlie', 'salary' : 45000}
# ]
# sorted_employees = sorted(employees, key = lambda x : (x['salary'], x['name']))
# print(sorted_employees)

# sorted_employees = sorted(employees, key = lambda x : (-x['salary'], x['name']))
# print(sorted_employees)

# # sorted_employees = sorted(employees, key = lambda x : (x['salary'], -x['name']))
# # print(sorted_employees) # Error, String cannot be ordered in descending order.