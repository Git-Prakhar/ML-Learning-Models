import numpy as np
from sklearn.linear_model import LinearRegression

house_sizes = np.array([750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200]).reshape(-1, 1)  
house_prices = np.array([150, 180, 200, 220, 240, 270, 290, 310, 330, 360])

model = LinearRegression()
print(model)

model.fit(house_sizes, house_prices)
print(model)

m = model.coef_[0]
print(model.coef_)
b = model.intercept_

print(f"y = {m}x + {b}")