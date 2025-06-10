# # globals()['variable'] -> if assigning any value to the local variable with same name as global variable

# add = lambda x = 10 : (lambda y : x + y)
# a = add()
# print(a)
# print(a(20))

# def show(a):
#     print(a(15))
# show(lambda x : x)

# def add():
#     y = 5
#     return (lambda x = 10 : x + y)
# add()

# # IIFE
# sum1 = lambda x : x + 5
# print(sum1(10))

# print((lambda x : x + 10)(5))

# add = lambda x, y : x + y 
# print(add(5, 2))

# # Function Decorator -> We use @function_name to specify a decorator to be applied on another function,  here functions are taken as argument into another function and then called inside the wrapper function.
 
# # Function Signature Order Rule
# def func(required, *args, default = None, **kwargs):
#   pass

# # Function Decorator
# def my_decorator(func):
#   def wrapper(*args, **kwargs):
#     print("Before the Function call")
#     result = func(*args, **kwargs)
#     print("After the Function call")
#     return result
#   return wrapper
# @ my_decorator
# def greet(name):
#     print(f"Hello, {name}! Welcome...")
# name = input("Enter your Name: ")
# greet(name)

# def require_admin(func):
#   def wrapper(user):
#     if user == 'guest':
#       print('Please Create an Account to Access!!..')
#       return
#     if user == 'admin':
#       print('Access Granted!!..')
#       return
#     return func(user)
#   return wrapper
# @ require_admin
# def view_dashboard(user):
#   print(f'Welcome, {user}, Here is your Dashboard ')
# user = input("Enter the user type(guest or admin or user): ")
# view_dashboard(user)