# test things here

# Idea - try to create data at a given interval as part of the python code, In parallel write this to a mysql database.

import pandas

datapath = "/Users/tim/git/MachineLearning/occupancy_data/datatest.txt"

dataset = pandas.read_csv(datapath)
print(dataset.shape)
print(dataset.head(20))
