
import matplotlib.pyplot as plt  # Import matplotlib for plotting
import numpy as np  # Import numpy for numerical operations

# Generate 50 random values for x and y coordinates
x = np.random.rand(50)
y = np.random.rand(50)

# Basic scatter plot with default settings
plt.scatter(x, y)
plt.title("Basic Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# Custom-defined coordinates using plain Python lists
x_manual = [10, 20, 30, 40, 50, 60, 70]
y_manual = [5, 7, 3, 2, 1, 4, 6]
plt.scatter(x_manual, y_manual)
plt.title("Manual Data Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.show()

# Styled scatter plot with red 'x' markers and larger size
plt.scatter(x, y, c='red', marker='x', s=100)
plt.title("Styled Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.show()

# Another marker style example (hexagon)
plt.scatter(x, y, c='green', marker='h', s=80)
plt.title("Hexagon Marker Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.show()
