
import matplotlib.pyplot as plt  # Import matplotlib for plotting

# Define the nationalities
nationalities = ['American', 'German', 'French', 'Other']

# Number of students from each nationality
students = [60, 23, 21, 34]

# Plot the basic pie chart
#plt.pie(students)  # Basic pie chart without labels

# Add labels to the pie chart
#plt.pie(students, labels=nationalities)  # Add nationality labels

# Add percentages inside the pie chart
#plt.pie(students, labels=nationalities, autopct='%1.2f%%')  # Show percentages

# Add a shadow to the chart for styling
#plt.pie(students, labels=nationalities, autopct='%1.2f%%', shadow=True)  # Add shadow effect

# Explode the 'French' slice (3rd one) to highlight it
#explode = [0, 0, 0.1, 0]  # Only French portion explodes
#plt.pie(students, labels=nationalities, autopct='%1.2f%%', shadow=True, explode=explode)

# Explode both American and French for more emphasis
explode = [0.2, 0.1, 0.1, 0.1]
#plt.pie(students, labels=nationalities, autopct='%1.2f%%', shadow=True, explode=explode)

# Sort the data and display the pie chart in ascending order
pairs = list(zip(students, nationalities))  # Combine both lists into tuples
pairs = sorted(pairs)  # Sort by number of students
students, nationalities = zip(*pairs)  # Unzip into separate lists

# Plot pie chart with sorted data
plt.pie(students, labels=nationalities, autopct='%1.2f%%', shadow=False, explode = explode,
        counterclock=False, startangle=90)  # Adjust orientation and direction

# Add title to the chart
plt.title("Student Nationality Distribution")  # Add chart title

# Display the pie chart
plt.show()
