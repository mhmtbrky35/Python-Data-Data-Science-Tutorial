import pandas as pd
import matplotlib.pyplot as plt
# We do not need import numpy because pandas use it.

# It works like dictionary
series = pd.Series([10,20,30,40], ['A','B','C','D']) # Second list always the index list
print(series)
# The output
# A    10
# B    20
# C    30
# D    40
# dtype: int64

series = pd.Series([10,20,"A string",40], index = ['A','B','C','D']) # We can specify the index list
print(series)
# The output
# A          10
# B          20
# C    A string
# D          40
# dtype: object

print(series['C']) # Second list always the index list
# print(series[10]) # This cause error

print(series.iloc[1]) # iloc gives the element from the integer location 

# We can give name to series
series.name = "My series"
print(series)
# The output
# A          10
# B          20
# C    A string
# D          40
# Name: My series, dtype: object

print(dict(series))

s1 = pd.Series([1,2,3,4], ["a","b","c","d"])
s2 = pd.Series([5,6,8,8], ["c","d","a","b"])

print(s1 + s2) # sum the values with the same indices and place the resultat the corresponding index.
# The output
# a     9
# b    10
# c     8
# d    10
# dtype: int64

s1 = pd.Series([1,2,3,4], ["a","b","c","d"])
s2 = pd.Series([5,6,8,8], ["sssssss","d","a","b"]) 

print(s1 + s2) # Unmatched indices will have NaN as their result.
# The output
# a           9.0
# b          10.0
# c           NaN
# d          10.0
# sssssss     NaN
# dtype: float64

print(s1.count()) #Like length function

print(s1.head(2)) # Gives first 2 element and their indices
# a    1
# b    2
# dtype: int64

print(s1.tail(2)) # Gives last 2 element and their indices 
# c    3
# d    4
# dtype: int64

def mysquare(x):
    return x ** 2

print(s1.apply(mysquare)) # Applies the function to all values.

s3 = pd.Series([5,1,2,3], ["c","d","a","b"])
print(s3) 
print(s3.sort_index()) # Sorts by index
print(s3.sort_values()) # Sorts by values
print(s3) # s3 won't change because the funtions return the sorted series, do not change the orignal series.
s3 = s3.sort_values() 
print(s3) # Now we can access the sorted series with original name.

s4 = pd.Series([5, 2, 8, 1, 5, 3, 7, 3], ["a", "b", "c", "d", "e", "f", "g", "h"])

s4.plot()
plt.show()
s4.plot.bar()
plt.show()

s4.plot.barh()
plt.show()

s4.plot.pie()
plt.show()

s4.plot.hist()
plt.show()

s4.to_csv("myseries.csv") # series.to_filetype("file name") 