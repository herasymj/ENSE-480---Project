#########################################################################
# Filename: train_model.py
# Written By: Jennifer Herasymuik
#
# Purpose: the purpose of this file is to train a model using the already
#   split training data. It will then export the model into a dot file
#   for use later in the program
#########################################################################


import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree

# Grab training data
number_of_trees = 7
training_data = pd.read_csv('../data/datasets/training_data.csv')
fraud_value_index = 10

# Divide into attributes and labels
x = training_data.iloc[:, 0:fraud_value_index].values
y = training_data.iloc[:, fraud_value_index].values

# Since data is already relatively scaled, no scaling is required
model = RandomForestClassifier(n_estimators=number_of_trees, criterion="gini")

# Create the model
model.fit(x, y)

# Save the model into a file, print the trees
pickle.dump(model, open('results/model.sav', 'wb'))
count = 1
for tree_model in model.estimators_:
    file_name = "results/tree" + str(count)
    count += 1
    dotfile = open(file_name + ".dot", 'w')
    tree.export_graphviz(tree_model, out_file=dotfile, class_names=['0', '1'])
    dotfile.close()

