import pandas as pd
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt

loc="C:\\dex\\datascience\\kaggle\\pizza_comp\\"
test_raw=loc+"test.json"
train_raw=loc+"train.json"
print test_raw
def import_json(j):
    #imports json and creates a new y column
    j1=pd.read_json(j)
    y=[]
    #print j1.describe()
    for i in j1['requester_received_pizza']:
        if i==False:
            y.append(0)
        else:
            y.append(1)
    j1['y']=y
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
        
def regression(j):
    c=0
    ints=[]
    #create a list of the keys with only integers
    for i in j.dtypes:
        if i=='int64':
           ints1=j.keys()[c]
           ints.append(ints1)
           c+=1
        else:
            #print 'no'
            c+=1
        
        
    #create a dataframe out of newlist
    jj=[i for i in j.keys() if i not in ints]
    j_remove=j[jj]
    j4=j[ints]
    j4=j4[-(j4.index.isin(j_remove.index))]
    #print j4.keys()
    #print j4.describe()
    #create list of all keys to be able to reference by index
    keys=[]
    for i in j4.keys():
        keys.append(i)
    c=1
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

    #res=sm.ols(formula="y~number_of_downvotes_of_request_at_retrieval+number_of_upvotes_of_request_at_retrieval", data=j).fit()
    res=sm.ols(formula=form, data=j).fit()
    #below prints out the summary information
    #print res.summary()
    #below prints out the parameters aka coefficients
    return res

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


            


train=import_json(train_raw)
#print train.keys()

#plott(train)
res_train=regression(train)


    