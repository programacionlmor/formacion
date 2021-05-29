"""
  Ejercicios de repaso: Estructuras de decisión.
  
  Autor :  Formador
  Creación/ Actualización  Observaciones
     Mayo-26-2021          v1: Versión inicial del programa.
     Mayo-29-2021          v2: Se incluye el perímetro del triángulo.
"""


# Notas generales:
# condición: se crea utilizando operadores relacionales o de comparación y lógicos
# Operadores relacionales:
#    “==” se usa para determinar si dos valores son exactamente iguales. Ejemplo: 2 == 2    Resultado: true
#    “!=” se usa para determinar Si dos valores son diferentes. Ejemplo: 2 != 5  Resultado:  true
#    “>”  se usa para determinar si el valor de la izquierda es mayor que el de la derecha. Ejemplo: 4 > 2  Resultado:true
#    “<“  se usa para determinar si el valor de la izquierda es menor que el de la derecha. Ejemplo: 1 < 2  Resultado:true
#    ">=” se usa para determinar si el valor de la izquierda es mayor o igual que el de la derecha. Ejemplo: 4 >= 2  Resultado:true
#    "<=" se usa para determinar si el valor de la izquierda es menor o igual que el de la derecha. Ejemplo: 4 <= 6  Resultado:true
# Operadores lógicos:
#   "and"  :  Si y sólo si todos los elementos son True dará por resultado True. Sino False.
#   "or"   :  Si algún elemento es True dará por resultado True. Sino False.
#   "Not"  :  El operador “not” es unario, de negación por ende solo dará True si su elemento es False y viceversa.



# Ejercicio No 1
# Dados los tres lados de un triángulo, determine si el triángulo es equilátero, isósceles o  escaleno.
# Triángulo equilatero:  Tiene todos los lados iguales.
# Triángulo isósceles :  Tiene dos lados iguales y uno desigual.
# Triángulo escaleno  :  Tiene todos los lados desiguales.


# Alternativa 1
# ladoUno,ladoDos,ladoTres = input("Digite el valor del lado uno del triángulo   : "), \
#                            input("Digite el valor del lado dos del triángulo   : "), \
#                            input("Digite el valor del lado tres del triángulo  : ")

##Identificar el tipo de triángulo
# if (ladoUno == ladoDos) and (ladoDos == ladoTres):
#     print ("El triangulo es equilátero")
# else:
#     if  (ladoUno == ladoDos) or (ladoUno == ladoTres) or (ladoDos == ladoTres):
#         print ("El triángulo es isósceles ")
#     else:
#         print ("El triángulo es escaleno")
        
        
# Alternativa 2

# ladoUno,ladoDos,ladoTres = input("Digite el valor del lado uno del triángulo   : "), \
#                            input("Digite el valor del lado dos del triángulo   : "), \
#                            input("Digite el valor del lado tres del triángulo  : ")

##Identificar el tipo de triángulo
# if (ladoUno == ladoDos) and (ladoDos == ladoTres):
#     print ("El triángulo es equilátero")
# elif (ladoUno == ladoDos) or (ladoUno == ladoTres) or (ladoDos == ladoTres):
#      print ("El triángulo es isósceles ")
# else:
#      print ("El triángulo es escaleno")

# Alternativa 3

# ladoUno,ladoDos,ladoTres = input("Digite el valor del lado uno del triángulo   : "), \
#                            input("Digite el valor del lado dos del triángulo   : "), \
#                            input("Digite el valor del lado tres del triángulo  : ")

##Identificar el tipo de triángulo
# if (ladoUno != ladoDos) and (ladoDos != ladoTres) and (ladoUno != ladoTres):
#     print ("El triángulo es escaleno")
# else:
#     if  (ladoUno == ladoDos == ladoTres):
#         print ("El triángulo es equilátero ")
#     else:
#         print ("El triángulo es isósceles ")

# Alternativa 4

# ladoUno,ladoDos,ladoTres = input("Digite el valor del lado uno del triángulo   : "), \
#                            input("Digite el valor del lado dos del triángulo   : "), \
#                            input("Digite el valor del lado tres del triángulo  : ")

##Identificar el tipo de triángulo
# if (ladoUno != ladoDos) and (ladoDos != ladoTres) and (ladoUno != ladoTres):
#     print ("El triángulo es escaleno")
# elif (ladoUno == ladoDos == ladoTres):
#      print ("El triángulo es equilátero ")
# else:
#      print ("El triángulo es isósceles ")


##################################################################################################
#
# VERSION 2 :  Incluir el perímetro del triángulo
# 
##################################################################################################

# Ejercicio No 2
# 1. Dados los tres lados de un triángulo, determine si el triángulo es equilátero, isósceles o  escaleno.
#    Triángulo equilatero:  Tiene todos los lados iguales.
#    Triángulo isósceles :  Tiene dos lados iguales y uno desigual.
#    Triángulo escaleno  :  Tiene todos los lados desiguales.
# 2. Calcular el perímetro del triángulo
#    El Perímetro del triángulo es igual a la suma de los lados.


# Alternativa 2 - con caracteres -

# ladoUno,ladoDos,ladoTres = input("Digite el valor del lado uno del triángulo   : "), \
#                            input("Digite el valor del lado dos del triángulo   : "), \
#                            input("Digite el valor del lado tres del triángulo  : ")

##Identificar el tipo de triángulo
# if (ladoUno == ladoDos) and (ladoDos == ladoTres):
#      print ("El triángulo es equilátero")
# elif (ladoUno == ladoDos) or (ladoUno == ladoTres) or (ladoDos == ladoTres):
#       print ("El triángulo es isósceles ")
# else:
#       print ("El triángulo es escaleno")

##Calcular el perímetro del triángulo
# perimetroTriangulo = ladoUno + ladoDos + ladoTres  #  Concatena los valores
# print("El perimetro del triángulo es", perimetroTriangulo)

# Alternativa 2 - con valores convertidos a enteros -

# ladoUno,ladoDos,ladoTres = input("Digite el valor del lado uno del triángulo   : "), \
#                            input("Digite el valor del lado dos del triángulo   : "), \
#                            input("Digite el valor del lado tres del triángulo  : ")

# #Convertir los lados del triángulo de cadena a entero
# ladoUno  = int(ladoUno)
# ladoDos  = int(ladoDos)
# ladoTres = int(ladoTres)


# #Identificar el tipo de triángulo
# if (ladoUno == ladoDos) and (ladoDos == ladoTres):
#      print ("El triángulo es equilátero")
# elif (ladoUno == ladoDos) or (ladoUno == ladoTres) or (ladoDos == ladoTres):
#       print ("El triángulo es isósceles ")
# else:
#       print ("El triángulo es escaleno")


# #Calcular el perímetro del triángulo
# perimetroTriangulo = ladoUno + ladoDos + ladoTres
# print("El perimetro del triángulo es", perimetroTriangulo)


