#tomo como parametro lista aunque tenga un list() dentro de la variable
#no es lo mas comun usarlo ya que tenemos las tuplas

#lista = list(['hola,', 'dalto', 34])
#print(lista)

#nos cuenta la cantidad de caracteres que tiene un texto 
#cadena = 'hola'
#resultado = len(cadena)
#print(resultado)

#en este ejemplo no devuelve la cantidad de elementos que tiene una lista, sin importar si es string,over,int o float
lista = [True,False,15,55,]
#resultado = len(lista)
#print(resultado)

#agregando un elemento a la lista.Esto modifica la lista y no la variable
#lista.append ('JAJAJAJAJ')
#print(lista)

#agregando un elemento a la lista en un indici especifico.
#lista.insert(2, 'TOMA MAMA')
#se coloca el indice a agregarlo y despues numero,texto o true o false
#no borra el indice si no que lo agrega moviendo a los demas 
#print(lista)

#agregando varios elementos a la lista, se le agrega una lista a los demas elementos
#lista.extend([False,2030])
#print(lista)

#eliminando un elemento de la lista por su indice.
# !GUARDA AL MODIFICAR LAS LISTAS, YA QUE ESTAS MODIFICAN SU ORDEN¡
#print(len(lista))

#lista.pop(0)
#lista.pop(-1), nos elimina el ultimo elemento de la lista, (-2) nos elimina el antepenultimo elemento de la lista. Asi susecivamente con los numeros

#print(len(lista))
 
#removiendo un elemento de la lista por su valor/parametro, si no encuentra en valor o parametro lanza una exepcion
#lista.remove('TOMA MAMA')
#print(lista)

#elimina todos los elementos de la lista
#lista.clear()
#print(lista)

#ordena los elementos, y no pueden tener cadenas de texto

#ordena los false, true y numeros de menaor a mayor en ese orden
#lista.sort() #reverse=True, cuando allas entendido como funciona el     sort, pon en codigo del inicio en los parentesis, y te daras cuenta que voltea todo
#print(lista)

#invirtiendo los valores de una lista, los valores que tiene esta solo los cambia de lugar de una manera desordenada
#lista.reverse()
#print(lista)

#verificando si un elemento se encuentra en una lista, busca elementos completos. El index no se puede usar en conjuntos
#elementos_encontrado = lista.index(55)
#print(elementos_encontrado)