import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# Autor: Rafael Lazcano
# Este archivo realiza un análisis exploratorio de parejas de variables, específicamente de la relación entre la
# supervivencia y las demás



set = pd.read_csv("C:\\Users\\r.lazcano.pello\\Desktop\\Documentos no relacionados con el proyecto\\Python\\Titanico\data\\train.csv")
sortedAge = set.sort_values('Age')
indice = np.arange(891)
plt.scatter(indice,sortedAge.Age)
#Edad
ageFlag = sortedAge.Age[1]
for x in range(1,30):
    if sortedAge.Age[x]==ageFlag:
        print("mismo que antes")
    else:
        print('cambiamos')



plt.scatter(x= set['Age'],y = set['Survived'],alpha=0.1)


#Clase
primeraSup = set.loc[(set['Survived'] == 1) & (set['Pclass']== 1)]
segundaSup = set.loc[(set['Survived'] == 1) & (set['Pclass']== 2)]
terceraSup = set.loc[(set['Survived'] == 1) & (set['Pclass']== 3)]
primeraMuer = set.loc[(set['Survived'] == 0) & (set['Pclass']== 1)]
segundaMuer = set.loc[(set['Survived'] == 0) & (set['Pclass']== 2)]
terceraMuer = set.loc[(set['Survived'] == 0) & (set['Pclass']== 3)]

#len(primeraSup)

supervivientes = (len(primeraSup),len(segundaSup),len(terceraSup))
muertos = (len(primeraMuer),len(segundaMuer),len(terceraMuer))
ind = np.arange(len(supervivientes))  # the x locations for the groups
width = 0.35  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, supervivientes, width,
                color='SkyBlue', label='Supervivientes')

rects2 = ax.bar(ind + width/2, muertos, width,
                color='IndianRed', label='muertos')

ax.set_ylabel('Nº de personas')
ax.set_title('Supervivencia por clase')
ax.set_xticks(ind)
ax.set_xticklabels(('Primera', 'Segunda', 'Tercera'))
ax.legend()

#Sex
femalesSup = set.loc[(set['Survived'] == 1) & (set['Sex']== "female")]
malesSup = set.loc[(set['Survived'] == 1) & (set['Sex']== "male")]
malesMuer = set.loc[(set['Survived'] == 0) & (set['Sex']== "male")]
femalesMuer = set.loc[(set['Survived'] == 0) & (set['Sex']== "female")]


supervivientes = (len(femalesSup),len(malesSup))
muertos = (len(femalesMuer),len(malesMuer))
ind = np.arange(len(supervivientes))  # the x locations for the groups
width = 0.35  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, supervivientes, width,
                color='SkyBlue', label='Supervivientes')

rects2 = ax.bar(ind + width/2, muertos, width,
                color='IndianRed', label='muertos')

ax.set_ylabel('Nº de personas')
ax.set_title('Supervivencia por genero')
ax.set_xticks(ind)
ax.set_xticklabels(('Mujeres', 'Hombres'))
ax.legend()


#Titles: En principio la informacion principal que indican los titulos se puede sacar del sexo y la edad. Pero
# seria interesante comprobar que pasa con los curas
#Primero pasamos a Python Vainilla para crear una lista con los títulos "limpios"
nameList = set.Name.tolist()
titles = []
for name in nameList:
    titleDirty = name.split(',')
    titleDirty = titleDirty[1].split(' ')
    title = titleDirty[1].split('.')
    titles.append(title[0])

#Ahora volvemos a Pandas, para eso convertimos la lista a un ndarray y añadimos una columna nueva al dataFrame.
npTitles = np.array(titles)
set["Titles"] = npTitles

#Indicamos que es de tipo categorico:
set["Titles"] = set["Titles"].astype('category')


curasVivos = set.loc[(set['Survived'] == 1) & (set['Titles']== "Rev")]
curasMuertos = set.loc[(set['Survived'] == 0) & (set['Titles']== "Rev")]
drVivos = set.loc[(set['Survived'] == 1) & (set['Titles']== "Dr")]
drMuertos = set.loc[(set['Survived'] == 0) & (set['Titles']== "Dr")]

#Militares
militaresVivos = set.loc[(set['Survived'] == 1) & ((set['Titles']== "Col")|(set['Titles']== "Major")|(set['Titles']== "Capt"))]
militaresMuertos = set.loc[(set['Survived'] == 0) & ((set['Titles']== "Col")|(set['Titles']== "Major")|(set['Titles']== "Capt"))]



supervivientes = (len(curasVivos),len(drVivos),len(militaresVivos))
muertos = (len(curasMuertos),len(drMuertos),len(militaresMuertos))
ind = np.arange(len(supervivientes))  # the x locations for the groups
width = 0.35  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, supervivientes, width,
                color='SkyBlue', label='Supervivientes')

rects2 = ax.bar(ind + width/2, muertos, width,
                color='IndianRed', label='muertos')

ax.set_ylabel('Nº de personas')
ax.set_title('Supervivencia por titulos especiales')
ax.set_xticks(ind)
ax.set_xticklabels(('Curas', 'Doctores','Militares'))
ax.legend()


#Familia Horizontal
plt.figure(5)
plt.scatter(x= set['SibSp'],y = set['Survived'],alpha=0.1)

#Familia vertical
plt.figure(6)
plt.scatter(x= set['Parch'],y = set['Survived'],alpha=0.1)

#Precio billete
plt.figure(7)
plt.scatter(x= set['Fare'],y = set['Survived'],alpha=0.1)

# Embarked
QVivos = set.loc[(set['Survived'] == 1) & (set['Embarked']== "Q")]
QMuertos = set.loc[(set['Survived'] == 0) & (set['Embarked']== "Q")]
SVivos = set.loc[(set['Survived'] == 1) & (set['Embarked']== "S")]
SMuertos = set.loc[(set['Survived'] == 0) & (set['Embarked']== "S")]
CVivos = set.loc[(set['Survived'] == 1) & (set['Embarked']== "C")]
CMuertos = set.loc[(set['Survived'] == 0) & (set['Embarked']== "C")]

supervivientes = (len(QVivos),len(QVivos),len(CVivos))
muertos = (len(QMuertos),len(SMuertos),len(CMuertos))
ind = np.arange(len(supervivientes))  # the x locations for the groups
width = 0.35  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, supervivientes, width,
                color='SkyBlue', label='Supervivientes')

rects2 = ax.bar(ind + width/2, muertos, width,
                color='IndianRed', label='Muertos')

ax.set_ylabel('Nº de personas')
ax.set_title('Supervivencia por lugar de embarque')
ax.set_xticks(ind)
ax.set_xticklabels(('Q', 'S','C'))
ax.legend()


