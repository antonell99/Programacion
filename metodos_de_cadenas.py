cadena1 = 'hola soy dalto'
cadena2 = 'bienvenido maquinola'

#resultado = DATO.METODO()
#resultado = cadena1.upper

#convierte en mayuscula
mayus = cadena1.upper()

#convierte en minuscula
minus = cadena1.lower()

#primera letra en mayuscula
primer_letra_en_masuc = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find('d')

#buscamos una cadena en otra cadena, si no hay coincidencias lanza una exepción 
busqueda_index = cadena1.index('a')

#si es numerico, devolvemos true, si no es false
es_numerico = cadena1.isnumeric()

#si es alfa numerico devolvemos  true, si no false
es_alfa_numerico = cadena1.isalpha()

#contamos las coincidencias de una cadena, dentro de otra cadena devuelve la cantidad de coincidencias
contrar_conincidencias = cadena1.count('hola')

#contamos cuantos caracteres tiene una cadena
contrar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith('h')

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith('dalto')

#reemplaza un pedazo de la cadena dada, por otra cadena dada
cadena_nueva = cadena1.replace(' ',',')

#separar cadena con la cadena que le pasemos 
cadena_separada = cadena1.split(' ')

print(cadena_separada[0])