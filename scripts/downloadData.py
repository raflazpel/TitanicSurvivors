# Author: Rafael Lazcano
# Date: 6-03-2018

# This file downloads all the data available for the project.
# Right now does not work, it downloads the html code of kaggle instead of data.
import urllib.request


print('Beginning file download with urllib2...')

urlSubmissionExample = 'https://www.kaggle.com/c/3136/download/gender_submission.csv'
urlTestSet = "https://www.kaggle.com/c/3136/download/test.csv"
urlTraininigSet = "https://www.kaggle.com/c/3136/download/train.csv"

urllib.request.urlretrieve(urlSubmissionExample, 'C:/Users/r.lazcano.pello/Desktop/Documentos no relacionados con el'
                                                 ' proyecto/Python/Titanico/submissionExample.csv')
urllib.request.urlretrieve(urlTestSet, 'C:/Users/r.lazcano.pello/Desktop/Documentos no relacionados con el'
                                                 ' proyecto/Python/Titanico/testSet.csv')
urllib.request.urlretrieve(urlTestSet, 'C:/Users/r.lazcano.pello/Desktop/Documentos no relacionados con el'
                                                 ' proyecto/Python/Titanico/trainingSet.csv')



