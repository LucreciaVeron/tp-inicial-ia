import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier

def predecir():
    covid_data = pd.read_csv("./Datos/covid.csv", sep=',')

    covid_data.head()

    covid_data['fecha_diagnostico'] = pd.to_datetime(covid_data['fecha_diagnostico'])

    ##Seleccionamos columnas que vamos a utilizar y quitamos los valores NaN
    columnas = ['sexo', 'edad', 'residencia_provincia_id', 'clasificacion_resumen', 'fecha_diagnostico']
    datos_seleccionados = covid_data[columnas].dropna()

    ##Cambiamos a numeros las columas de texto para poder hacer la regresion lineal
    label_encoder = LabelEncoder()
    for column in ['sexo', 'clasificacion_resumen', 'fecha_diagnostico']:
        datos_seleccionados[column] = label_encoder.fit_transform(datos_seleccionados[column])
        
    ##guardamos los datos en las variables x e y, x compara todas las columnas excepto calsificacion_resumen
    X = datos_seleccionados.drop('clasificacion_resumen', axis=1)
    y = datos_seleccionados['clasificacion_resumen']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f'Precisión del modelo: {accuracy:.2f}')
    
predecir()