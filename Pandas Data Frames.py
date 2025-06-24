import pandas as pd
import matplotlib.pyplot as plt

data = {
    "SSN"   : [123, 511, 422, 872],
    "Name"  : ["Anna", "Bob", "John", "Mike"],
    "Age"   : [29, 43, 82, 23],
    "Height": [176, 165, 187, 182],
    "Gender": ["f", "m", "m", "m"]
} #This is a dictionary.

df = pd.DataFrame(data) # init a data frame
print(df) # (Gives the indices automatically)
# Output 
#    SSN  Name  Age  Height Gender
# 0  123  Anna   29     176      f
# 1  422   Bob   43     165      m
# 2  511  John   82     187      m
# 3  872  Mike   23     182      m

print(df.shape) # Shape attribute of the data frame. In this case (4, 5).

df.set_index('SSN', inplace=True) # Reindexes the data by 'SSN' values.
print(df)
# Output 
#      Name  Age  Height Gender
# SSN
# 123  Anna   29     176      f
# 511   Bob   43     165      m
# 422  John   82     187      m
# 872  Mike   23     182      m

print(df.shape) # Shape attribute of the data frame. In this case (4, 4).
print(df.ndim) # ndim is the dimension attribute of the data frame.
print(df.dtypes) # Data type attribute of the data frame. It gives data type of each individual columns.

print(df.tail(2)) # Like Series
print(df.head(2))

# Output
# Name      object
# Age        int64
# Height     int64
# Gender    object
# dtype: object

print(df.T) # Transpose attribute of the data frame (Like a matrix).
 
print(df['Name']) # Wee can access a column
print(df['Name'].iloc[1]) # Wee can access a specific value by iloc attribute.
print(df.iloc[0:2])

# Plotting We can plot all numerical values directly, except 'SSN' in this case.)
df.plot() 
plt.show()

df.hist()
plt.show()

df.plot.bar()
plt.show()

# We can plot each columns one by one.
df['Age'].plot()
plt.show()

df.Age.hist()
plt.show()