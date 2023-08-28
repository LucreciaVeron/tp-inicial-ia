# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 22:08:07 2023

@author: Nacho
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("./covid-csv.csv")

x = df['fecha_diagnostico'].drop_duplicates()
y = df['fecha_diagnostico'].value_counts()

df_new = pd.DataFrame({'fecha_diagnostico' : x, 'count' : y})

df_new['fecha_diagnostico'] = pd.to_datetime(df_new['fecha_diagnostico'])

fechas = np.array(df_new['fecha_diagnostico']).reshape(-1,1)
cant = np.array(df_new['count']).reshape(-1,1)

regresion_lineal= LinearRegression()
regresion_lineal.fit(fechas,cant)

predicted = regresion_lineal.predict(x)

print(predicted)
