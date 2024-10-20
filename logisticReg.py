import numpy as np
import matplotlib.pyplot as plt

class LogisticRegressionGD(object):
    def __init__(self, eta=0.05, iter=100, random_state=1):
        self.eta = eta
        self.iter = iter
        self.random_state = random_state

    def fit(self, X, y):
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.cost_ = []

        for i in range(self.iter):
            net_input = self.net_input(X)
            output = self.activation(net_input)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * np.sum(errors)

            cost = (-y.dot(np.log(output))) - ((1 - y).dot(np.log(1 - output)))
            self.cost_.append(cost)

        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]
    
    def activation(self, z):
        return 1. / (1. + np.exp(-np.clip(z, -250,250)))
    
    def predict(self, X):
        return np.where(self.activation(self.net_input(X)) >= 0.5, 1, 0)
    

weights = np.array([20, 12, 7, 25, 18, 10])
obese = np.array([1, 0, 0, 1, 1, 0])

X = weights.reshape(-1, 1)
y = obese

model = LogisticRegressionGD(eta=0.05, iter=1000, random_state=1)
model.fit(X, y)
print(model.w_)

test_weights = np.array([15, 10, 5, 30, 20, 10])

print(model.predict(test_weights.reshape(-1, 1)))