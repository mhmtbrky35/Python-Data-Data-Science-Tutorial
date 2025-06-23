import numpy as np # pyright: ignore[reportMissingImports]

#initialization of numpy array
first_array = np.array([1,2,3,4])
b = np.array([5,6,7,8])

print(first_array[0])
print(b[1])

#initialization of multi dimentional numpy array
c = np.array([[1,2,3,4],[5,6,7,8]])

print(c.shape) #Gives size and row size of matrix.

#addition of Python arrays
x = [1,2,3,4]
y = [5,6,7,8]
print(x + y)

#addition of numpy arrays
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
print(x + y)

#Zeros and Ones Functions
a = np.zeros((5,7,3))
print(a)

b = np.ones((5,7,3))
print(b)

#Full Function
c = np.full((5,7,3), 9)
print(c)

#Empty Function
a = np.empty((8,4,2))
print(a)

#Random
a = np.random.random((5,5))
print(a)

#Some Mathematical operations
x = np.array([0,5,10,15,20,25,30])
y = x * 2 - x ** 2 
print(y)

#arange funciton
x = np.arange(0, 1000, 5)
y = x * 2 - x ** 2 
print(y)


#linspace
x = np.linspace(0, 1000, 101)
print(x)

#I could not find an argument
x = np.linspace(0, 1000, 101)
y = np.sin(x)
print(y)

#size
print(x.size)

#ndim
print(x.ndim)

#dtype
print(x.dtype)
