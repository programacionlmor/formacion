"""
  Tuplas  en python
  Autor :  Formador
|
  Creación/ Actualización  Observaciones
     Mayo-28-2021          Versión inicial del programa
"""

#Proponer una representación con tuplas para las cartas de una baraja. 

# import random

# def seleccionarCarta(numeroPalo:int, numeroCara:int) ->tuple:
#     caras = ("As ", "Dos ", "Tres ", "Cuatro ", "Cinco ", "Seis ",  "Siete ", "Ocho ", "Nueve ", "Diez ", "Joker ", "Reina ", "Rey ")
#     palos = ("Corazones ", "Diamantes ", "Treboles ", "Espadas ")

#     carta =  (caras[numeroCara],palos [numeroPalo])
  
#     return carta


# aleatorioCara = random.randint(0, 12)
# aleatorioPalo = random.randint(0, 3)

# print(seleccionarCarta (aleatorioPalo,aleatorioCara))


# Sacar cuatro  cartas al azar. Si se obtiene para las cuatro cartas la misma cara sin importar el palo, el jugador gana


# import random

# def seleccionarCarta(numeroPalo:int, numeroCara:int) ->tuple:
#     caras = ("As ", "Dos ", "Tres ", "Cuatro ", "Cinco ", "Seis ",  "Siete ", "Ocho ", "Nueve ", "Diez ", "Joker ", "Reina ", "Rey ")
#     palos = ("Corazones ", "Diamantes ", "Treboles ", "Espadas ")

#     carta =  (caras[numeroCara],palos [numeroPalo])
  
#     return carta


# aleatorioCara = random.randint(0, 12)
# aleatorioPalo = random.randint(0, 3)
  
# listaCartas = []
# for lanzada in range(1,5):

#     aleatorioCara = random.randint(0, 12)
#     aleatorioPalo = random.randint(0, 3)

#     cartaAleatoria = seleccionarCarta (aleatorioPalo,aleatorioCara)
#     listaCartas.append(cartaAleatoria)

# print(listaCartas)


# if (listaCartas[0][1] == listaCartas[1][1] ==  listaCartas [2][1] ==  listaCartas[3][1] == listaCartas[4][1]):
#     print("Ganador")
# else:
#     print("Inténtalo nuevamente")



#Escribir una función que reciba dos vectores que parten del origen (0,0) y devuelva su producto escalar


# valorX1 = 3
# valorY1 = 5


# valorX2 = 1
# valorY2 = 3


# tuplaVector1 = (valorX1,valorY1)
# tuplaVector2 = (valorX2,valorY2)

# productoPunto = tuplaVector1[0] * tuplaVector2[0] + tuplaVector1[1] * tuplaVector2[1]
# print(productoPunto )



# Escribir una función que reciba dos vectores y devuelva si son o no ortogonales 
# (perpendiculares) ProductoPunto = 0



# valorX1 = 3
# valorY1 = 5
# valorX2 = 1
# valorY2 = 3

# valorX1 = 0
# valorY1 = 1
# valorX2 = 1
# valorY2 = 0


# tuplaVector1 = (valorX1,valorY1)
# tuplaVector2 = (valorX2,valorY2)

# productoPunto = tuplaVector1[0] * tuplaVector2[0] + tuplaVector1[1] * tuplaVector2[1]

# if (productoPunto == 0):
#     print("Los vectores son ortogonales" )
# else:
#     print("Los vectores No son ortogonales" )



# Dada una lista de números enteros y un entero k, escribir una programa que:
# Devuelva tres listas, una con los menores, otra con los mayores y otra con
# los iguales a k.

# tamanoLista = int(input("Digite el tamaño de la lista de numeros enteros :"))

# lista=[]

# for numeroEntero in range(tamanoLista):
#     valorLista = int(input("Ingrese valor para llenar la lista: "))
#     lista.append(valorLista)


# valorReferencia = int(input("Ingrese valor de referencia K: "))


# listaMayores=[]
# for numeroEntero in range(tamanoLista):
#     if lista[numeroEntero] > valorReferencia:
#        listaMayores.append(lista[numeroEntero])


# listaMenores=[]
# for numeroEntero in range(tamanoLista):
#     if lista[numeroEntero] < valorReferencia:
#        listaMenores.append(lista[numeroEntero])



# listaIguales=[]
# for numeroEntero in range(tamanoLista):
#     if lista[numeroEntero] ==  valorReferencia:
#        listaIguales.append(lista[numeroEntero])


# print("mayores a ", valorReferencia," son ",listaMayores)
# print("menores a ",valorReferencia, " son ",listaMenores)
# print("iguales a ",valorReferencia, " son ",listaIguales)






