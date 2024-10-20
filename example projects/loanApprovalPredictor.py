import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Data
data = pd.read_csv("./csv/loanApproveData.csv")

# Cleaning Data
data = data.dropna()

# Dividing Data into training set and test set
training_data, test_data = train_test_split(data, test_size=0.2)

# Values
income = training_data["income"].values
credit_score = training_data["credit_score"].values
loan_approved = training_data["loan_approved"].values

# Features and Target
X = pd.DataFrame({'income': income, 'credit_score': credit_score})
y = loan_approved

# Model
model = LogisticRegression()
model.fit(X, y)

# Weight and Bias
w = model.coef_[0]
b = model.intercept_

print(f"Weight: {w}")
print(f"Bias: {b}")

# Testing
y_test = test_data["loan_approved"].values
y_pred = model.predict(test_data[["income", "credit_score"]])
print(f"Predictions: {y_pred}")

# Metrics
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(test_data["income"], y_test, color="blue", label="Actual")
plt.scatter(test_data["income"], y_pred, color="red", label="Predicted")
plt.legend()

plt.show()