#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list,sort_keys = '../tools/python2_lesson14_keys_unix.pkl')
labels, features = targetFeatureSplit(data)
labels = np.asarray(labels).reshape(-1,1)
features = np.asarray(features).reshape(-1,1)
X_train, X_test, Y_train, Y_test = train_test_split(features, labels, test_size=0.3,random_state=42)

### your code goes here
x=0 
for i in Y_test:
    if i[0] == 1.0 :
        x+=1
print(x)
clf = DecisionTreeClassifier()
clf.fit(X_train, Y_train)
pred = (clf.predict(X_test))
y=0
for i in range(len(Y_test)):
    if  pred[i] == Y_test[i][0] and pred[i] == 1.:
        y+=1
print(y)
print(recall_score(Y_test,pred))