import numpy as np

# a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(a)
# print(a.shape)

# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print('shape of array :', arr.shape)


######################## Array Reshape ##########################


# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(x)
# print(x.reshape(2, 5))

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(2, 3, 2)
# print(newarr)


# Can We Reshape Into any Shape?
# Yes, as long as the elements required for reshaping are equal in both shapes.
# We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements.

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(3, 3)
# print(newarr)