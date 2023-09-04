#Importamos las bibliotecas
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# Limpiamos las columnas de las clasificaciones que no nos sirve
def limpiar_data(data):
    data.drop(data[(data['clasificacion_resumen'] == 'Sospechoso')].index, inplace=True)
    data.drop(data[(data['sexo'] == 'NR')].index, inplace=True)
    data.dropna(axis=0)
    return data

#Convertimos las variables categoricas de texto a numero
def mapear_datos(data):
    data['sexo'] = data['sexo'].map({'M': 0, 'F': 1})
    data['cuidado_intensivo'] = data['cuidado_intensivo'].str.strip().map({'NO': 0, 'SI': 1})
    data['asistencia_respiratoria_mecanica'] = data['asistencia_respiratoria_mecanica'].str.strip().map({'NO': 0, 'SI': 1})
    data['fallecido'] = data['fallecido'].str.strip().map({'NO': 0, 'SI': 1})

    return data

#Separamos los datos para el entrenamiento
def separar_datos (data):
    X = data[['sexo', 'edad', 'cuidado_intensivo', 'asistencia_respiratoria_mecanica']]
    y = data['fallecido']
    X_train, X_validation, y_train, y_validation = train_test_split(X, y, test_size=0.20, random_state=7)
    return X_train, X_validation, y_train, y_validation

#Entrenamos el modelo de regresion logistica con las variables de entrenamiento
def entrenar_modelo (X_train, y_train):
    model = LogisticRegression(max_iter=15000)
    model.fit(X_train, y_train)
    return model


def prediccion(edad, sexo, cuidado_intensivo, asistencia_respiratoria_mecanica):
    # Cargar el conjunto de datos
    data = pd.read_csv("/home/ifbarrientos/mysite/covid.csv", sep=',')

    # Nos quedamos con los casos confirmados
    data = data[(data['clasificacion_resumen'] == 'Confirmado')]

    #Convertimos a la edad en float porque el dataset tiene las edades en float
    edad_f = float(edad)

    #Llamada a las funciones
    data = limpiar_data(data)
    data = mapear_datos(data)
    X_train, X_validation, y_train, y_validation = separar_datos(data)
    model = entrenar_modelo (X_train, y_train)

    #Hacemos la prediccion (Utilizamos la funcion predict_proba para poder hacer la prediccion de las columnas seleccionadas)
    #con [0][1] tomamos el valor de la derecha de la prediccion ya que este nos proporciona que tan probable es de que ocurra y
    prediccion = model.predict_proba([[sexo, edad_f, cuidado_intensivo, asistencia_respiratoria_mecanica]])[0][1]
    #lo multiplicamos por 100 para obtener un porcentaje
    porcentaje = prediccion*100
    return porcentaje


# Ejemplo para probar
edad = 11
sexo = 0  # 0 para masculino, 1 para femenino
cuidado_intensivo = 1  # 0 para no, 1 para sí
asistencia_respiratoria_mecanica = 1  # 0 para no, 1 para sí

resultado = prediccion(edad, sexo, cuidado_intensivo, asistencia_respiratoria_mecanica)
print(f"Probabilidad de fallecer: {resultado} %")

