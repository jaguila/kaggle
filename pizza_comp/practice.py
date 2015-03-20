import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import patsy

#things to remember when using regressions OLS or LOGIT you use train['y'],train['vars'] instead of formula for prediction


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
    for i in j.dtypes:
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
    keys=[]
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
    print form
    #below is linear regression
    #res=sm.ols(formula=form, data=j).fit()
    #below is logit regression used for binary dependant variables
    #y, X=patsy.dmatrices(form,j,return_type='dataframe')
    cols=j.columns[1:]
    #X=sm.add_constant(X)
    res=sm.Logit(j['y'], j[cols]).fit()
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



def regression_prep(j):
    #create the datasets that will be used for regression
    #the variables must be found
    #find the int variables using the var_train
    ints=var_train(j)
    #ints.append('y')
    #looks for non int variables and appends to jj
    jj=[i for i in j.keys() if i not in ints and i!='y']
    j.drop(jj, axis=1 ,inplace=True)
    return j

            




def keydif(j,k):
    ans=[i for i in j.keys() if i not in k.keys()]
    print "these are the variables that need to be dropped"
    for i in ans:
        if i !='y':
            print i
            j.drop(i,axis=1,inplace=True)
        else:
            pass
    return j    
    
    

train=import_json(train_raw)
test=import_json(test_raw)
test_raw1=import_json(test_raw)
test1=var_train(test)
test2=test[test1]



#plott(train)
train_r=regression_prep(train)
#print train_r.keys()
p_res_test=keydif(test,train_r)
p_res_train=keydif(train_r,test)
cols=p_res_train.columns.tolist()
cols = cols[-1:] + cols[:-1]
p_res_train=p_res_train[cols]

res_train=regression(p_res_train,p_res_test)
print res_train.summary()
#print predict_count(res_train,test)
#print p_res_train.keys()
#print p_res_test.keys()
#train.hist()
#plt.show()
#print p_res_train.shape
ans=res_train.predict(p_res_test)

def fix(j,k):
#ans=[str(i)+", "for i in ans]
    ans2=[]
    c=0
    for i in j:
        if i > k:
            ans2.append(1)
            c+=1
        else:
            ans2.append(0)
    print c
    return ans2
ans2=fix(ans,.25)
#fix(ans,.30)
req_id=[]
for i in test_raw1['request_id']:
    req_id.append(i.encode('ascii','ignore'))
ans3=zip(req_id,ans2)
            



print "count of less than 25% %s count of all %s" %len(ans2), len(ans)

import csv
with open(loc+'ans.csv','wb') as csvfile:
    answriter=csv.writer(csvfile, delimiter=',')
    answriter.writerow(['request_id','requester_received_pizza'])
    for i in range(0,len(ans3)):
        answriter.writerow(ans3[i])


