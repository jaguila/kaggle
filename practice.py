import pandas as pd
import statsmodels.formula.api as sm
df=pd.DataFrame({"A": [10,20,30,40,50], "B": [20, 30, 10, 40, 50], "C": [32, 234, 23, 23, 42523]})

result=sm.ols(formula="A~B+C", data=df).fit()
print result.params

#import sys

import sys 
#print (sys.version)

#below is how to subset in a dataframe
#print test[test['requester_received_pizza']==True].count()
#print test[test['y']==1].count()