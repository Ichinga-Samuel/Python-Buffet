import matplotlib.pyplot as plt
import numpy as np
from math import *


x = np.array([i for i in range(-7, 7)])
y = np.array([sin(i) for i in x])

# Sine Function
# f = sin(x)
plt.plot(x, y, label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('The Graph of Trigonometric Functions')
plt.show()

# Cosine Function
y = np.array([cos(i) for i in x])
plt.plot(x, y, label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

yx = lambda x: pow(sin(x),2) + pow(cos(x),2)
y = np.array([yx(i) for i in x])
plt.plot(x, y, label='sin(x)**2 + cos(x)**2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Tangent Function
y = np.array([tan(i) for i in x])
plt.plot(x, y, label='tan(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

