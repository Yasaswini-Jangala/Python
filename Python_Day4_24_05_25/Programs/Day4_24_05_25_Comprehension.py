# # List Comprehension -> # Print the Names of the Active Users
# users = [('Alice', True), ('Bob', False), ('Charlie', True), ('David', False), ('Enna', True), ('Famina', True), ('George', False), ('Hema', True)]
# print('\n'.join(name for name, status in users if status))

# # Tuple Comprehension -> # UpperCasing the Product Codes
# product_codes = ["abc123", "xyz456", "ijk789", "code0", "code1", "code2", "code3"]
# print('\n'.join(tuple(code.upper() for code in product_codes)))

# # Dictionary Comprehension -> # Print Names of Students who got Marks >= 85
# marks = {'Alice' : 70, 'Bob' : 72,'Charlie' : 74, 'David' : 76, 'Enna' : 78, 'Famina' : 80, 'George' : 82, 'Hema' : 84, 'Iyan' : 86, 'Jack' : 88, 'Kimon' : 90, 'Lara' : 92, 'Misha' : 94, 'Nadia' : 96, 'Oman' : 98}
# print('\n'.join({name: score for name, score in marks.items() if score >= 85}))

# # Set Comprehension -> # Extracting Unique Department Names
# employees = [('Alice', 'Support'), ('Bob', 'HR'), ('Charlie', 'IT'), ('David', 'Finance'), ('Enna', 'IT'), ('Famina', 'Finance'), ('George', 'IT'), ('Hema', 'Finance'), ('Iyana', 'Support'), ('James', 'IT'), ('Kiara', 'IT'), ('Lara', 'Finance'), ('Misha', ''), ('Nadia', 'IT'), ('Oman', 'Support')]
# print('\n'.join({dept for _, dept in employees}))