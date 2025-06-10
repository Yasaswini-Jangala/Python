with open("sample.txt", "w") as file:
    file.write("This is the initial content.\n")
with open("sample.txt", "a+") as file:
    file.write("This is the appended content.\n")
    file.seek(0)
    print(file.read())