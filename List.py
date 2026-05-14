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
"""

# Sort List
name = ["java", "python", "dotnet", "c"]
name.insert(2, "zohan")
name.sort(reverse=True)
print(name)


# Copy List
a = [1,2,3,4]
b = a.copy()
c = a[:]
print(a)


                                                       #Intermediate Questions

# 1)reate a list of 20 numbers and print only the even numbers using list operations.
# 2)Take a list of names and print the longest name without using max().
# 3)Remove all duplicate values from a list without converting it into a set.
# 4)Reverse a list without using reverse() or slicing.
# 5)Find the second largest number in a list without sorting.
# 6)Merge two lists and remove common duplicate values.
# 7)Count how many times each element appears in a list without using Counter.
# 8)Move all zeros in a list to the end while maintaining the order of other elements.
# 9)Split a list into two equal parts. If odd, put the extra element in the first list.
# 10)Find all pairs in a list whose sum equals a target number.
# 11)Create a list of mixed data types and separate numbers, strings, and booleans into different lists.
# 12)Find the middle element of a list. If the list has even length, return both middle elements.
# 13)Replace every negative number in a list with 0.
# 14)Create a new list containing squares of only odd numbers from an existing list.
# 15)Check whether a list is a palindrome.
# 16)Insert a new element after every occurrence of a specific value.
# 17)Remove all elements greater than a given number.
# 18)Compare two lists and find elements that exist in the same positions.
# 19)Convert a sentence into a list of words and sort them by word length.
# 20)Find the product of all numeric elements in a list.


                                                        #Advance Questions

# 1)Rotate a list to the right by k positions without using built-in rotation functions.
# 2)Implement your own version of list flattening for nested lists of any depth.
# 3)Find the first non-repeating element in a list.
# 4)Detect whether a list contains a continuous subarray whose sum equals a given target.
# 5)Find the intersection of multiple lists without using set intersection.
# 6)Group list elements by their frequency.
# 7)Implement list chunking (split into groups of size n).
# 8)Rearrange a list so positive and negative numbers appear alternately.
# 9)Find the longest consecutive sequence in an unsorted list.
# 10)Build a mini task manager using lists only (add, delete, update, search tasks).
# 11)Implement your own custom sorting algorithm for a list (without using sort()).
# 12)Find the shortest sublist whose sum is greater than a target value.
# 13)Rearrange list elements in wave format (high-low-high-low).
# 14)Find duplicate elements along with their occurrence positions.
# 15)Implement matrix addition using nested lists.
# 16)Transpose a matrix using list operations only.
# 17)Find the maximum difference between two elements where larger comes after smaller.
# 18)Compress a list using run-length encoding logic.
# 19)Simulate browser back/forward history using lists.
# 20)Build a shopping cart system using list operations only.
