import numpy as np

arr = np.arange(10, 50)  # Crear vector de 10 a 49

arr_inver = arr[:: -1]  # Invertir el vector

arr_inver[arr_inver % 2 == 0] = -1  # Reemplazar los pares por -1

print(arr_inver)



