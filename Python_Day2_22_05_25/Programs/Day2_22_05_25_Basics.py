# # Ctrl / -> for single line comments in Python

# print(10+5)
# print(10*5)
# print(10**5)
# print(10/5)
# print(10//5)

# income = 50000
# tax_rate = 0.5
# tax = income * tax_rate
# print(f"Your tax is {int(tax)}")

# company = 'CAPGEMINI'
# print(f'Company -> {company}')
# print(f'Company[0] -> {company[0]}')
# print(f'Company[5] -> {company[5]}')
# print(f'Company[0:3] -> {company[0:3]}')
# print(f'Company[:3] -> {company[:3]}')
# print(f'Company[3:] -> {company[3:]}')
# print(f'Company[3:6] -> {company[3:6]}')
# print(f'Company[::-1] -> {company[::-1]}')
# print(f'Company[::2] -> {company[::2]}')

# company += ' INDIA'
# print(f'Upper -> {company.upper()}')
# print(f'Lower -> {company.lower()}')
# print(f'Title -> {company.title()}')
# print(f'Capitalize -> {company.capitalize()}')

# str1 = "Hello", "Capgemini", "This", "is", "Yasaswini", "from", "Capgemini", "in", "Hyderabad"
# str2 = "Hello_", "Capgemini_", "This_", "is_", "Yasaswini_", "from_", "Capgemini_", "in_", "Hyderabad_"
# print(f"type(str1) -> {type(str1)}") 
# print(f"str1 -> {str1}")
# print(f"' '.join(str1) -> {' '.join(str1)}")
# print(f"'_'.join(str1) -> {'_'.join(str1)}")
# print(f"' '.join(str1).split() -> {' '.join(str1).split()}") 
# print(f"'_'.join(str1).split() -> {'_'.join(str1).split()}")
# print()
# print(f"type(str2) -> {type(str2)}") 
# print(f"str2 -> {str2}")
# print(f"' '.join(str2) -> {' '.join(str2)}") 
# print(f"'_'.join(str2) -> {'_'.join(str2)}") 
# print(f"' '.join(str2).split() -> {' '.join(str2).split()}") 
# print(f"'_'.join(str2).split() -> {'_'.join(str2).split()}") 

# print(f"'APPLES ' * 5 -> {'APPLES ' * 5}")
# print(f"'APPLES ' * 5 + 'ARE ' * 5 + 'SWEET ' * 5 -> {'APPLES ' * 5 + 'ARE ' * 5 + 'SWEET ' * 5}")
# print(f"'APPLES ' * -5 -> {'APPLES ' * -5}")

# print("I am going to insert %s here" %'the text')
# x,y='some text', 'other text'
# print("I am going to insert %s here and the %s here" %(x, y))
# print("I am going to insert %s here and the %s here" %('some part of the text', 'other part of the text'))

# print("Floating point numbers: (%f) %%1.0f -> %1.0f" % (151515.151515, 151515.151515))
# print("Floating point numbers: (%f) %%5.5f ->  %5.5f  " % (151515.151512, 151515.15151215))
# print("Floating point numbers: (%f) %%5.5f ->  %5.5f  " % (151515.151515, 151515.15151515))
# print("Floating point numbers: (%f) %%5.5f  ->  %5.5f  " % (151515.151517, 151515.15151715))
# print("Floating point numbers: (%f) %%3.5f -> %3.5f " % (151515.151515, 151515.151515))
# print("Floating point numbers: (%f) %%7.5f  ->  %7.5f  " % (151515.151515, 151515.15151515))
# print(len("Floating point numbers: (%f) %%1.0f -> %1.0f " % (151515.151515, 151515.151515)))
# print(len("Floating point numbers:(%f) %%5.5f ->  %5.5f " % (151515.151515, 151515.151515)))
# print(len("Floating point numbers: (%f) %%5.5f -> %5.5f " % (151515.151515, 151515.151515)))

# print("%10.2f" % 12.34) #      12.34
# print("%7.2f" % 12.34) #   12.34
# print("%5.2f" % 12.34) # 12.34
# print("%3.2f" % 12.34) # 12.34

# print('{0:9} | {1:10}'.format('Fruit', 'Quantity'))
# print('{0:9} | {1:10}'.format('Mango', 15))
# print('{0:9} | {1:10}'.format('Sapota', 10))
# print('{0:9} | {1:10}'.format('Apple', 5))
# print()
# print('{0:<9} | {1:^10} | {2:>10}'.format('Left', 'Center', 'Rght'))
# print('{0:<9} | {1:^10} | {2:>10}'.format(5, 10, 15 ))