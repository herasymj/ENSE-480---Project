#########################################################################
# Filename: rfe_analysis.py
# Written By: Jennifer Herasymuik
#
# Purpose: the purpose of this file is to determine what features are
#   more important to training the data than others.
#########################################################################


import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE

# Grab all data
number_of_trees = 7
training_data = pd.read_csv('../data/datasets/creditcard.csv')
fraud_value_index = 30

# Divide into attributes and labels
x = training_data.iloc[:, 0:fraud_value_index].values
y = training_data.iloc[:, fraud_value_index].values

# Since data is already relatively scaled, no scaling is required
model = RandomForestClassifier(n_estimators=number_of_trees, criterion="gini")

# Use recursive feature elimination to reduce features then create model
rfe_model = RFE(model, 10)
selected_features = rfe_model.fit(x, y)


# Write results to a text file
resultsFile = open('datasets/rfe_results.txt', 'a')
resultsFile.writelines("\n\n" + "Num Features: " + str(selected_features.n_features_) + '\n')
resultsFile.writelines("Selected Features: " + str(selected_features.support_) + '\n')
resultsFile.writelines("Feature Ranking: " + str(selected_features.ranking_) + '\n')
resultsFile.close()

