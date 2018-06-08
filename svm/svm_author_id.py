#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time

sys.path.append("../tools/")
from tools.email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
# features_train = features_train[:len(features_train) // 100]
# labels_train = labels_train[:len(labels_train) // 100]
#########################################################
### your code goes here ###
from sklearn.svm import SVC

clf = SVC(C=10000,kernel='rbf')
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
list1=list(pred)
print(list1.count(1))
print(pred)
print(clf.score(features_test, labels_test))
#########################################################
