import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,100,1)
y1 = np.sin(x)
y2 = x ** 2 + 2 * x
y3 = x ** 2 + 5 * x - 2
y4 = 1000 * np.log(np.abs(x))

plt.figure(1) # Window 1

ax1 = plt.subplot(221) 
ax2 = plt.subplot(222)
ax3 = plt.subplot(223) 
ax4 = plt.subplot(224)

ax1.plot(x,y1,'r--')
ax2.plot(x,y2,'go')
ax3.plot(x,y3)
ax4.plot(x,y4)
# The first digit says how many rows 
# we have in plot window.
# Second one says how many different columns
# we have in plot window.
# The third digit gives information 
# about this particular subplot.

plt.tight_layout() #It shows more beautiful

plt.figure(2) # Window 2

ax1 = plt.subplot(121) 
ax2 = plt.subplot(122)

ax1.plot(x,y1,'yo')
ax2.plot(x,y2,'b^')
plt.tight_layout() #It shows more beautiful

plt.show()