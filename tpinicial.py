#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


mydataset = pd.read_csv("./2022-new.csv")
mydataset


mydataset.keys()


mydataset['departamento_id']


mydataset[['departamento_nombre', 'cantidad_casos']]


mydataset.plot.scatter(x='cantidad_casos', y='provincia_nombre')
plt.show()


mydataset.plot.scatter(x='cantidad_casos', y='departamento_nombre')
plt.show()


mydataset.plot.scatter(x='semanas_epidemiologicas', y='cantidad_casos')
plt.show()


agrupado_semanas = mydataset.groupby('semanas_epidemiologicas')['cantidad_casos'].sum()
#print(agrupado_semanas)


agrupado_departamento = mydataset.groupby('departamento_nombre')['cantidad_casos'].sum()
#print(agrupado_departamento)


agrupado_provincia = mydataset.groupby('provincia_nombre')['cantidad_casos'].sum()
#print(agrupado_provincia)


agrupado_edad = mydataset.groupby('grupo_edad_desc')['cantidad_casos'].sum()
#print(agrupado_edad)


ejemplo = np.array(agrupado_departamento)
#print("//////////////////////////////////////////")
#print(ejemplo)


ejemplo2 = mydataset.groupby(['departamento_nombre', 'cantidad_casos'])
#print(ejemplo2)
mydataset.head()

mydataset = pd.DataFrame(mydataset)


x = mydataset.values
#print("LO DE X ////////////////////////////////////")
#print(x)


departamentos = np.array(mydataset['grupo_edad_id']).reshape(-1,1)
print("LO DE DEPARTAMENTOS ////////////////////////////////////")
print(departamentos)

cantidad = np.array(mydataset['cantidad_casos'])
print("LO DE CANTIDAD ////////////////////////////////////")
print(cantidad)

Dep_train, Dep_test, cant_train, cant_test = train_test_split(departamentos, cantidad, test_size = 0.25)

regresion_lineal= LinearRegression()
regresion_lineal.fit(Dep_train, cant_train)



predicted = regresion_lineal.score(Dep_test, cant_test)

print(predicted)