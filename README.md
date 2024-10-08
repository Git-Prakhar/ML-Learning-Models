# Machine Learning Models

This repository contains implementations of basic linear regression models using Python. The models are implemented both with and without the use of the Scikit-Learn library, as well as using NumPy for fundamental operations.

## File Descriptions

1. **gradientDescent.py**  
   Implements linear regression using the gradient descent optimization algorithm. This file contains the logic to minimize the cost function through iterative updates.

2. **leastSqMethod.py**  
   Implements linear regression using the least squares method. This file provides an analytical solution to linear regression, calculating the coefficients directly without using Scikit-Learn.

3. **linearReg.py**  
   A generic linear regression model implementation. This file demonstrates a simple linear regression model using Scikit-Learn.

4. **multiReg.py**  
   Implements multiple linear regression. This file demonstrates a multiple linear regression model using Scikit-Learn.

## Requirements

- Python 3.x
- NumPy
- Scikit-Learn (optional, depending on the file usage)

You can install the necessary libraries using pip:

```bash
pip install numpy scikit-learn
```

## Usage

To run the models, execute the corresponding Python file in the terminal. For example, to run the linear regression model with scikit-learn, use the following command:

```bash
python linearReg.py
```

## Contributions

Contributions are welcome! For feature requests, bug reports, or questions, please submit an issue or open a pull request.