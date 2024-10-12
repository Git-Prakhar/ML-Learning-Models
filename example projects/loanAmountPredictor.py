import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# Data
data = pd.read_csv("./csv/loanApproveData.csv")

# Cleaning Data
data = data.dropna()
data = data[data["loan_approved"] == 1]

print(data.info())

# Dividing Data into training set and test set
training_data, test_data = train_test_split(data, test_size=0.2)

# Correlation
correlation = data.corr()
print(correlation)

# Values
income = training_data["income"]
credit_score = training_data["credit_score"]
loan_amount = training_data["loan_amount"]

# Features and Target
x = np.array([income, credit_score]).T
y = np.array(loan_amount).reshape(-1, 1)

# Model
model = LinearRegression()
model.fit(x, y)

# Slope and Intercept
m1 = model.coef_[0][0]
m2 = model.coef_[0][1]
b = model.intercept_

print(f"Equation: y = {m1}x1 + {m2}x2 + {b}")

# Predictions
def predict_loan_amount(income, credit_score):
    return m1 * income + m2 * credit_score + b

# Testing
y_test = test_data["loan_amount"]
y_pred = predict_loan_amount(test_data["income"], test_data["credit_score"])

# Metrics
print(f"Mean Absolute Error: {mean_absolute_error(y_test, y_pred)}")
print(f"R2 Score: {r2_score(y_test, y_pred)}")

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(test_data["income"], y_test, color="blue", label="Actual")
plt.scatter(test_data["income"], y_pred, color="red", label="Predicted")

# Regression Line plot from m1, m2, and b
x = np.linspace(0, 200000, 100)
y = m1 * x + m2 * 700 + b
plt.plot(x, y, color="green", label="Regression Line")

plt.xlabel("Income")
plt.ylabel("Loan Amount")
plt.legend()
plt.show()