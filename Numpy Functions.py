import numpy as np # pyright: ignore[reportMissingImports]

# Creating a 3x3 numpy array
a = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])

# Applying sine function element-wise to array
print(np.sin(a))

# Applying cosine function element-wise to array
print(np.cos(a))

# Applying tangent function element-wise to array
print(np.tan(a))

# Applying exponentiation (e^x) to each element
print(np.exp(a))

# Applying square root to each element
print(np.sqrt(a))

# Applying natural logarithm to each element
print(np.log(a))

# Aggregate function: sum of all elements in array
print(a.sum())

# Aggregate function: max value in array
print(a.max())

# Aggregate function: min value in array
print(a.min())

# Aggregate function: arithmetic mean of array
print(a.mean())

# Aggregate function: median of array
print(np.median(a))

# Aggregate function: standard deviation of array
print(np.std(a))

# Expanding the array to 3x4 for reshaping examples
a = np.array([[1, 2, 3, 10], 
              [4, 5, 6, 20], 
              [7, 8, 9, 30]])

# Reshaping the array to 2x6
a = a.reshape((2, 6))
print(a)

# Reshaping to 6x2
a = a.reshape((6, 2))
print(a)

# Reshaping to 3D array: 2x3x2
a = a.reshape((2, 3, 2))
print(a)

# Flattening the array to 1D
print(a.flatten())

# Transposing the 3D array (not shown directly but concept applied to 2D)
a = np.array([[1, 2, 3, 10], 
              [4, 5, 6, 20], 
              [7, 8, 9, 30]])
print(a.transpose())

# Iterating over flattened array using .flat
for x in a.flat:
    print(x)

# Accessing a specific flattened index
print(a.flat[7])

# Creating another array of same shape to demonstrate concatenation
b = np.array([[11, 12, 13, 14], 
              [15, 16, 17, 18], 
              [19, 20, 21, 22]])

# Concatenating arrays vertically (axis=0)
c = np.concatenate((a, b))
print(c)

# Stacking arrays along a new axis (creates 3D array)
c2 = np.stack((a, b))
print(c2)

# Showing the shapes after stacking
print(c.shape)   # (6, 4)
print(c2.shape)  # (2, 3, 4)

# Horizontal stacking
print(np.hstack((a, b)))

# Vertical stacking
print(np.vstack((a, b)))

# Changing array to 4x4 for splitting
a = np.array([[1,  2,  3,  4],
              [5,  6,  7,  8],
              [9,  10, 11, 12],
              [13, 14, 15, 16]])

# Splitting into 4 equal parts row-wise
parts = np.split(a, 4)
for part in parts:
    print(part)

# Splitting into 2 equal parts row-wise
parts = np.split(a, 2)
for part in parts:
    print(part)

# Horizontal split into 2 column-wise parts
parts = np.hsplit(a, 2)
for part in parts:
    print(part)

# Appending a new row [10, 20, 30, 40] correctly
b = [10, 20, 30, 40]
a = np.append(a, [b], axis=0)
#b = [[10, 20, 30, 40]] #We need a list that includes a list
#a = np.append(a, b, axis=0)
print(a)

# Inserting b as second row (index=1)
a = np.insert(a, 1, b, axis=0)
print(a)

# Changing array to 4x4 for inserting again
a = np.array([[1,  2,  3,  4],
              [5,  6,  7,  8],
              [9,  10, 11, 12],
              [13, 14, 15, 16]])

# Inserting b as second column (axis=1)
a = np.insert(a, 2, b, axis=1)
print(a)
