# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 22:08:07 2023

@author: Nacho
"""

from collections import Counter
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

covid_dataset = pd.read_csv("./diagnostico-sin-blank.csv")

##Se separa el mes y año de cuando se hizo el diagnostico de covid
covid_dataset['fecha_diagnostico'] = pd.to_datetime(covid_dataset['fecha_diagnostico'])

covid_dataset['mes'] = covid_dataset['fecha_diagnostico'].dt.month
covid_dataset['año'] = covid_dataset['fecha_diagnostico'].dt.year

##Se busca los casos que si fueron confirmados
casos_confirmados = covid_dataset[covid_dataset['clasificacion_resumen'] == 'Confirmado']

##De aquellos casos confirmados se crea un dataframe separando la cantidad por año y mes
casos_por_mes = casos_confirmados.groupby(['año', 'mes'])['id_evento_caso'].count().reset_index()
casos_por_mes.rename(columns={'id_evento_caso': 'cantidad_casos'}, inplace=True)

anio_2021 = casos_por_mes[casos_por_mes['año']==2021]

#print(anio_2021)

mes = np.array(anio_2021['mes']).reshape(-1,1)
cant = np.array(anio_2021['cantidad_casos'])

counter = Counter(cant)
print(counter)

X_train, X_test, y_train, y_test = train_test_split(mes, cant, test_size=0.30, random_state=0)

regresion_lineal= LinearRegression()
regresion_lineal.fit(X_train,y_train)

predicted = regresion_lineal.predict(X_test )

plt.scatter(X_train, y_train,color='g')
plt.plot(X_test, predicted,color='k')

plt.show()