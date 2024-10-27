'''
This file is a try to create a graph of Cost Function
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])

costArr = []

def lr(w0, w1, x):
    return w0 + w1*x

def cost(w0, w1, x,y):
    return np.sum((lr(w0, w1, x) - y)**2)

def gradient(w0, w1, x, y):
    dw0 = np.sum(lr(w0, w1, x) - y)
    dw1 = np.sum((lr(w0, w1, x) - y)*x)
    return dw0, dw1

def gd(w0, w1, x, y, alpha, epochs):
    for i in range(epochs):
        dw0, dw1 = gradient(w0, w1, x, y)
        w0 = w0 - alpha*dw0
        w1 = w1 - alpha*dw1
        costArr.append(cost(w0, w1, x, y))
    return w0, w1

w0, w1 = gd(0,0, x, y, 0.01, 1000)
print(w0, w1)

# Create a meshgrid for w0 and w1 to calculate cost
w0_range = np.linspace(-10, 10, 100)
w1_range = np.linspace(-10, 10, 100)
W0, W1 = np.meshgrid(w0_range, w1_range)
Z = np.array([cost(w0, w1, x, y) for w0, w1 in zip(W0.flatten(), W1.flatten())]).reshape(W0.shape)

# Plot the cost function
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(W0, W1, Z, cmap='viridis')
plt.show()