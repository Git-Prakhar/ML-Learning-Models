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

5. **logisticReg.py**
   Implements logistic regression. This file demonstrates a logistic regression model without using Scikit-Learn.

6. **Example Project Folder**
   Contains a sample projects that demonstrates the use of models.

   6.1 **loanAmountPredictor.py**
   A simple project that demonstrates the use of linear regression to predict the loan amount based on the applicant's income and credit score.

   6.2 **loanApprovalPredictor.py**
   A simple project that demonstrates the use of logistic regression to predict the loan approval status based on the applicant's income and credit score.

7. **csv Folder**
   Contains the dataset used in the example project.

   7.1 **loanApproveData.csv**
   A dataset containing the applicant's age, income, loan amount, credit score, and loan approval status.

## Requirements

- Python 3.x
- NumPy
- Pandas
- Matplotlib
- Scikit-Learn (optional, depending on the file usage)

You can install the necessary libraries using pip:

```bash
pip install numpy pandas matplotlib scikit-learn
```

## Usage

To run the models, execute the corresponding Python file in the terminal. For example, to run the linear regression model with scikit-learn, use the following command:

```bash
python linearReg.py
```

## Contributions

Contributions are welcome! For feature requests, bug reports, or questions, please submit an issue or open a pull request.