"""
Python list.
Methods:
    append()
    insert()  todo: used to enter a specific record at specific index.
    sort()
    copy()    todo: use the coln ":" to copy the list.
    reverse() todo: if reverse is true than sort in desending and if false than sort is assending.
    remove()
    pop()
    clear()
    count()
    extend()
    index()
"""

# Sort List

# name = ["java", "python", "dotnet", "c"]
# name.insert(2, "zohan")
# name.sort(reverse=True)
# print(name)
#
#
# # Copy List
# a = [1,2,3,4]
# b = a.copy()
# c = a[:]
# print(a)

## ================================
# LIST PRACTICE QUESTIONS + SOLUTIONS
# ================================


# 1) Given a list of integers, remove duplicate values without changing the original order.

def remove_duplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

print(remove_duplicates([1, 2, 4, 6, 7, 2, 3]))


# ==============================================


# 2) Given a list of integers, find the second largest unique number.

def second_largest(nums):
    unique = set(nums)

    if len(unique) < 2:
        return "No second largest number"

    largest = second = float('-inf')

    for num in unique:
        if num > largest:
            second = largest
            largest = num
        elif num > second:
            second = num

    return second

print(second_largest([1, 2, 4, 6, 7, 2, 3, 6, 8, 9, 37, 24, 46, 23, 41]))


# ==============================================


# 3) Rotate a list to the right by k positions.

def rotate_list(nums, k):
    if not nums:
        return []

    k = k % len(nums)

    return nums[-k:] + nums[:-k]

print(rotate_list([1,2,3,4,5,6,7,8,9,10], 4))


# ==============================================


# 4) A list contains numbers from 1 to n, but one number is missing.

def find_missing(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum

print(find_missing([1,2,3,4,5,6,8,9]))


# ==============================================


# 5) Move all zeros to the end without changing the order of non-zero elements.

def move_zeros(nums):
    result = []
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            result.append(num)

    result.extend([0] * zero_count)

    return result

print(move_zeros([0, 1, 0, 3, 12]))


# ==============================================


# 6) Product of array except self

def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]

    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]

    return result

print(product_except_self([1,2,3,4]))