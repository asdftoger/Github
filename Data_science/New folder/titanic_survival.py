# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 13:22:01 2017

@author: John
"""
'''
dataset features
survival        Survival
                (0 = No; 1 = Yes)
pclass          Passenger Class
                (1 = 1st; 2 = 2nd; 3 = 3rd)
name            Name
sex             Sex
age             Age
sibsp           Number of Siblings/Spouses Aboard
parch           Number of Parents/Children Aboard
ticket          Ticket Number
fare            Passenger Fare
cabin           Cabin
embarked        Port of Embarkation
                (C = Cherbourg; Q = Queenstown; S = Southampton)
'''
'''
PassengerId    891 non-null int64
Survived       891 non-null int64
Pclass         891 non-null int64
Name           891 non-null object
Sex            891 non-null object
Age            714 non-null float64
SibSp          891 non-null int64
Parch          891 non-null int64
Ticket         891 non-null object
Fare           891 non-null float64
Cabin          204 non-null object
Embarked       889 non-null object
'''
#Columns to alter for NaNs: Age,Cabin,embarked
#Classification: Survived: 0 and 1
#SES indicators: Pclass, Age, Fare,Embarked,Name,Ticket,Cabin
#Others: Sex,SibSp,Parch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import sys
from IPython import get_ipython
get_ipython().magic('matplotlib inline')


from time import time
from scipy.stats import randint as sp_randint
from sklearn.model_selection import RandomizedSearchCV
#XXX
SEED = None
np.random.seed(SEED)
def feature_importance_plot(features,legend = None, title = 'Importance value of features'):
    sns.barplot(x = features[0],y = features.index,data = features, orient = 'h')
    plt.title(title)
    plt.show()
X = pd.read_csv('Datasets/train.csv')
X_test = pd.read_csv('Datasets/test.csv')

#correlation map
#plt.imshow(X.corr(),cmap = 'Blues')
#plt.xticks(range(len(X.corr())),X.columns,rotation = 'vertical')
#plt.yticks(range(len(X.corr())),X.columns)
#plt.colorbar()
#plt.show()

'''
Correlation
Doesn't tell me much about the dataset
'''
#==============================================================================
# 
#==============================================================================
def report(results, n_top=3):
    for i in range(1, n_top + 1):
        candidates = np.flatnonzero(results['rank_test_score'] == i)
        for candidate in candidates:
            print("Model with rank: {0}".format(i))
            print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
                  results['mean_test_score'][candidate],
                  results['std_test_score'][candidate]))
            print("Parameters: {0}".format(results['params'][candidate]))
            print("")
            
            
def dummies_fix(l1,l2,cols = None):
    #Ensures that both dataframes have the same columns
    assert isinstance(l1,pd.DataFrame)
    assert isinstance(l2,pd.DataFrame)
    #Creating dummies in both dataframes
    l1 = pd.get_dummies(l1,columns=cols)
    l2 = pd.get_dummies(l2,columns=cols)
    #Creating differences lists
    d1 = l1.columns.difference(l2.columns)
    d2 = l2.columns.difference(l1.columns)
    d1,d2 = list(d1),list(d2)

    #Setting differences to 0
    l1 = l1.drop(axis = 1, labels = d1)
    l2 = l2.drop(axis =1,labels = d2)
#    for i in d2:    
#        l1[i] = 0.0
#    print d2  
#    sys.exit()
    return l1,l2    


            
def names_breakup(*args):
    for i in args:
        i['Name_Len'] = i['Name'].apply(lambda x: len(x))
        i['Name_Title'] = i['Name'].apply(lambda x: x.split(',')[1]).apply(lambda x: x.split('.')[0])
        del i['Name']
    return args

def ticket_firstchar(*args):
    for i in args:
        i['Ticket'] = i['Ticket'].apply(lambda x: x[0])
    return args

def cabin_firstchar(*args):
    for i in args:
        i['Cabin'] = i['Cabin'].apply(lambda x: str(x)[0])
    return args

def cabin_breakup(*args):
    cabin_map = {True: 'Letter',False: 'NaN'}
    for i in args:
        i['Cabin'] = i['Cabin'].apply(lambda x: x.isupper()).apply(lambda x: cabin_map[x])
        
#        for j in i.index:
#            if i['Cabin',j]:  
#            i['Cabin'] = i['Cabin'].apply()

def family_status(*args):
    for i in args:
        for j in i.index:
            if j in i[(i.Parch == 0) & (i.SibSp == 0)].index:
                i.ix[j,'Fam_status'] = 'Single'
            elif j in i[i.Parch > 3].index:
                i.ix[j,'Fam_status'] = 'Big Family'
            else:
                i.ix[j,'Fam_status'] = 'Family'
        del i['SibSp']
        del i['Parch']
           
            #i[,'Fam_status'] = 'Single'
#       i.loc[i.loc[:,'Parch']!= 0 ]['Parch'] = 'Family'
    return args
#==============================================================================
#     
#==============================================================================
#print X.dtypes
#print X.info()
#PassengerId is not useful
X = X.drop(axis = 1,labels = ['PassengerId'])
X_test = X_test.drop(axis = 1,labels = ['PassengerId'])

#targets

y = X.Survived
X_test['Survived'] = y #Temp, Will be dropped when required.
#
X,X_test = dummies_fix(X,X_test,cols = ['Pclass','Embarked'])
# An introductory glance into the survival rates and survival rates vs Class

#sns.countplot(X.Survived,palette='Set2')
#sns.countplot(X.Survived, hue = X.Pclass)
#plt.show()


#print X.groupby(['Pclass'])['Survived'].mean()
'''
Higher Passenger class leads to higher relative survival rate
1    0.629630
2    0.472826
3    0.242363
'''

#==============================================================================
# 
#==============================================================================

#Any relationship between gender and survival?
#sex = X.Sex.unique()
#print sex

#X.Sex = pd.get_dummies(X.Sex)
#X_test.Sex = pd.get_dummies(X_test.Sex)
#print X.groupby(['Sex'])['Survived'].mean()
#A More females survived than males. Is this a SES/class thing?
#print X.groupby(['Sex','Pclass'])['Survived'].mean()
#Plotting Sex,PClass and survival
#sns.countplot(X.Sex)
plt.show()

#fig, (ax1, ax2) = plt.subplots(ncols=2,sharey=True)
#sns.countplot(X[X.Sex== 0.0]['Survived'],hue = X.Pclass,ax = ax1)
#sns.countplot(X[X.Sex== 1.0]['Survived'],hue = X.Pclass,ax = ax2)
#plt.show()
X,X_test = dummies_fix(X,X_test,cols=['Sex'])


#==============================================================================
# Age and Fare
#==============================================================================
#Fixing and group ages to compare survival
#Using qcut and categorizing
#fixna_and_qcut((X,X_test),cols = ['Age','Fare'])
#X,X_test = dummies_fix(X,X_test,cols=['Age','Fare'])

#Filling NAs without qcuting
X.Age.fillna(X.Age.mean(),inplace = True)
X.Fare.fillna(X.Fare.mean(),inplace = True)
X_test.Age.fillna(X_test.Fare.mean(),inplace = True)
X_test.Fare.fillna(X_test.Fare.mean(),inplace = True)


#sns.countplot('Age',hue = 'Survived',data = X)
'''
['male' 'female']
Sex
0.0    0.188908
1.0    0.742038
Name: Survived, dtype: float64
Sex  Pclass
0.0  1         0.368852
     2         0.157407
     3         0.135447
1.0  1         0.968085
     2         0.921053
     3         0.500000
Name: Survived, dtype: float64
Relatively more women survive than men across all classes
'''
#Any relationship between family/siblings and survival/Sex/SES?
#Single people, no SibSp and Parch were more likely to perish

family_status(X,X_test)
X,X_test = dummies_fix(X,X_test,cols = ['Fam_status'])

#Name contains the title of the person, this may indicatie higher SES, also it will tell us which women were married and not
#Create 2 more columns, namelength and title


names_breakup(X,X_test)
#X,X_test = X.drop(axis = 1, labels = ['Name_Title']), X_test.drop(axis = 1, labels = ['Name_Title'])
print X.groupby(['Name_Title'])['Survived'].mean()

#sys.exit()
X,X_test = dummies_fix(X,X_test,cols = ['Name_Title'])

#'Age' should be catted dataset by dataset, they should not be compared
#X,X_test = pd.get_dummies(X,columns = ['Age']),pd.get_dummies(X_test,columns=['Age'])
#sys.exit()
C = X.filter(axis = 1,regex = 'Name_Title')
print C.mean()
for i in C.columns:
    if C[i].mean()<0.01:
        X.drop(axis = 1,labels = i,inplace = True)
C = X_test.filter(axis = 1,regex = 'Name_Title')
print C.mean()
for i in C.columns:
    if C[i].mean()<0.01:
        X_test.drop(axis = 1,labels = i,inplace = True)        
#sys.exit()
#==============================================================================
# #Sibing spouse analysis, needs names_breakup
# #' Miss' is correct, the split contains a space.
# Married = X[(X.Age > 18) & (X.Name_Title != str(' Miss')) & (X.SibSp > 0)]
# fig, (ax1, ax2) = plt.subplots(nrows=2,sharex=False)
# sns.countplot(y = 'Sex',data = Married,hue = 'Survived',ax = ax1)
# sns.countplot(y = 'Sex',data = X,hue = 'Survived',ax = ax2)
# print X.groupby(['SibSp'])['Survived'].mean()
#==============================================================================

#print X.groupby(['SibSp'])['Sex'].mean()
#print X.groupby(['SibSp'])['Pclass'].mean()
#
#print X.groupby(['Parch'])['Survived'].mean()
#fig, (ax1, ax2) = plt.subplots(nrows=2,sharex=True)
#sns.countplot(y = 'SibSp',data = X,hue = 'Survived',ax = ax1)
#sns.countplot(y = 'Parch',data = X,hue = 'Survived',ax = ax2)


#print X.groupby(['Parch'])['Sex'].mean()
#print X.groupby(['Parch'])['Pclass'].mean()
#
#print X.groupby(['Sex','SibSp'])['Survived'].mean()
#print X.groupby(['Sex','Parch'])['Survived'].mean()
'''
Women with children and with <3 SibSp were more likely to survive than men
Sex  SibSp
0.0  0        0.168203
     1        0.310680
     2        0.200000
     3        0.000000
     4        0.083333
     5        0.000000
     8        0.000000
1.0  0        0.787356
     1        0.754717
     2        0.769231
     3        0.363636
     4        0.333333
     5        0.000000
     8        0.000000
Sex  Parch
0.0  0        0.165289
     1        0.327586
     2        0.322581
     3        0.000000
     4        0.000000
     5        0.000000
1.0  0        0.788660
     1        0.766667
     2        0.612245
     3        0.750000
     4        0.000000
     5        0.250000
     6        0.000000
'''
#==============================================================================
# #What are indicators of SES class
# #Potentially-
# #Pclass, Age, Fare,Embarked,Name,Ticket
#==============================================================================
#Embarked
#print X.groupby(['Embarked'])['Pclass'].mean()


'''
C    1.886905
Q    2.909091
S    2.350932
Embarked will be omitted but it does show that C has higher SES/PClass people
'''
#plt.show()
#print X.groupby(['Pclass'])['Age'].mean(),X.groupby(['Pclass'])['Age'].std()


#Age
'''
Pclass
1    38.233441
2    29.877630
3    25.140620
Name: Age, dtype: float64 Pclass
1    14.802856
2    14.001077
3    12.495398
On average older people are in a higher Pclass
'''


#print X.groupby(['Name_Len'])['Survived'].mean(), X.groupby(['Name_Len'])['Survived'].value_counts()
#print X.groupby(['Sex','Name_Title'])['Survived'].mean()

#Ticket analysis
#ticket_firstchar(X)
#print X.groupby(['Ticket'])['Survived'].mean()
#print X.groupby(['Ticket'])['Survived'].count()

#Cabin analysis
cabin_firstchar(X,X_test)

#print X.groupby(['Cabin'])['Survived'].count()

#print X.groupby(['Cabin'])['Survived'].mean()
#sns.countplot(x='Cabin',data = X,hue = 'Survived')

#cabin_breakup(X,X_test)
#X,X_test = dummies_fix(X,X_test,cols=['Cabin'])

#X,X_test = dummies_fix(X,X_test,cols = ['Cabin'])


dropcol = ['Ticket','Cabin']
X = X.drop(axis = 1, labels= dropcol)
X_test = X_test.drop(axis = 1, labels= dropcol)

#DROP SURVIVED IN X, X_test does not contain 'Survived
X = X.drop(axis = 1,labels = ['Survived'])
if 'Survived' in X_test.columns:
    X_test = X_test.drop(axis = 1,labels = ['Survived'])


#Classification

#sys.exit()

#Power tuning RFC
#sys.exit()

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators= 150)
param_dist = {"max_depth": [3,4,5,6,7,8,9,10,11,None],
              "max_features": sp_randint(1,len(X.columns)),
              "min_samples_split": sp_randint(20,30),
              "min_samples_leaf": sp_randint(10,20),
              "bootstrap": [False],
              "criterion": ["entropy"]}
# run randomized search
n_iter_search = 100
random_search = RandomizedSearchCV(clf, param_distributions=param_dist,
                                   n_iter=n_iter_search,random_state = SEED,n_jobs=1)
start = time()
random_search.fit(X,y)
print("RandomizedSearchCV took %.2f seconds for %d candidates"
      " parameter settings." % ((time() - start), n_iter_search))
report(random_search.cv_results_)
#print .feature_importances_
        
clf.set_params(**random_search.best_params_)
clf.random_state = SEED
clf.fit(X,y)
y_pred = clf.predict(X_test)
#print X.columns,'\n', clf.feature_importances_

feat_imp = pd.DataFrame(clf.feature_importances_,X.columns)
#plt.show()
feature_importance_plot(feat_imp)
#
#

#Exporting to CSV,DONT DELETE
EXP = pd.DataFrame(y_pred,index = [i for i in range(892,1310)],columns=['Survived'])
EXP.index.name = 'PassengerId'
EXP.to_csv('Kaggle_Titanic_sub.csv')
