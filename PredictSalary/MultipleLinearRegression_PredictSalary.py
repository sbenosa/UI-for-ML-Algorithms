'''
Author: Sherwin Benosa
To predict salary of potential employee based on position, years of experience and industry
April 10, 2019
'''
# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data_Salaries.csv')
X = dataset.drop('salary', axis=1)
y = dataset[['salary']]

# Encoding Categorical Data
dataset = pd.get_dummies(dataset)
dataset.columns

# Drop these columns to avoid dummy variable trap
dataset = dataset.drop(columns = ['position_barista','industry_F&B'])

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(dataset.drop(columns = 'salary'), dataset['salary'],
                                                    test_size = 0.2,
                                                    random_state = 0)


# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)
print(y_pred)

# Formatting Final Results
final_results = pd.concat([y_test], axis = 1).dropna()
final_results['Salary'] = y
final_results['Prediction'] = y_pred
final_results = final_results[['Prediction','Salary']].reset_index(drop=True)


# Save the Model in a binary format
import pickle

with open('predict_salary.pkl', 'wb') as model_pkl:
	pickle.dump(regressor, model_pkl)
