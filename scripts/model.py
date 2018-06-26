import statsmodels.formula.api as sm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression



set = pd.read_csv("C:\\Users\\r.lazcano.pello\\Desktop\\Documentos no relacionados con el proyecto\\Python\\TitanicSurvivors\\Data\\cleanTrainingSet.csv")
testSet = pd.read_csv("C:\\Users\\r.lazcano.pello\\Desktop\\Documentos no relacionados con el proyecto\\Python\\TitanicSurvivors\\Data\\test.csv")
testSet = testSet.filter(items=['Age','Sex','Embarked'])


trainingSet = set.filter(items=['Survived', 'Age','Sex','Embarked'])
trainingSet = trainingSet.dropna()

#Transform categorical data inot dummies

cat_vars=['Sex','Embarked']
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(trainingSet[var], prefix=var)
    data1=trainingSet.join(cat_list)
    trainingSet=data1
cat_vars=['Sex','Embarked']
data_vars=trainingSet.columns.values.tolist()
to_keep=[i for i in data_vars if i not in cat_vars]
data_final=trainingSet[to_keep]
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


logreg = LogisticRegression()
logreg.fit(X, y)
y_pred = logreg.predict(X)
print(y_pred)
print('Accuracy of logistic regression classifier on training set: {:.2f}'.format(logreg.score(X, y)))


#Transform categorical data inot dummies

cat_vars=['Sex','Embarked']
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(testSet[var], prefix=var)
    data2=testSet.join(cat_list)
    testSet=data2
cat_vars=['Sex','Embarked']
data_vars=testSet.columns.values.tolist()
to_keep=[i for i in data_vars if i not in cat_vars]
testData_final=testSet[to_keep]
testData_final.columns.values
data_final_vars=data_final.columns.values.tolist()


X=[i for i in data_final_vars if i not in y]
cols=["Age", "Sex_male","Sex_female"]
X=testData_final[cols]
X.fillna(25.0,inplace=True)

print('wait')

y_pred = logreg.predict(X)
print('PREDICTION')
print(y_pred)



submission = pd.read_csv("C:\\Users\\r.lazcano.pello\\Desktop\\Documentos no relacionados con el proyecto\\Python\\TitanicSurvivors\\Data\\gender_submission.csv")
submission.Survived=y_pred
submission.to_csv('out2.csv',index=False)
print(submission)