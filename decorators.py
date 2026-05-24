"""
Decorators.

Rules of decorators:
    1. Function decorators need to return something
    2. Decorators can be used to wrap the functionality of another function
    3. *args and **kwargs are used to pass arguments to the function
    4. @ symbol is used to apply the decorator to the function
    5. A decorator is a function that takes another function as an argument and extends the behavior of the latter function without explicitly modifying it.

    imp: The function where we are apply the decorator, they take as a input that function and send to decorator function. In decorator function we used that decorated
    function according our functionality/requirements.

"""


# simple example of decorator

# def first(func):
#     func()
#     return "Azhar Ali"
#
# @first
# def second():
#     print('Akhtar ALi')
#
# print(second)



#Decorator function with argument.

# def first(func):
#     def inner(name):
#         return func(name).upper()
#     return inner
#
# @first
# def second(name):
#     return name
#
# name = input('Enter you name =>')
# print(second(name))


#Decorator function with list

# def first(func):
#     def inner(names):
#         for name in names:
#             print(func(name).upper())
#     return inner
#
# @first
# def second(name):
#     return name
#
# names = ['azhar', 'akhtar', 'qasim shabbir', 'zaki']
# second(names)


# 1) Create a decorator that logs the function name, arguments passed, and returned value whenever a function is called.

# 2) Create a decorator that allows a function to execute only if the user is authenticated.

# 3) Create a decorator that measures and displays the execution time of a function.

# 4) Create a decorator that executes a function multiple times based on a given parameter.

# 5) Create a decorator that retries a function automatically if it raises an exception.    