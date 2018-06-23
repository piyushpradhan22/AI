#!/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    errorList=[]

    ### your code goes here
    print("inside Cleaner")
    
    agesList=[]
    net_worthsList=[]
    predictionsList=[]
    for x in range(len(ages)):
        agesList.append([ages[x][0]])
        net_worthsList.append([net_worths[x][0]])
        predictionsList.append([predictions[x][0]])
    
    for i in range(len(predictions)):
        error = abs(predictionsList[i][0] - net_worthsList[i][0])
        errorList.append(error)
        
    for j in range((len(predictions))//10):
        ix=errorList.index(max(errorList))
        errorList.pop(ix)
        agesList.pop(ix)
        net_worthsList.pop(ix)
    for k in range(len(agesList)):
        cleaned_data.append((agesList[k],net_worthsList[k],errorList[k]))
    return cleaned_data

