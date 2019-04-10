#########################################################################
# Filename: split_data.py
# Written By: Jennifer Herasymuik
#
# Purpose: the purpose of this file is to split the data set into the training
#   data (70%) and test data (30%). It also makes sure both the test and
#   training data sets contain some of the few fraudulent transactions
#########################################################################


import csv
import random


headers = ['V4', 'V7', 'V9', 'V10', 'V11', 'V12', 'V14', 'V16', 'V17', 'V20', 'Class']

with open('datasets/creditcard.csv', 'r') as csvDataFile:
    with open('datasets/test_data.csv', 'w') as testFile:
        with open('datasets/training_data.csv', 'w') as trainingFile:
            csvReader = csv.DictReader(csvDataFile)
            training_writer = csv.DictWriter(trainingFile, headers, extrasaction='ignore', lineterminator='\n')
            test_writer = csv.DictWriter(testFile, headers, extrasaction='ignore', lineterminator='\n')
            fraud_transactions = 492
            total_transactions = 284807
            training_fraud_max = fraud_transactions * 0.7   # number of fraudulent transaction we need for training
            training_legitimate_max = (total_transactions * 0.7) - training_fraud_max   # number of legit transactions
            test_max = total_transactions - training_legitimate_max - training_fraud_max
            count = 0
            train_fraud_count = 0  # Amount of current fraudulent values for training
            training_count = 0  # Amount of current legitimate transactions for training
            for row in csvReader:
                if count == 0:
                    training_writer.writeheader()
                    test_writer.writeheader()
                    count += 1
                    continue
                rand_val = random.randint(1, 10)
                is_fraud = row.get('Class')
                # If the value is 7 or below, add to training data if not full
                if rand_val <= 7:
                    if is_fraud == '1':
                        train_fraud_count += 1
                    training_count += 1
                    training_writer.writerow(row)
                    trainingFile.flush()
                else:   # Add to testing data
                    test_writer.writerow(row)
                    testFile.flush()
                print(count)
                count += 1
            # Document to hold statistics
            with open('datasets/data_statistics.csv', 'a') as statsFile:
                stats_writer = csv.writer(statsFile, lineterminator='\n')
                stats_writer.writerow(["fraud_training", train_fraud_count])
                stats_writer.writerow(["fraud_testing", fraud_transactions - train_fraud_count])
                stats_writer.writerow(["legitimate_training", training_count])
                stats_writer.writerow(["legitimate_testing", total_transactions - training_count])
