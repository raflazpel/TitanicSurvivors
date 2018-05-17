'''
This class serves a first cleansing of the data.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Store training and tests sets
testSet = pd.read_csv("C:\\Users\\r.lazcano.pello\\Desktop\\Documentos no relacionados con el proyecto\\Python\\Titanico\\data\\test.csv")
trainingSet = pd.read_csv("C:\\Users\\r.lazcano.pello\\Desktop\\Documentos no relacionados con el proyecto\\Python\\TitanicSurvivors\\Data\\train.csv")

#Delete ticket variable
del trainingSet['Ticket']

#Name: El nombre en principio es irrelevante (Se podría probar si el orden alfabetico se uso para asignar los camarotes
# que a su vez podrian estar dispuestos de manera que los mas cercanos a los bote facilitasen la supervivencia)

#Con el nombre viene el titulo que puede ser usado para observar correlacion. Master es para hombres menores, Mr para
# adultos, Ms para mujeres casadas y Mrs. para mujeres solteras

#Primero pasamos a Python Vainilla para crear una lista con los títulos "limpios"
nameList = trainingSet.Name.tolist()
titles = []
for name in nameList:
    titleDirty = name.split(',')
    titleDirty = titleDirty[1].split(' ')
    title = titleDirty[1].split('.')
    titles.append(title[0])

#Ahora volvemos a Pandas, para eso convertimos la lista a un ndarray y añadimos una columna nueva al dataFrame.
npTitles = np.array(titles)
trainingSet["Titles"] = npTitles

#Indicamos que es de tipo categorico:
trainingSet["Titles"] = trainingSet["Titles"].astype('category')
# Para comprobar las categorias:
print(trainingSet["Titles"].dtype)

#Observamos que el algoritmo no recoge bien todas las posibilidades, vamos estudiar los nombres de los pasajeros que
# dan problemas:

weirdTitles = trainingSet.loc[(trainingSet['Titles'] != 'Mr') & (trainingSet['Titles'] != 'Miss') &
                (trainingSet['Titles'] != 'Master') & (trainingSet['Titles'] != 'Mrs') ]
print(weirdTitles)

#Histograma de titulos:
plt.figure(3)
trainingSet['Titles'].value_counts().plot(kind='bar')