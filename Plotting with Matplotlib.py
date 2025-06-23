import numpy as np 
import matplotlib.pyplot as plt 

#x = np.linspace(-100,100,201)
x = np.arange(-100,101,3) # better for this example
y1 = 0.5 * x ** 2 + 2 * x
y2 = 0.01 * x ** 3 + 2 * x + 1
y3 = 1000 * np.sin(x)
y4 = 1000 * np.log(np.abs(x))

plt.plot(x,y1,'r-')
plt.plot(x,y2, 'b--')
plt.plot(x,y3,'go')
plt.plot(x,y4,'y^')
plt.show() 