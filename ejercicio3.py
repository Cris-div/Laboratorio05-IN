import pandas as pd

# Crear los datos
datos = {
    "Estudiante": ["Ana", "Luis", "Carlos", "María", "José", "Lucía", "Pedro"],
    "Nota": [15, 12, None, 18, 14, None, 16]
}

# Crear DataFrame
df = pd.DataFrame(datos)

# Calcular la media de las notas disponibles
media = df["Nota"].mean()

print("Media de las notas:", media)

# Reemplazar los valores NaN por la media
df["Nota"] = df["Nota"].fillna(media)

# Mostrar DataFrame final
print("\nDataFrame final:")
print(df)