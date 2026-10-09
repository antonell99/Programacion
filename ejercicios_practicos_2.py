frase = input('decime una frase y calculo el tiempo ')
palabras_separadas = frase.split(' ')
cantidad_de_palabras = len(palabras_separadas)
print(f'dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(f'dalto lo diria en {cantidad_de_palabras/2 *1.3}')
if cantidad_de_palabras > 120:
    print('para flaco tampoco te pedi un testamento')