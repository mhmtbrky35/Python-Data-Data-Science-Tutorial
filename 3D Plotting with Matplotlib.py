
import matplotlib.pyplot as plt  # Import matplotlib for plotting
import numpy as np  # Import numpy for numerical operations
from mpl_toolkits import mplot3d  # Import 3D plotting toolkit

# ---- Spiral Plot in 3D using sine and cosine ----
# Create a 3D axis
fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')

# Define z as the input range, and x/y as sine and cosine of z
z = np.linspace(0, 30, 100)
x = np.sin(z)
y = np.cos(z)

# Plot a 3D line using x, y, z coordinates
ax.plot3D(x, y, z)
plt.title("3D Spiral Plot")

# ---- Surface Plot in 3D using a custom function ----
def z_function(x, y):
    return np.sin(np.sqrt(x**2 + y**2))  # Define a function of two variables

# Define input ranges for x and y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# Convert 1D arrays into 2D mesh grids
X, Y = np.meshgrid(x, y)

# Compute Z values using the function
Z = z_function(X, Y)

# Create a new 3D axis for surface plot
fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='viridis')  # You can change cmap to change color styling
plt.title("3D Surface Plot")
plt.show()
