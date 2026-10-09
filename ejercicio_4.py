import numpy as np

# Fijamos semilla para reproducibilidad
np.random.seed(42)

# 1. Matriz 5x5 con enteros entre 1 y 100
matriz = np.random.randint(1, 101, size=(5, 5))

print("Matriz inicial:", matriz)

# 2. Posiciones donde valor > 50
filas, columnas = np.where(matriz > 50)

print("Coordenadas (fila, col) de valores > 50:")

for f, c in zip(filas, columnas):
    
    print(f"Fila {f}, Columna {c} -> Valor: {matriz[f, c]}")

# 3. Copia y reemplazo de valores < 30
matriz_filtrada = matriz.copy()

matriz_filtrada[matriz_filtrada < 30] = 0

print("Matriz con valores < 30 reemplazados por 0:", matriz_filtrada)