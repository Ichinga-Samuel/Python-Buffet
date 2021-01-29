import matplotlib.pyplot as plt
import numpy as np


x = np.array([1,2,3,4,5,6,7,8,9])
x1 = np.array([-3, -2, -1, 0, 1, 2, 3])

# Line Function
f = lambda m, b, x: m * x + b
# m is the slope of the line and b is the intercept on the y axis. It is the
# the value of y when x is = 0

plt.plot(x, f(3, 4, x), label='Straight Line')  # plot takes two main arguments x and the f(x)
plt.xlabel('x')
plt.ylabel('y')
plt.title('The Graph of Functions')
plt.legend()  # the legend function enables the label to be shown
plt.show()

# Square Function
f = lambda x: x**2

plt.plot(x1, f(x1), label='Squared Function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Square root Function
f = lambda x: x**0.5
plt.plot(x, f(x), label='Square Root Function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
