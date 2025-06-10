# # Reading the entire file content with read()
# with open('FileHandling_Read.txt') as f:
#     content = f.read()
#     print(content)

# # Reading the file line-by-line with readline()
# with open('FileHandling_Read.txt') as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print(line)

# # Reading the file line-by-line with readline() and stripping the newline
# with open('FileHandling_Read.txt') as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print(line.strip())

# # Reading all lines at once with readlines()
# with open('FileHandling_Read.txt') as f:
#     for line in f.readlines():
#         print(line)

# # Reading all lines and stripping newlines with readlines()
# with open('FileHandling_Read.txt') as f:
#     for line in f.readlines():
#         print(line.strip())

# # Writing to a file with write()
# with open('FileHandling_Write.txt', 'w') as f:
#     f.write("Hello, this is a line.\n")
#     f.write("Zeroth line.\n")

# # Writing multiple lines with writelines()
# lines = ["First line\n", "Second line\n", "Third line\n"]
# with open('FileHandling_Write.txt', 'w') as f:
#     f.writelines(lines)

# # Appending a single line to an existing file
# with open('FileHandling_Write.txt', 'a') as f:
#     f.write("This line is appended.\n")

# # Appending multiple lines with writelines()
# more_lines = ["Appending fourth line\n", "Appending fifth line\n"]
# with open('FileHandling_Write.txt', 'a') as f:
#     f.writelines(more_lines)

# # 'w+' mode: write and read, truncates the file if it exists
# with open('example_wplus.txt', 'w+') as f:
#     f.write("Line 1\n")
#     f.write("Line 2\n")
#     f.seek(0)
#     print("w+ mode content:")
#     print(f.read())

# # 'r+' mode: read and write, file must exist
# with open('example_rplus.txt', 'w') as f:
#     f.write("Original line\n")

# # 'r+' mode: read and write, file must exist. It does not truncate the file.
# with open('example_rplus.txt', 'r+') as f:
#     print("r+ mode before writing:")
#     print(f.read())
#     f.seek(0)
#     f.write("Modified line\n")
#     f.seek(0)
#     print("r+ mode after writing:")
#     print(f.read())

# # 'a+' mode: read and append, creates file if it doesn't exist
# with open('example_aplus.txt', 'a+') as f:
#     f.write("Appended line 1\n")
#     f.write("Appended line 2\n")
#     f.seek(0)
#     print("a+ mode content:")
#     print(f.read())

# from os.path import exists
# print(exists('test_file_0.txt'))
# print(exists('test_file_00.txt'))

# from pathlib import Path
# print(Path('test_file_0.txt').is_file())
# print(Path('test_file_00.txt').is_file())

# from os.path import exists
# print(exists('test_file_1.txt'))
# print(exists('test_file_01.txt'))

# from pathlib import Path
# print(Path('test_file_1.txt').is_file())
# print(Path('test_file_01.txt').is_file())

# from pathlib import Path
# print(Path('C:\\Users\\admin\\Desktop\\ALL FILES\\CapgeminiTraining\\Python\\Python_Day6_26_0_25\\Python_Day6_26_05_25.txt').is_file())
# print(Path('C:\\Users\\admin\\Desktop\\ALL FILES\\CapgeminiTraining\\Python\\Python_Day6_26_0_25').is_file())

# # Read CSV content
# import csv
# with open('C:\\Users\\admin\\Desktop\\ALL FILES\\CapgeminiTraining\\Python\\Python_Day7_27_05_25\\Programs\\Predictions.csv', encoding = 'utf-8') as f:
#   reader = csv.reader(f)
#   for line in reader:
#     print(line)

# import csv
# with open('C:\\Users\\admin\\Desktop\\ALL FILES\\CapgeminiTraining\\Python\\Python_Day7_27_05_25\\Programs\\Predictions.csv', 'r') as f:
#   csv_reader = csv.reader(f)
#   for line_no, line in enumerate(csv_reader, 1):
#     if line_no == 1:
#       print("HEADER")
#       print(line)
#       print("RECORDS")
#     else:
#       print(line)

# import csv
# with open('C:\\Users\\admin\\Desktop\\ALL FILES\\CapgeminiTraining\\Python\\Python_Day7_27_05_25\\Programs\\country.csv', 'r') as f:
#   csv_reader = csv.reader(f)
#   total_area = 0
#   next(csv_reader)
#   for line in csv_reader:
#     total_area += float(line[1])
#   print(f"Total Area: {total_area}")

# import csv
# with open('C:\\Users\\admin\\Desktop\\ALL FILES\\CapgeminiTraining\\Python\\Python_Day7_27_05_25\\Programs\\country.csv', 'w') as f:
#   writer = csv.writer(f)
#   writer.writerow(['Country', 'Area', 'Population'])
#   writer.writerow(['Country0', '1234560', '123456780'])

# import csv
# with open('C:\\Users\\admin\\Desktop\\ALL FILES\\CapgeminiTraining\\Python\\Python_Day7_27_05_25\\Programs\\country_writer.csv', 'w', newline='') as f:
#   writer = csv.writer(f)
#   data = [
#     ['Country', 'Area', 'Population'],
#     ['Country1', '1234567', '123456789'],
#     ['Country2','7654321', '987654321'],
#     ['Country3','1357911', '135791113'],
#     ['Country4','2468100', '246810120']
#   ] 
#   writer.writerows(data)

# import csv
# field_names = ['Country', 'Area', 'Population'] 
# data = [
#     {'Country': 'Country1', 'Area': '1234567', 'Population': '123456789'},
#     {'Country': 'Country2', 'Area': '7654321', 'Population': '987654321'},
#     {'Country': 'Country3', 'Area': '1357911', 'Population': '135791113'},
#     {'Country': 'Country4', 'Area': '2468100', 'Population': '246810120'},
#     {'Country': 'Country5', 'Area': '2468100', 'Population': '246810120'},
#     {'Country': 'Country6', 'Area': '4812160', 'Population': '481216200'}
# ]
# with open('C:\\Users\\admin\\Desktop\\ALL FILES\\CapgeminiTraining\\Python\\Python_Day7_27_05_25\\Programs\\country.csv', 'w+', newline='') as f:
#   writer = csv.DictWriter(f, fieldnames=field_names)
#   writer.writeheader()
#   writer.writerows(data)
#   f.seek(0)
#   print("Content of country.csv")
#   print(f.read())

# import os
# print(f"\nos.listdir('.') -> \n{'\n'.join(os.listdir('.'))}")
# print(f"\nos.getcwd() -> \n{os.getcwd()}")
# print(f'\nos.chdir("..") -> \n{os.chdir("..")}\n')
# print(f"\nos.getcwd() -> \n{os.getcwd()}")
# print(f"\nos.listdir('.') -> \n{'\n'.join(os.listdir('.'))}")
# with open("new_file.txt", "w") as f:
#     f.write("Hello from Python")
# if os.path.exists("new_file.txt"):
#     print("newfile.txt exists")
# os.rename("Programs\\test_file.txt", "renamed_test_file.txt")