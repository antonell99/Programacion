import numpy as np

matriz = np.random.randint(1, 101, size=(5, 5))
salir = False

while salir == False:
    print("Matriz actual:")
    print(matriz)
    print("MENU")
    print("-----------------")
    print("1. Transpuesta")
    print("2. Inversa")
    print("3. Calcular determinante")
    print("4. Salir")
    
    try:
        opcion_elegida = int(input("Ingrese la opcion: "))
    except ValueError:
        print("Error: Por favor, ingrese un numero entero valido.")
        continue

    if opcion_elegida <= 4:
        if opcion_elegida == 0:
            print("No existe esa opcion")
        elif opcion_elegida == 1:
            transpuesta= np.transpose(matriz)
            print("Transpuesta:", transpuesta)
            
        elif opcion_elegida == 2:
            inversa = np.linalg.inv(matriz)
            print("Inversa:", inversa)
        elif opcion_elegida == 3:
            determinante= np.linalg.det(matriz)
            print("Determinante:", determinante)
        elif opcion_elegida == 4:
            salir = True 
    else:
        print("Opcion incorrecta")
    
