import pandas as pd


# a = [1, 4, 7, 10]
# a = pd.Series(a, index=["w", "x", "y", "z"])
# print(a)


#Select the specified index from the series.

# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories, index = ["day1", "day2"])
# print(myvar)



# data = {
#     "names":['Azhar', "Akhtar", "Asghar"],
#     "marks": [78,49, 90]
# }
# x = pd.DataFrame(data)
# print(x.loc[0])


#Read the csv file.

# data = pd.read_csv('data.csv')
# print(data.head(10))
# print(data.info())

# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
# data = pd.read_csv('data.csv')
# new_data = data.dropna()
# print(new_data.to_string())


# If you want to change the original DataFrame, use the inplace = True argument:
# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.

# data = pd.read_csv('data.csv')
# data.dropna()
# print(data.to_string())

# data = {
#     "names":['Azhar', "Akhtar", "Azhar"],
#     "marks": [78,49, 78]
# }
#
# data = pd.DataFrame(data)
# data = data.duplicated()
# print(data)
