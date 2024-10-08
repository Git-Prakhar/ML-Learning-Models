import numpy as np

house_sizes = np.array([750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200])
house_prices = np.array([150, 180, 200, 220, 240, 270, 290, 310, 330, 360])

# Hyperparameters
learning_rate = 0.000001
iterations = 10000 

# Slope and Intercept
m = 0 
b = 0

def compute_cost(house_sizes, house_prices, m, b):
    total_cost = np.sum((house_prices - (m * house_sizes + b)) ** 2) / len(house_prices)
    return total_cost

def gradient_descent(house_sizes, house_prices, m, b, learning_rate, iterations):
    N = len(house_sizes)
    
    for i in range(iterations):
        
        y_pred = m * house_sizes + b
        
        new_m = (-2/N) * np.sum(house_sizes * (house_prices - y_pred))
        new_d = (-2/N) * np.sum(house_prices - y_pred)
        
        m -= learning_rate * new_m
        b -= learning_rate * new_d
        
        cost = compute_cost(house_sizes, house_prices, m, b)

        if i % 1000 == 0:
            print(f"Iteration {i}: Cost = {cost}, m = {m}, b = {b}")
    
    return m, b

m, b = gradient_descent(house_sizes, house_prices, m, b, learning_rate, iterations)

print(f"Final equation: y = {m}x + {b}")