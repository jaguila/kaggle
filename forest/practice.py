import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import patsy

loc="C:\\dex\\datascience\\kaggle\\forest"
train=loc+"\\train.csv"
test=loc+"\\test.csv"

def importcsv(j):
    j=pd.read_csv(j)
    print j.dtypes
    
    #below we change the type of the columns that are factors to objewcts
    for i in j.keys()[11:]:
        j[i]=j[i].astype(object)
    print j.dtypes[11:]
    return j

def plott(j):
    f1=plt.figure()
    a={}
    y=0
    for i in j.keys()[11:15]:
        a[i]=f1.add_subplot(4,1,y)
        a[i].plot(j["Cover_Type"],j[i],'ro')
        plt.title(i)
        plt.xlim(0,8)
        plt.ylim(-1,2)
        y+=1
    plt.show()
        
    

train=importcsv(train)
plott(train)