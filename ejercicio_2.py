import numpy as np

# 1. Matriz 4x4 del 1 al 16
matriz = np.arange(1, 17).reshape(4, 4)

print("Matriz original:", matriz)

# 2. Submatriz central (filas 1 a 3 exclusiva, columnas 1 a 3 exclusiva)
submatriz = matriz[1:3, 1:3]

print("Submatriz central:", submatriz)

# 3. Suma por columnas (axis=0)
suma_columnas = np.sum(matriz, axis=0)

print("Suma por columnas:", suma_columnas)
