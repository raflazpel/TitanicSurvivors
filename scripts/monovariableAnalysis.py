import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Store training and tests sets
testSet = pd.read_csv("C:\\Users\\r.lazcano.pello\\Desktop\\Documentos no relacionados con el proyecto\\Python\\Titanico\data\\test.csv")
trainingSet = pd.read_csv("C:\\Users\\r.lazcano.pello\\Desktop\\Documentos no relacionados con el proyecto\\Python\\Titanico\data\\train.csv")

# Individual analysis of variables.
# We suppose PassengerId is arbitrary and thus, not relevant.

#Survive : El objetivo de nuestro estudio. Es una variable binaria.
survived =  np.array(trainingSet.Survived)
plt.figure(1)
plt.subplot(211)
plt.hist(survived,density=True,bins=[-0.5,0.5,0.5,1.5],histtype ='step')
plt.ylabel("Densidad (Tanto por 1)")
plt.xlabel(" Survived ")
plt.title(" Survived ")
plt.subplot(212)
plt.boxplot(survived)


#Pclass
#Its a categorical variable but since its categories are ints 1,2,3 we wont convert the type.
clas =  np.array(trainingSet.Pclass)
plt.figure(2)
plt.subplot(211)
plt.hist(clas,density=True,bins=[0.5,1.5,2.5,3.5],histtype ='step')
plt.ylabel("Densidad (Tanto por 1)")
plt.xlabel(" Clase ")
plt.title(" Clase ")
plt.subplot(212)
plt.boxplot(clas)

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

#Sexo:
plt.figure(4)
trainingSet['Sex'].value_counts().plot(kind='bar')

# Age: La edad es una variable continua, la primera no categorica hasta ahora.

age =  np.array(trainingSet.Age)
age = age[np.logical_not(np.isnan(age))]
plt.figure(5)
plt.title("Edad")
plt.subplot(211)
plt.hist(age,density=True,bins=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70],histtype ='step')
plt.subplot(212)
plt.boxplot(age)

#Siblings and spouses
#Its a categorical variable but since its categories are ints 1,2,3 we wont convert the type.
sibSp =  np.array(trainingSet.SibSp)
plt.figure(6)
plt.subplot(211)
plt.hist(sibSp,density=True,bins=[-0.5,0.5,1.5,2.5,3.5,4.5,5.5,6.6,7.5,8.5],histtype ='step')
plt.ylabel("Densidad (Tanto por 1)")
plt.xlabel(" Hermanos y esposas ")
plt.title(" Hermano y esposas ")
plt.subplot(212)
plt.boxplot(sibSp)

#Parch
#Its a categorical variable but since its categories are ints 1,2,3 we wont convert the type.
parch =  np.array(trainingSet.Parch)
plt.figure(7)
plt.subplot(211)
plt.hist(parch,density=True,bins=[-0.5,0.5,1.5,2.5,3.5,4.5,5.5,6.6,7.5],histtype ='step')
plt.ylabel("Densidad (Tanto por 1)")
plt.xlabel(" Padres e hijos ")
plt.title(" Padres e hijos ")
plt.subplot(212)
plt.boxplot(parch)

# La siguiente variable es el numero de ticket. En principio no deberia ser relevante para la supervivencia, a menos
# que esté correlacionado con el orden de asignacion de camarotes. Me parece curioso que haya algunos tickets repetidos.


# La siguiente variable es el precio de la tarifa

fare = np.array(trainingSet.Fare)
plt.figure(8)
plt.subplot(211)
plt.hist(fare,density=True,histtype ='step')
plt.ylabel("Densidad (Tanto por 1)")
plt.xlabel(" Precio ")
plt.title(" Precio ")
plt.subplot(212)
plt.boxplot(fare)


#Practicamente todos los valores de la cabina son nulos. ¿No tenian camarote?¿Se desconoce cual era? En principio vamos
# a dejar estar variable fuera en primera iteracion.


#Puerto de embarque:
plt.figure(9)
trainingSet['Embarked'].value_counts().plot(kind='bar')
plt.ylabel("Densidad (Tanto por 1)")
plt.xlabel(" Puerto ")

#Mostramos gráficas
plt.show()