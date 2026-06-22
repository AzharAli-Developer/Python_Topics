import re

# question1: Write a program that extracts all numbers from a given string.

# name = "My age is 22234 and my brother is 232458 years old."
# num = re.findall(r'\d+', name)
# print(num)


#question2:Write a program that finds all email addresses present in a text.

# email = "Contact us at info@gmail.com or support@yahoo.com"
# match = re.findall(r'\w+@\w+\.\w+', email)
# print(match)


# question3: Write a program that extracts all words starting with the letter p.
# text = "python is powerful and programming is practical"
# match = re.findall(r'p\w+', text)
# print(match)


# question4: Write a program that checks whether a phone number follows this format:
# numbers = ["0349-7020971", "03029078559", "0329-1011159", "0320-9772971","03428821614" ]
# for num in numbers:
#     match = re.findall(r'03\d{2}-\d{7}', num)
#     if match:
#         print("Correct Number:", num)
#     else:
#         print("Incorrect Number:", num)


# question5: Write a program that counts how many times a specific word appears in a sentence. like 'python'
# text = "python is easy. python is powerful. python is popular."
# match = re.findall(r"python", text)
# print(len(match))