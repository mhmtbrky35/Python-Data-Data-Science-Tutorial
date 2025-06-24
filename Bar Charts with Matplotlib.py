
import matplotlib.pyplot as plt  # Import matplotlib for data visualization
import numpy as np  # Import numpy for numerical operations

# Skill levels for 4 people in Python
python = (85, 67, 23, 98)
# Skill levels in Java
java = (70, 68, 90, 14)
# Skill levels in Networking
networking = (60, 20, 56, 22)
# Skill levels in Machine Learning
machine_learning = (88, 23, 10, 40)

# Names of the individuals
people = ['Bob', 'Anna', 'John', 'Mark']

# Create x-axis positions for the bar charts
index = np.arange(4)

# Width of each bar
width = 0.2

# Plot bar charts for each skill category
plt.bar(index, python, width=width, label='Python')  # Plot Python skills
plt.bar(index + width, java, width=width, label='Java')  # Plot Java skills
plt.bar(index + 2*width, networking, width=width, label='Networking')  # Plot Networking skills
plt.bar(index + 3*width, machine_learning, width=width, label='Machine Learning')  # Plot Machine Learning skills

# Add chart title and axis labels
plt.title("IT Skill Levels")  # Set the title of the chart
plt.xlabel("Person")  # Label for x-axis
plt.ylabel("Skill Level")  # Label for y-axis

# Set custom x-axis tick positions and labels
plt.xticks(index + 1.5*width, people)  # Place person names under grouped bars

# Add a legend to differentiate the skill categories
plt.legend(loc='upper right')

# Set the y-axis limit to better reflect actual skill values
plt.ylim(0, 120)

# Display the bar chart
plt.show()
