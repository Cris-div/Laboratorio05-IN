import pandas as pd
import matplotlib.pyplot as plt

# Crear los datos
datos = {
    "Edad": [22, 25, 27, 28, 30, 31, 32, 34, 35, 36, 38, 40, 42, 45, 48]
}

# Crear DataFrame
df = pd.DataFrame(datos)

# Mostrar DataFrame
print(df)

# Crear histograma
plt.hist(df["Edad"], bins=5)

plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.title("Distribución de edades")

plt.show()