import pandas as pd
import matplotlib.pyplot as plt

# Crear los datos
datos = {
    "Producto": ["Laptop", "Mouse", "Teclado", "Monitor", "Audífonos"],
    "Ventas": [35, 80, 55, 42, 68]
}

# Crear DataFrame
df = pd.DataFrame(datos)

# Mostrar DataFrame
print(df)

# Gráfico de barras
plt.bar(df["Producto"], df["Ventas"])

plt.xlabel("Producto")
plt.ylabel("Ventas")
plt.title("Ventas por Producto")

plt.show()