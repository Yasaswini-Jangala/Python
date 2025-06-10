# print("\033[90mThis is gray text\033[0m")
# print("\033[91mThis is red text\033[0m")
# print("\033[92mThis is green text\033[0m")
# print("\033[93mThis is yellow text\033[0m")
# print("\033[94mThis is dark blue text\033[0m")
# print("\033[95mThis is pink text\033[0m")
# print("\033[96mThis is sky blue text\033[0m")

# command = ""
# while command.lower() != "quit":
#   command = input("Give a Command: ")
#   if command.lower() == "start":
#     print("Car Started.....")
#   elif command.lower() == "stop":
#     print("Car Stopped.")
#   elif command.lower() == "quit":
#     print("\033[91mCommndsOutOfRange\033[0m")
#     break
#   else:
#     print("Wrong Command")

# # Do Not Repeat Yourself

# command = ""
# started = False
# while True:
#   command = input("\nGive a Command: ").lower()
#   if command == "start":
#     if started:
#       print("Car is alreday Started.")
#     else:
#       started = True
#       print("Car Started.....")
#   elif command == "stop":
#     if not started:
#       print("Car is alreday Stopped.")
#     else:
#       started = False
#       print("Car Stopped.")
#   elif command == "help":
#     print("""\033[92m
# start -> To Start the Car
# stop  -> To Stop the Car
# quit  -> To Quit
#           \033[0m""")
#   elif command == "quit":
#     print("\033[91mQuit Command executed\033[0m")
#     break
#   else:
#     print("Wrong Command\nPlease use the 'Help' Command to know more about the Commands")