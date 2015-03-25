import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
import pandas as pd


#Modeling for new restaurant investments. Try to predict the annual restaurant sales of 100,000 regional locations


loc='C:\\dex\\datascience\\kaggle\\restaurant_rev'
train_raw=loc+'\\train.csv'

def import_csv(jj):
    j=pd.read_csv(jj)
    print j.columns
    #for i in j:
        #print i.dtype
    return j
        
def plot(j):
    f1=plt.figure()
    a1={}
    c=1
    for i in j.columns[5:20]:
        a1[i]=f1.add_subplot(5,4,c)
        a1[i].plot(j[i],j['revenue'],'ro')
        plt.title(i)
        c+=1
    plt.show()

def regression(j):
    cols=[]
    n=0
    for i in j.dtypes:
        if i in ('float','int64'):
            cols.append(j.columns[n])
            n+=1
        else:
            n+=1
    print cols
    jj=j[cols]
    jcols=jj.columns.tolist()
    jcols=jcols[-1:]+jcols[:-1]
    form='revenue~'
    c=0
    for i in jj.columns[1:]:
        if c==0:
            form+=i
        else:
            form+='+'+i
            
        c+=1
    
    res=sm.ols(formula=form, data=jj).fit()
    print res.summary()
    





train=import_csv(train_raw)
#plot(train)    
regression(train)