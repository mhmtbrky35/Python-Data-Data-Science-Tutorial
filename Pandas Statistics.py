import pandas as pd
import matplotlib.pyplot as plt

data = {
    "SSN"   : [123, 511, 422, 872],
    "Name"  : ["Anna", "Bob", "John", "Mike"],
    "Age"   : [29, 43, 82, 23],
    "Height": [176, 165, 187, 182],
    "Gender": ["f", "m", "m", "m"]
} #This is a dictionary.

df = pd.DataFrame(data)
df.set_index('SSN', inplace=True)

print(df.count()) 
# Output
# Name      4
# Age       4
# Height    4
# Gender    4
# dtype: int64

print(df.Age.count())
# Output
# 4

print(df['Age'].count())
# Output
# 4

print(df['Age'].sum())
# Output
# 177
print(df['Name'].sum())
# Output
# AnnaBobJohnMike

print(df['Age'].prod())
# Output
# 2351842

#print(df['Name'].prod()) 
# Causes error

print(df['Height'].mean())
# Output
# 177.5

print(df['Height'].median())
# Output
# # 179.0 ????????

print(df['Height'].mode())
# Output
# 0    165
# 1    176
# 2    182
# 3    187
# Name: Height, dtype: int64

print(df['Height'].std()) #standard deviation
# Output
# 9.46924847422786

print(df['Height'].min()) 
# Output
# 165

print(df['Height'].max()) 
# Output
# 187

print(df['Height'].describe()) # Gives all statistical values of Age.
# Output
# count      4.000000
# mean     177.500000
# std        9.469248
# min      165.000000
# 25%      173.250000
# 50%      179.000000
# 75%      183.250000
# max      187.000000
# Name: Height, dtype: float64

print(df.describe()) # Gives all statistical values of df.
# Output
#              Age      Height
# count   4.000000    4.000000
# mean   44.250000  177.500000
# std    26.525145    9.469248
# min    23.000000  165.000000
# 25%    27.500000  173.250000
# 50%    36.000000  179.000000
# 75%    52.750000  183.250000
# max    82.000000  187.000000
