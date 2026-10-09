import numpy as np

# Matriz con 5 puntos (x, y)
puntos = np.array([
    [3.0, 4.0],
    [1.0, 1.0],
    [0.0, 2.0],
    [5.0, 12.0],
    [8.0, 6.0]
])

# 1. Distancia euclidiana al origen por punto
# Elevamos al cuadrado, sumamos por fila (axis=1) y aplicamos raíz cuadrada

distancias = np.sqrt(np.sum(np.square(puntos), axis=1))

print("Distancias al origen:", distancias)

# 2. Centrado de datos (Media por columna axis=0)
media_columnas = np.mean(puntos, axis=0)  # [media_x, media_y]

puntos_centrados = puntos - media_columnas

print("Media por columna (X, Y):", media_columnas)

print("Puntos centrados:", puntos_centrados)
