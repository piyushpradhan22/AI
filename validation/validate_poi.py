#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import numpy as np
import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb"))

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list, sort_keys = '../tools/python2_lesson13_keys_unix.pkl')
labels, features = targetFeatureSplit(data)
labels = np.asarray(labels).reshape(-1,1)
features = np.asarray(features).reshape(-1,1)

### it's all yours from here forward!
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()
# =============================================================================
# clf.fit(features,labels)
# print(clf.score(features, labels))
# =============================================================================

### train test split

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(features, labels, test_size=0.3,random_state=42)
clf.fit(X_train,Y_train)
pred = (clf.predict(X_test))
#print (pred)
#print (Y_test)
print (clf.score(X_test,Y_test))