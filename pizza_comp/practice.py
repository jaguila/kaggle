import pandas as pd
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt
import patsy

loc="C:\\dex\\datascience\\kaggle\\pizza_comp\\"
test_raw=loc+"test.json"
train_raw=loc+"train.json"
print test_raw
def import_json(j):
    #imports json and creates a new y column
    j1=pd.read_json(j)
    y=[]
    requ=[]
    #print j1.describe()
    if j==train_raw:
        for i in j1['requester_received_pizza']:
            if i==False:
                y.append(0)
            else:
                y.append(1)

        j1['y']=y

    else:
        pass
    for i in j1['requester_upvotes_minus_downvotes_at_request']:
        if i<0:
            requ.append(0)
        else:
            requ.append(i)
    j1.drop('requester_upvotes_minus_downvotes_at_request',1)
    j1['requester_upvotes_minus_downvotes_at_request']=requ
    return j1
    
def plott(j):
    #start by setting up figure, then adding subplot, then plotting on subplot
    
    f1=plt.figure()
    c=1
    #add a dictionary to allow for assign a new variable while iterating
    ax1={}
    for i in j.keys()[1:4]:
        #you must use encode to remove the unicode
        ii=i.encode('ascii','ignore')
        #makes a dictionary key by the current key and the adds subplot
        ax1[ii]=f1.add_subplot(4,1,c)
        print ii
        #refers to subplot and plots on it
        ax1[ii].plot(j['y'],j[ii],'ro') 
        plt.xlim(-1,2)
        plt.title(ii)
        c+=1
    plt.show()
def var_train(j):
    #create list of keys with only integers
    c=0
    ints=[]
    for i in test.dtypes:
        if i=='int64':
            ints1=j.keys()[c]
            ints.append(ints1)
            c+=1
        else:
            #print 'no'
            c+=1
    test1=j[ints]
    return ints
        
def regression(j,k):
    ints=var_train(k)
    ints.append('y')
    #create a dataframe out of newlist
    jj=[i for i in j.keys() if i not in ints and i!='y']
    j_remove=j[jj]
    #print j_remove.keys()
    #j4=j[ints]
    xfer=[]
    for i in j['y']:
        xfer.append(i)
    #j4=j4[-(j4.index.isin(j_remove.index))]
    j=j[-(j.index.isin(j_remove.index))]
    #j4['y']=xfer
    #print j4['y']
    print j.keys()
    #print j4.describe()
    #create list of all keys to be able to reference by index
    keys=[]
    #for i in j4.keys():
    for i in j.keys():
        keys.append(i)
    c=1
    #print keys
    #create string for formula in ols
    form="y~"
    #if statement for difference in start of formula
    for i in keys:
        if c==1 and i!='y':
            form+="%s" %i
        elif c>1 and i!='y':
            form+="+%s" %i
        c+=1
    form=str(form)
    #below is linear regression
    #res=sm.ols(formula=form, data=j).fit()
    #below is logit regression used for binary dependant variables
    #y, X=patsy.dmatrices(form,j,return_type='dataframe')
    #res=sm.Logit(y, X).fit()
    #below prints out the summary information
    #print res.summary()
    #below prints out the parameters aka coefficients
    #return res


            


train=import_json(train_raw)
test=import_json(test_raw)
print test.keys()
test1=var_train(test)
test2=test[test1]



#plott(train)
res_train=regression(train,test)
#print res_train.summary()


def predict_count(j,k):
    pred=j.predict(k)
    count=0
    missing=0
    for i in pred:
        if i == 0:
            missing+=1
        elif i==1:
            count+=1
        else:
            pass
    print missing
    print count

def negdim(j):
    neg=[]
    for i in j.keys():
        if j[i].dtype=='int64':
            for ii in j[i]:
                if ii<0:
                    neg.append(i)
                    continue
                else:
                    pass
        else:
            pass
    #set returns only unique values
    neg=set(neg)
    neg=list(neg)
    return neg
#print negdim(train)
#print negdim(test)
            