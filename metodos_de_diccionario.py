#podemos usar numeros en el diccionario para usarlo de llave, y asignarle el valor 
diccionario = {
    'nombre' : 'lucas',
    'apellido':'dalto',
    'subs' : 100000
}
#keys devuelve las clasves, y nos sirve para (iterar) --> no le presten atencion al iterar, aun no lo vemos

#nos devuelve un objeto dict.item
#claves = diccionario.keys()
#print(claves)

#get devuelve el valor de una clave, 
#obteniendo un elemento con get() (si no encuentra nada el programa continua)
#claves = diccionario.get('nombre')
#print(claves)

#clear elimina todos los elementos del diccionario

#diccionario.clear ()
#print(diccionario)

#pop elimina un elemento del diccionario, se puede sacar mas de un elemento usando la coma y poniendo la otra llave

#diccionario.pop('apellido')
#print(diccionario)

#items sirve para iterar el dict. Obteniendo un elemento dict_items iterable
#iterear es recorer el elemento. !RECUERDEN QUE AUN NO LO VEMOS, NO LE DEN TANTA BOLILLA¡

#diccionario_iterable = diccionario.items()
#print(diccionario_iterable)