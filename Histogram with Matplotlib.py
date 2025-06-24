    
import matplotlib.pyplot as plt  # Import matplotlib for plotting
import numpy as np  # Import numpy for numerical operations

# Mean (average height) and standard deviation
mu = 172  # average height in cm
sigma = 8  # standard deviation in cm

# Generate normally distributed heights for 10,000 students
x = mu + sigma * np.random.randn(10000)

# Plot histogram of student heights with density normalization
plt.hist(x, bins=20, facecolor='blue')  # Histogram for first 100 samples
plt.show()

# More realistic bell curve using all 10,000 values
plt.hist(x, 100, facecolor='blue', density=True)  # Density=True converts count to probability
plt.xlabel("Height (cm)")  # Label for x-axis
plt.ylabel("Percentage of Students")  # Label for y-axis
plt.title("Heights of Students")  # Plot title
plt.grid(True)  # Enable grid

# Add mu and sigma values as text on the plot
plt.text(145, 0.04, "mu = 172\nsigma = 8")  # Annotate mean and std deviation

# Show the final plot
plt.show()
