#creando una lista (se puede modificar)
lista = ["Lucas Dario","Soy Daltito",True,1.85]

#creando una tupla (no se puede modificar)
tupla = ("Lucas Dario","Soy Daltito",True,1.85)

#esto es valido
#lista[3] = "Maquinola"

#esto no
#tupla[3] = "Maquinola"

#creanodo un conjunto (set) (Conjunto no puede haber datos duplicados) (no se puede llamar elementos por su indice)


conjunto = {"Lucas Dario","Soy Daltito",True,1.85,"Lucas Dario"}
#print (conjunto[3]) --> no puede acceder al elemento

#creando un diccionario (dict) (La estructura es key y value y separamos con comas dependiendo los elementos)
diccionario = {
    #Clave     Valor
    #key       Value
    "nombre" : "Lucas Dalton",
    "Canal" : "Soy Dalto",
    "Esta emocionado" : True,
      "Altura" : 1.85,
    "Dato duplicado" : "Soy Dalto"

}
#se puede modificar fuera de las llaves
print (diccionario ['Dato duplicado'])