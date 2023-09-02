import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def predecir(edad, sexo):
    data = pd.read_csv("./Datos/covid.csv", sep=',')
    
    edad_f = float(edad) #Lo convierto a float porque el dataset tiene las edades en float

    ##Quitamos los valores que no queremos
    data.drop(data[(data['clasificacion_resumen'] == 'Sospechoso')].index, inplace=True)
    data.drop(data[(data['sexo'] == 'NR')].index, inplace=True)

    data.dropna(axis=0)

    columnas = ['sexo', 'edad', 'cuidado_intensivo', 'clasificacion_resumen', 'asistencia_respiratoria_mecanica', 'fallecido']
    datos_seleccionados = data[columnas].dropna()
    datos_seleccionados['sexo'] = datos_seleccionados['sexo'].str.strip().map({'M': 0, 'F': 1})
    datos_seleccionados['cuidado_intensivo'] = datos_seleccionados['cuidado_intensivo'].str.strip().map({'NO': 0, 'SI': 1})
    datos_seleccionados['asistencia_respiratoria_mecanica'] = datos_seleccionados['asistencia_respiratoria_mecanica'].str.strip().map({'NO': 0, 'SI': 1})
    datos_seleccionados['fallecido'] = datos_seleccionados['fallecido'].str.strip().map({'NO': 0, 'SI': 1})
    datos_seleccionados['clasificacion_resumen'] = datos_seleccionados['clasificacion_resumen'].str.strip().map({'Descartado': 0, 'Confirmado': 1})
    
    datos_seleccionados.drop(datos_seleccionados[(datos_seleccionados['edad'] != edad_f)].index, inplace=True)
#    datos_seleccionados.drop(datos_seleccionados[(datos_seleccionados['sexo'] != sexo)].index, inplace=True)

    print(datos_seleccionados[(datos_seleccionados['edad'] == edad_f)])

    X = datos_seleccionados.drop('fallecido', axis=1)
    y = datos_seleccionados['fallecido']
    X_train, X_validation, y_train, y_validation = train_test_split(X, y, test_size=0.20, random_state=7)
    model = LogisticRegression(max_iter=15000)
    model.fit(X_train, y_train)
    prediction = model.predict(X_validation)
    accuracy = accuracy_score(y_validation, prediction)
    return accuracy

print(predecir(55,0))