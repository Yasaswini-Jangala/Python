# # def function_name("parameters")
# # function_call("arguments")

# def Multiply(x, y):
#   result = x * y
#   return result
# x, y = map(int, input("Please Enter the values of 'x' and 'y' to perform Multiplication: ").split())
# print(Multiply(x, y))

# def my_function1():
#   print("This is my_function1 without arguments and without return")
# my_function1()

# def my_function2():
#   return "This is my_function2 without arguments and with return"
# print(my_function2())

# def my_function3(msg):
#   return msg
# print(my_function3("This is my_function3 with arguments and with return"))

# # optional parameters (or) default parameter should always be at the right most in the parameters list
# def my_function4(msg = "This is my_function4 with default parameter and with return"):
#   return msg
# print(my_function4())

# def my_function5(msg1 = "This is my_function5 with 1st default parameter",msg2 = "This is my_function5 with 2nd default parameter"):
#   return msg1, msg2, "with return"
# print(my_function5())

# def my_function6(msg0, msg1 = "This is my_function6 with 1st default parameter",msg2 = "This is my_function6 with 2nd default parameter"):
#   return msg0, msg1, msg2, "with return"
# print(my_function6("This is my_function6 with a parameter"))

# def my_function7(msg1,msg2 = "This is my_function5 with 1 default parameter and with 1 parameter (default parameter)"):
#   return msg1, msg2, "with return"
# print(my_function7("This is my_function5 with 1 default parameter and with 1 parameter (parameter)"))

# def analyze_scores(scores):
#   total = sum(scores)
#   length = len(scores)
#   average = total / length
#   highest = max(scores)
#   lowest = min(scores)
#   return total, length, average, highest, lowest
# scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# total_score, length_scores, average_score, highest_score, lowest_score = analyze_scores(scores)
# print(f"Total Score: {total_score}")
# print(f"Length of Scores: {length_scores}")
# print(f"Average Score: {average_score}")
# print(f"Highest Score: {highest_score}")
# print(f"Lowest Score: {lowest_score}")

# # Lambda Functions
