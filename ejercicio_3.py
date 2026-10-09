import numpy as np

# 1. Generar 100 datos aleatorios
datos = np.random.normal(0, 1, 100)

# 2. Obtener estadísticas básicas
v_min = np.min(datos)

v_max = np.max(datos)

media = np.mean(datos)

print(f"Mínimo: {v_min:.2f} | Máximo: {v_max:.2f} | Media: {media:.2f}")

# 3. Normalizar entre 0 y 1 (Broadcasting de NumPy)
datos_norm = (datos - v_min) / (v_max - v_min)

print("Primeros 5 elementos normalizados:", datos_norm[:5])