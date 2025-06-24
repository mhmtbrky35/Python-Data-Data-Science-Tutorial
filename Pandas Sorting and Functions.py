import pandas as pd
import numpy as np

data = {
    "SSN"   : [123, 511, 422, 872],
    "Name"  : ["John", "Anna", "Bob", "Mike"],
    "Age"   : [29, 43, 82, 23],
    "Height": [176, 165, 187, 182],
    "Gender": ["f", "m", "m", "m"]
} #This is a dictionary.

df = pd.DataFrame(data) # init a data frame
df.set_index('SSN', inplace=True) # Set SSN As ID

print(df['Height'].apply(np.sin))
print(df['Height'].apply(lambda x: x * 100))

for x in df:
    print(x)
    
for x in df['Age']:
    print(x)

for key, value in df['Age'].items(): # DataFrame.items() iterate over (column name, Series) pairs. -> (index, value_at_that_column_and_index)
    print(f"{key}: {value}")
    
for key, value in df.items():
    print(f"{key}:\n{value}")
    
print(df)
    
for row in df.iterrows():
    print(row)
    
# Let's sort 

df.sort_index(inplace=True)
print(df)

df.sort_values(by=['Name', 'Age'], inplace=True) # The primary sorting priority is 'Name', and the secondary priority is 'Age'.
print(df)

df.sort_values(by=['Age', 'Name'], inplace=True) # The primary sorting priority is 'Age', and the secondary priority is 'Name'.
print(df)