import pandas as pd
from sklearn.impute import KNNImputer

# Cargar el archivo Excel
df = pd.read_excel("datos_imputacion_knn_5_vecinos.xlsx")

# Mostrar los datos originales
print("Datos originales:")
print(df)

# Crear el imputador KNN con 5 vecinos
imputer = KNNImputer(n_neighbors=5)

# Columnas que se utilizarán para la imputación
columnas = [
    "Trabajadores",
    "Horas_Funcionamiento",
    "Consumo_kWh"
]

# Aplicar KNN
df[columnas] = imputer.fit_transform(df[columnas])

# Redondear los resultados a 2 decimales
df = df.round(2)

# Mostrar los datos finales
print("\nDatos después de aplicar KNN:")
print(df)