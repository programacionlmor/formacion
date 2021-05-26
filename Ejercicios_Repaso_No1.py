"""
  Ejercicios de repaso: Estructuras de decisión.
  
  Autor :  Formador
  Creación/ Actualización  Observaciones
     Mayo-26-2021          Versión inicial del programa
"""


# Nota generales:
# condicion: se crea utilizando operadores relacionales y lógicos


# Ejercicio No 1
# Dados los tres lados de un triangulo, determine si el triangulo es equilatero, isoceles o obtuso
# Triangulo equilatero: Tiene todos los lados iguales
# Triangulo isoceles:  Tiene dos lados iguales y uno desigual
# Triangulo escaleno:  Tiene todos los lados desiguales


# Alternativa 1
# ladoUno,ladoDos,ladoTres = input("Digite el valor del lado uno del triángulo   : "), \
#                            input("Digite el valor del lado dos del triángulo   : "), \
#                            input("Digite el valor del lado tres del triángulo  : ")


# if ((ladoUno == ladoDos) and (ladoDos == ladoTres)):
#     print (" El triangulo es equilatero")
# else:
#     if  (ladoUno == ladoDos) or (ladoUno == ladoTres) or (ladoDos == ladoTres):
#         print (" El triangulo es isóceles ")
#     else:
#         print ("El triangulo es escaleno")
        
        
# Alternativa 2

# ladoUno,ladoDos,ladoTres = input("Digite el valor del lado uno del triángulo   : "), \
#                            input("Digite el valor del lado dos del triángulo   : "), \
#                            input("Digite el valor del lado tres del triángulo  : ")


# if ((ladoUno == ladoDos) and (ladoDos == ladoTres)):
#     print (" El triangulo es equilatero")
# elif (ladoUno == ladoDos) or (ladoUno == ladoTres) or (ladoDos == ladoTres):
#      print (" El triangulo es isóceles ")
# else:
#      print ("El triangulo es escaleno")

# Alternativa 3

# ladoUno,ladoDos,ladoTres = input("Digite el valor del lado uno del triángulo   : "), \
#                            input("Digite el valor del lado dos del triángulo   : "), \
#                            input("Digite el valor del lado tres del triángulo  : ")


# if ((ladoUno != ladoDos) and (ladoDos != ladoTres) and (ladoUno != ladoTres)):
#     print (" El triangulo es escaleno")
# else:
#     if  (ladoUno == ladoDos == ladoTres):
#         print (" El triangulo es equilatero ")
#     else:
#         print ("El triangulo es isóceles ")

# Alternativa 4

# ladoUno,ladoDos,ladoTres = input("Digite el valor del lado uno del triángulo   : "), \
#                            input("Digite el valor del lado dos del triángulo   : "), \
#                            input("Digite el valor del lado tres del triángulo  : ")


# if ((ladoUno != ladoDos) and (ladoDos != ladoTres) and (ladoUno != ladoTres)):
#     print (" El triangulo es escaleno")
# elif (ladoUno == ladoDos == ladoTres):
#      print (" El triangulo es equilatero ")
# else:
#      print ("El triangulo es isóceles ")
