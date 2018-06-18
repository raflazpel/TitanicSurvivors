import statsmodels.formula.api as sm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split


set = pd.read_csv("C:\\Users\\r.lazcano.pello\\Desktop\\Documentos no relacionados con el proyecto\\Python\\TitanicSurvivors\\Data\\cleanTrainingSet.csv")

ages = set.filter(items=['Survived', 'Age','Sex','Embarked'])
ages = ages.dropna()
#Transform categorical data inot dummies

cat_vars=['Sex','Embarked']
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(ages[var], prefix=var)
    data1=ages.join(cat_list)
    ages=data1
cat_vars=['Sex','Embarked']
data_vars=ages.columns.values.tolist()
to_keep=[i for i in data_vars if i not in cat_vars]
data_final=ages[to_keep]
data_final.columns.values
data_final_vars=data_final.columns.values.tolist()
y=['Survived']

X=[i for i in data_final_vars if i not in y]
cols=["Age", "Sex_male","Sex_female"]
X=data_final[cols]
y=data_final['Survived']


model =  sm.Logit(y,X)
result=model.fit()
print(result.summary())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
print(y_pred)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))