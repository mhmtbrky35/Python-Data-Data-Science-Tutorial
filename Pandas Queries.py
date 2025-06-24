import pandas as pd

# Reading csv file as a Data Frame
df = pd.read_csv('people.csv', delimiter = ',')

df.set_index('SSN', inplace = True)
#print(df)

print(df.loc[df['Age'] == 45]) # Interesting

print(df.loc[(df['Age'] >= 45)  & (df['Height'] > 170)]) # Interesting

print(df.loc[df['Age'] == 45]['Name']) # Interesting
