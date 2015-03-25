#pizza competition
#random acts of pizza. Create an algorithm capable of predicting which requestswill get pizza
#ex. poem, instrument
import matplotlib.pyplot as plt
import json
import re
import numpy as np
import pandas as pd
from pandas.stats.api import ols


loc="C:\\dex\\datascience\\kaggle\\pizza_comp\\"
test=open(loc+"test.json")
train=open(loc+"train.json")


plt.close()

#test=json.load(test)
#train=json.load(train)
def setup(test,train):
    #loads in test and train datasets as dataframes
    test=pd.read_json(test)
    train=pd.read_json(train)
    #print train.keys()
    y=[]
    #sets the y variable
    for i in train["giver_username_if_known"]:
        if i == 'N/A':
            y.append(0)
        else:
            y.append(1)
    train['y']=y
    #print train
    #print train['number_of_upvotes_of_request_at_retrieval']
    #res=ols(y=train['y'],x=train[['number_of_upvotes_of_request_at_retrieval','number_of_downvotes_request_at_retrieval']])
    #form="train[y]~train['number_of_upvotes_of_request_at_retrieval']+train['number_of_downvotes_request_at_retrieval']"
    #res=ols(formula=form, data=train)
    #train2=train[train['y']>0]
    #plt.plot(train['y'],train['number_of_upvotes_of_request_at_retrieval'],'ro')
    #plt.plot(train['y'],train['number_of_downvotes_of_request_at_retrieval'],'bo')
    #plt.xlabel("Get pizza")
    #plt.ylabel("Variables")
    #plt.xlim(-1,2)

    train[train.y >0].number_of_upvotes_of_request_at_retrieval.hist(bins=50)
    train[train.y>0].number_of_downvotes_of_request_at_retrieval.hist(bins=10)
   

    plt.show()
    return train

train1=setup(test,train)
c1=[10,12]
c2=[11,12]
p1=(c1<c2)
print p1


    