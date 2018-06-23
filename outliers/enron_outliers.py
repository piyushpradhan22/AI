#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset_unix.pkl", "rb") )
features = ["salary", "bonus"]

data_dict_ol_removed=dict(data_dict)
data_dict_ol_removed.pop('TOTAL',0)
data_dict_ol_removed.pop('SKILLING JEFFREY K',0)
data = featureFormat(data_dict_ol_removed, features)


### your code below
x=0
i=0
for point in data:
    salary = point[0]
    bonus = point[1]
    i+=1
    if((point[0])>x):
        x=point[0]
    matplotlib.pyplot.scatter( salary, bonus )
print("Highest value: ",x)
l=0
key=''
for i in data_dict_ol_removed:
    dict1=data_dict.get(i)
    dict1=dict(dict1)
    sal=dict1.get('salary')
    if(sal=='NaN'):
        sal=0
    if(sal>l):
        l=sal
        key=i
print("highest key:", key)
matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


