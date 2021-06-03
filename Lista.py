"""
  Listas en python
  Autor :  Formador
|
  Creación/ Actualización  Observaciones
     Mayo-28-2021          Versión inicial del programa
"""
from os import system

######################################################
#  OPERACIONES BASICAS CON LISTAS
######################################################


# # #creo una lista vacia
# numeros = []
# print(numeros)

# # #Añadir elementos a lista 
# numeros.append(5)
# print(numeros)

# numeros.append("piña")
# print(numeros)

# numeros.append("sandia")
# print(numeros)

# numeros.append("calabazas")
# print(numeros)

# numeros.append("manzanas")
# print(numeros)

# numeros.append("peras")
# print(numeros)

# numeros.append("uvas")
# print(numeros)

# numeros.append("zanahorias")
# print(numeros)

# numeros.append("bananos")
# print(numeros)

# numeros.append("cerezas")
# print(numeros)

# numeros.append("fresas")
# print(numeros)

# numeros = [5,"piña","sandia","calabazas","manzanas","peras","uvas","zanahorias","bananos","cerezas","fresas"]
# print(numeros)

# # #Cambiar el valor de un elemento 
# numeros[0] = 6
# print(numeros)

# numeros[2] = "piña"
# print(numeros)

# numeros[-3] = "agraz"
# print(numeros)

# # #Ver un rango de la lista con incrementos
# numeros = [5,"piña","sandia","calabazas","manzanas","peras","uvas","zanahorias","bananos","cerezas","fresas"]
# porcionLista = numeros[1:10:2]
# print(porcionLista)

# #Insertar un elemento a la lista
# numeros.insert(9,"melocotones") # El elemento que inserto queda en esa posición
# print(numeros)

# # #Borrar un elemento a la lista por indice
# numeros.pop(0)
# print(numeros)

# # #Borrar  el primer elemento que coincida en contenido
# numeros.remove("fresas")
# print(numeros)

# del numeros[0:len(numeros)+1]
# print(numeros)

# # ######################################################
# # #  OTRAS FUNCIONES CON LISTAS
# # ######################################################

# # #funcion count() cuenta la cantidad de veces que un elemento aparece en la lista.
# numeros = [5,"piña","fresas","calabazas","manzanas","fresas","uvas","zanahorias","bananos","cerezas","fresas"]
# numeroRepeticiones = numeros.count("fresas")
# print(numeroRepeticiones)

# # #funcion extend() extiende una lista agregando un iterable al final.
# numeros.extend(["moras"])
# print(numeros)

# # #funcion index() recibe un elemento como argumento, y devuelve el índice de su primera aparición en la lista.
# indice =numeros.index("fresas")
# print(indice)

# indice =numeros.index("fresas",3)
# print(indice)

# # #funcion reverse(). Asigna sobre la misma variable.
# # #invierte el orden de los elementos de una lista. 
# numeros.reverse() 
# print(numeros)

# # #funcion sort(). Asigna sobre la misma variable
# # #ordena los elementos de una lista. 
# system('cls')
# print(numeros)
# numeros.pop(-1)
# print(numeros)
# numeros.sort()
# print(numeros)
# numeros.sort(reverse=True)
# print(numeros)

# #########################################################
# # Numeros primos
# #########################################################
# # Es un número natural.
# # Es mayor que 1.
# # Son divisibles por sí mismo y por 1.

# #Versión 1
# rangoFinal  = 5
# listaPrimos = []
# for numeroActual in range(2,rangoFinal+1):

#     contadorDivisores = 0
#     # ciclo interno para identificar si tiene más de un divisor
#     for divisor in range(2,numeroActual+1):
#         if (numeroActual % divisor == 0):
#            contadorDivisores +=1


#      #  Si no tiene más de un divisor
#     if contadorDivisores <=1 :
#         listaPrimos.append(numeroActual)

# print("Lista de Primos :",listaPrimos )


# #Versión 2

# rangoFinal  = 5
# listaRango = list(range(2,rangoFinal+1))


# listaPrimos = []
# for numeroActual in listaRango:

#     contadorDivisores = 0
#     # ciclo interno para identificar si tiene más de un divisor

#     listaDivisor = list(range(2,numeroActual+1))
#     for divisor in listaDivisor:
#         if (numeroActual % divisor == 0):
#            contadorDivisores +=1


#      #  Si no tiene más de un divisor
#     if contadorDivisores <=1 :
#         listaPrimos.append(numeroActual)

# print("Lista de Primos :",listaPrimos )
