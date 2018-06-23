#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset_unix.pkl", "rb") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)
x=0
y=9999999999999999999
dict1=dict(data_dict)
for i in range(len(dict1)):
    exs=(dict((list(dict1.values()))[i])).get('salary')
    if(exs=='NaN'):
        exs=0
    if(exs>0 and exs<y):
        y=exs
    if(exs>x):
        x=exs
print(x,y)
### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi  = "poi"

# minmaxscaler
def featureScaling(arr):
    arr2=[]
    maxx=max(arr)
    minn=min(arr)
    i=0
    for v in arr:
        arr2.append((v-minn)/float(maxx-minn))
        i+=1
    return arr2

# tests of your feature scaler--line below is input data
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )
arr_salary=[]
arr_eso=[]
for ic in finance_features:
    arr_salary.append(ic[0])
for ic1 in finance_features:
    arr_eso.append(ic1[1])  
arr_salary=featureScaling(arr_salary)
arr_eso=featureScaling(arr_eso)
finance_features_scaled=[]
n=0
for ic2 in range(len(finance_features)):
    finance_features_scaled.append([arr_salary[n],arr_eso[n]])
    n+=1
### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2 in finance_features_scaled:
    plt.scatter( f1, f2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred
from sklearn.cluster import KMeans

km = KMeans(n_clusters=2)
pred=km.fit_predict(finance_features_scaled)


### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features_scaled, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print ("no predictions object named pred found, no clusters to plot")
