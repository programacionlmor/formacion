"""
  Conversiones Tipos de dato

  Autor :  Formador
|
  Creación/ Actualización  Observaciones
     Junio-2-2021          Versión inicial del programa
"""


# Notas Generales:
# Hay dos tipos de conversión de datos:
# Conversión implicita : En la medida que la variable cambie de tipo de dato durante su ejecución.
# conversión explícita : Se invoca una función especifica para convertir a un tipo de dato determinado.
#

#############################
# Conversión implicita
#############################
# tipoDato = "Esto es una cadena "
# print(type(tipoDato))
# tipoDato = 1
# print(type(tipoDato))



#######################
# Conversión Explicita
#######################

# #1. De entero a flotante

# tipoDatoEntero = 1

# tipoDatoFlotante = float(tipoDatoEntero)
# print(tipoDatoFlotante)




# #2. De flotante a entero

# tipoDatoEntero = int(tipoDatoFlotante)
# print(tipoDatoEntero)

# tipoDatoFlotante = 1.9999999999999999  # Cuando hay más de o igual a dieciséis dígitos 9 después del decimal, la función devuelve entero + 1
# tipoDatoEntero = int(tipoDatoFlotante)
# print(tipoDatoEntero)


# #3.  De caracter a entero

# tipoDatoCaracter = "1"
# tipoDatoEntero = int(tipoDatoCaracter)
# print(type(tipoDatoEntero))

# tipoDatoCaracter = "a"
# tipoDatoEntero = int(tipoDatoCaracter) # Marca error

# tipoDatoCaracter = "12a"
# tipoDatoEntero = int(tipoDatoCaracter) # Marca error


# tipoDatoCaracter = "12a"
# if tipoDatoCaracter.isnumeric():
#    tipoDatoEntero = int(tipoDatoCaracter) # Marca error
# else:
#     print(" No es posible hacer la conversión")



# #4.De entero a caracter - De flotante a caracter

# tipoDatoEntero = 1
# tipoDatoCaracter = str(tipoDatoEntero)
# print(tipoDatoCaracter)
# print(type(tipoDatoCaracter))

# tipoDatoFlotante = 1.0
# tipoDatoCaracter = str(tipoDatoFlotante)
# print(tipoDatoCaracter)
# print(type(tipoDatoCaracter))

##5. Conversión listas, tuplas, diccionarios, conjuntos

# De listas a tuplas

# listaFrutas = ["fresa","banano"]
# print(listaFrutas)
# tuplaFrutas = tuple(listaFrutas)
# print(tuplaFrutas)


# De tuplas a listas

# tuplaFrutas = ("fresa","banano")
# print(tuplaFrutas)
# listaFrutas = list(tuplaFrutas)
# print(listaFrutas)


# De entero a lista
# entero = 1
# listaEntero = list(entero) # Marca error de iterable

# De float a lista
# flotante  = 1.0
# listaFlotante = list(flotante) # Marca error de iterable

# De entero a tupla
# entero = 1
# tuplaEntero = tuple(entero) # Marca error de iterable

#De float a tupla
# flotante  = 1.0
# tuplaFlotante = tuple(flotante) # Marca error de iterable

#De caracter a lista
cadena = "hoy       es viernes"
listaCadena = list(cadena)
print(listaCadena)


# caracter ="h"
# listaCaracter = list(caracter)
# print(listaCaracter)


#De caracter a tupla
# cadena = "hoy       es viernes"
# tuplaCadena = tuple(cadena)
# print(tuplaCadena)


# caracter ="h"
# tuplaCaracter = tuple(caracter)
# print(tuplaCaracter)




# Pasar de lista a variables independientes de caracteres (reto)









# #Conversión de listas a tuplas (transformación natural)

# a_tuple = (1,1,1,1,2,3,4,5,6,7,8,9,10)
# b_list = [1,2,4,5,12,2,3,4,5]

# print(tuple(b_list)) #Funcion tuple
# print(list(a_tuple)) #Funcion list

# #Conversión de string a lista o tupla
# miString = "Este es el curso de Intro a Python"
# print(tuple(miString))
# print(list(miString))

# #Conversión de listas y tuplas a set (aplica en sentido inverso)
# print(set(a_tuple))
# print(set(b_list))

# #Conversión a diccionario (solo colecciones de pares de elementos)
# ejem1 = [[1,2],[3,4]] #Esto es una lista de listas (lista anidada). La listas anidadas contienen dos elementos.
# ejem2 = [(1,2),(3,4)] #Esto es una lista de tuplas. Las tuplas contienen dos elementos.

# #Como acceder a una lista anidada
# print(ejem1)
# print(ejem1[0])
# print(ejem1[0][0])

# print(ejem2[0][1])
# #Como convertirla a un diccionario
# print(dict(ejem1))
# print(dict(ejem2))




