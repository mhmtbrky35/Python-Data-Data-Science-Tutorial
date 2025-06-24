import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

#Style sheets references
#https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html

#style.use('ggplot') # Plot style 1
#style.use('fivethirtyeight') # Plot style 2
  

x = np.arange(0,20,0.1) 

y1 = np.sin(x)
y2 = np.cos(x)

plt.grid(True) # For activating grids 

plt.title("This is for the title") # Title
plt.suptitle("For the suptitle") # Sup title

# Label names
plt.xlabel("Name of x axis")
plt.ylabel("Name of y axis")

# Plot the graphs
plt.plot(x,y1, label = "Sine Function") # labeling for legend
plt.plot(x,y2, label = "Cosine Function")

# Adding a legend
plt.legend(loc = "upper left")
#plt.legend(loc = "lower right")

# Open the window
plt.show()