"""In this section we will learn different concepts of python.
like:
    .Variables
        .Assign multiple values to multiple variables.
        .Assign one value to multiple variables.
        .Local variables and global variables.
        .Using the word of Global.

    Operators:
        .Arithmetic operators
        .Assignment operators
        .Comparison operators
        .Logical operators
        .Identity operators (is, isnot)
        .Membership operators (in, not in)
        .Bitwise operators
"""


# Identity operators: return true if same object is exist.
# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x
# print(x is z) # returns True because z is the same object as x
# print(x is y) # returns False because x is not the same object as y, even if they have the same content
# print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


# Membership operators: return true if the value is present in the object.
# x = ["apple", "banana"]
# print("banana" in x)


""" Intermediate Level Questions. """

"""
1. Student Result Analyzer

Create a program where:
    Store a student's name, obtained marks, and total marks in variables.
    Calculate the percentage using operators.
    Convert percentage into integer using casting.
    Use boolean conditions to check:
    If percentage >= 80 → "Excellent"
    If percentage >= 60 → "Good"
    Otherwise → "Needs Improvement"
    Print a formatted result message using string operations.
    
    Topics covered: variables, numbers, operators, casting, booleans, strings
"""

st_name = "Azhar Ali"
total_marks = 1100
obtained_marks = 873
percentage = (obtained_marks / total_marks) * 100
percentage = int(percentage)

if percentage >= 80:
    print('Excellent')
elif percentage >= 60:
    print("Good")
else:
    print('Needs Improvements')





"""
2. Password Strength Checker

Create a program that:

Store a password in a variable.
Check:
Length should be greater than 8
Password contains at least one number
Password contains at least one uppercase letter
Use boolean operators (and, or, not) to decide whether password is strong.

Topics covered: strings, booleans, operators
"""

password = 'Azhar123'
password_length = True if len(password) > 8 else False

num =[1,2,3,4,5,6,7,8,9]
n = [p for p in password if p in num]
number = True if n else False

upper_letter = None
for p in password:
    if p.isupper() == p:
        upper_letter = True
        break
    else:
        upper_letter = False
strong_password = None
if password_length and number and upper_letter:
    strong_password = True
    print('Password is strong.')
else:
    print('Password is not strong.')
    strong_password = False
