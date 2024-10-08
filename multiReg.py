import numpy as np
from sklearn.linear_model import LinearRegression

features = np.array([[1,2], [2,3], [3,4], [4,5], [5,6], [6,7], [7,8], [8,9]])
originalOutput = np.array([3,5,7,9,11,13,15,17])

model = LinearRegression()
model.fit(features, originalOutput)

m = model.coef_
b = model.intercept_

m = np.round(m, 2)
b = round(b, 2)

print(f"y = {m[0]}x1 + {m[1]}x2 + {b}")

b0 = -0.0
b1 = 1.0
b2 = 1.0

def predict(x1, x2):
    return b0 + b1*x1 + b2*x2

print(predict(10, 11))