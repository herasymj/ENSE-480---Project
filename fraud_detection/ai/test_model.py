#########################################################################
# Filename: test_model.py
# Written By: Jennifer Herasymuik
#
# Purpose: the purpose of this file is to test the model that has been
#   previously created. It will import the model and then run it on the
#   test data. It will also print out a list of statistics related to the
#   testing of the data and the error involved.
#########################################################################


import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.externals import joblib

# TODO: make sure model is not empty, if it is run train model
# Load in the test data
fraud_value_index = 30
test_data = pd.read_csv('../data/datasets/test_data.csv')
x = test_data.iloc[:, 0:fraud_value_index].values
y = test_data.iloc[:, fraud_value_index].values

# Load the trained model
loaded_model = joblib.load('results/model.sav')

# Evaluate model with test data and print statistics to a file
result = loaded_model.predict(x)

# Write results to a text file
resultsFile = open('results/results.txt', 'a')
resultsFile.writelines(str(confusion_matrix(y, result)))
resultsFile.writelines(str(classification_report(y, result)))
resultsFile.writelines(str(accuracy_score(y, result)))
resultsFile.close()


