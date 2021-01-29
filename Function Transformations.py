import matplotlib.pyplot as plt
import numpy as np
from math import *


f = lambda x: 6.75 * ((x**3) - (2 * (x ** 2)) + x)
x = np.arange(-1, 2, 0.1)
plt.plot(x, f(x), label='Main Function')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function Transformations')
plt.show()


# Vertical Translation
vt = lambda x, k: f(x) + k
plt.plot(x, vt(x, 4), label='Vertical Translation')


# Horizontal Translation
ht = np.array([i-2 for i in x])
#plt.plot(ht, f(ht), label='Horizontal Translation')


# Vertical Scaling
vs = lambda x, A: f(x) * A
plt.plot(x, vs(x, 2), label='Vertical Scaling')

# Horizontal Scaling
hs = np.array([i*2 for i in x])
plt.plot(ht, f(ht), label='Horizontal Scaling')

plt.legend()