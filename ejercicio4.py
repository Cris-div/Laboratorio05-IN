import pandas as pd
from sklearn.impute import KNNImputer

# Crear los datos
datos = {
    "Estudiante": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Horas de estudio": [2.0, 3.0, 4.0, 5.0, 6.0, 3.5, 5.5, 4.5],
    "Asistencia (%)": [65, 72, 80, 88, 95, 76, 92, 85],
    "Nota": [10, 12, 14, None, 18, 13, None, 16]
}

# Crear DataFrame
df = pd.DataFrame(datos)

print("DataFrame original:")
print(df)

# Crear el imputador KNN con 3 vecinos
imputer = KNNImputer(n_neighbors=3)

# Aplicar KNN solamente a las columnas numéricas
datos_imputados = imputer.fit_transform(
    df[["Horas de estudio", "Asistencia (%)", "Nota"]]
)

# Crear DataFrame con los datos imputados
df[["Horas de estudio", "Asistencia (%)", "Nota"]] = datos_imputados

print("\nDataFrame después de aplicar KNN:")
print(df)