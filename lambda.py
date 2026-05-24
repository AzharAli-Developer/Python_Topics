"""
Lambda function.
"""

# lambda function with sinlge variable

# x= 5
# y = lambda x : x+5
# print(y(x))


# lambda function with multiple variables

# x = 6
# y =  5
# z = lambda x,y : x*y
# print(z(x, y))


########################## Lambda with built-in functions (map, filter and sorted) #######################

#with filter

# num = [1,2,3,4,5,10,20,14,13,15]
# even_numbers = list(filter(lambda x: x%2 == 0, num))
# print(even_numbers)


# with map

# num = [3, 4, 7, 5, 6, 1, 2]
# square = list(map(lambda x : x**2, num))
# print(square)

#sorted

# sorted_num = sorted(num, key=lambda x: x)
# print(sorted_num)


# 1) Sort a list of tuples based on the second value using a lambda function.

# 2) Filter all even numbers from a list using lambda with filter.

# 3) Create a new list containing the square of each number using lambda with map.

# 4) Sort a list of strings based on their length using lambda.

# 5) Extract usernames from a list of email addresses using lambda.