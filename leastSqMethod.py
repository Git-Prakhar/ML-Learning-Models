import numpy as np

house_sizes = np.array([750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200])
house_prices = np.array([150, 180, 200, 220, 240, 270, 290, 310, 330, 360])

def leastSquareMethod(size, price):
    meanX = np.mean(size)
    meanY = np.mean(price)

    dev_x = size - meanX
    dev_y = price - meanY
    productOfDeviation = dev_x * dev_y
    dev_x_squared = dev_x ** 2
    sumOfProductOfDeviation = np.sum(productOfDeviation)
    sumOfDev_x_squared = np.sum(dev_x_squared)

    m = sumOfProductOfDeviation / sumOfDev_x_squared
    b = meanY - (m * meanX)

    return m, b

m, b = leastSquareMethod(house_sizes, house_prices)
print(f"y = {m}x + {b}")

def predictPrice(m, b, size):
    return m * size + b

print(predictPrice(m, b, 1000))