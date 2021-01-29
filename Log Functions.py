import matplotlib.pyplot as plt
import numpy as np
from math import *


# Exponential
x = np.array([i for i in range(10,20)])

plt.plot(x, e**x, label='e**x')
plt.xlabel('x')
plt.ylabel('y')
#plt.legend()

plt.title('Logarthmic Functions')
plt.show()

# ln(x)
z = np.array([e**i for i in x])
y = np.array([log(i) for i in z])
plt.plot(x, y, label='ln(x)')
plt.legend()
