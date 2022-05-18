"""
 variaciones del operardor asignación
 precedencia de operadores


 Autor:  Formador
 
 Fecha Creación/Actualización   Observación
  Mayo-11-2021                   Versión inicial

"""

#  Convenciones para el nombramiento de variables
# - No usar simbolos especiales !, @, #, $, %, etc. 
# - No inicie el nombre con un número digito.
# - Los nombres de variables deben tener una combinación de letras en minúsculas (a a z), mayúsculas (A a Z) 
# , dígitos (0 a 9) o un guión bajo (_). 
# - Nombres con sentido.!!

#!notaUno = 10
#notaUno@ = 10
#nota%Uno = 10
#1notaUno = 10

#1 Camel Case   -- > contarElementos
#2 Pascal Case  ---> ContarElementos
#3 Snake Case   ---> contar_elementos
#4 Kebab Case   ---> contar-elementos

# Variaciones del operador de asignación

notaUno     = 10
notaDos     = 10
notaTres    = 10

# Asignación de un solo valor a varias variables

notaUno = notaDos = notaTres = 10

notaUno = notaDos = notaTres = input("Digite el valor de la nota que es igual para todas las notas")

print(notaUno)
print(notaDos)
print(notaTres)

## Asignar varios valores a varias variables


notaUno, notaDos, notaTres = input("Digite Nota Uno :"), input("Digite Nota Dos :"), input("Digite Nota Tres:")
notaUno, notaDos, notaTres = input().split()
notaUno, notaDos, notaTres = input(), input(), input()

notaUno, notaDos, notaTres = 10 , 5 , 6
print(notaUno)
print(notaDos)
print(notaTres)

# Asignación con suma, resta, multiplicación, division, division entera, modulo.

valor = 2
valor = valor + 1
print(valor)

valor  = 10
valor += 1
print(valor)


valor -= 1
print(valor)
valor = valor/5
print(valor)
valor /=5
print(valor)
valor *=2
print(valor)
valor %=2
print(valor)













#Tipos de datos en python
#Python tiene varios tipos de datos integrados , como números (enteros, flotantes, números complejos), cadenas, listas, tuplas y diccionarios.

# 1. Números Enteros
print(0)
print(1)
print(-14)
print(32424234234) 
print(type(0))
print(type(-1))
#Los enteros en Python 3 pueden ser de cualquier tamaño, solo estan limitados por la memoria disponible


#2. Números de punto flotante (reales)
print(1.9)
print(4e7)
print(4e-4)
print(type(4e-4))
print(type(4e7))
print(type(1.9))


# IEEE 754: 64-bit “double-precision” max: 1.8e308
print(1.81e308)
print(1.8e307)
print(1.7e308)


"""
La conversión entre tipos de datos en python ocurre de dor formas:
1. Conversión implicita. (La realiza Python en tiempo de ejecución)
2. Conversión explicita. (El programador la definio)
"""
#1. Conversión implicita
numeroEntero = 4
numeroFlotante = 1.5

suma = numeroEntero + numeroFlotante

print(type(suma)) #El resultante es un Float. 

#2. Conversión explicita (Type Casting)
#2.1.Conversión en tipos de datos primitivos: Integers, Float, Strings, Boolean

sumaFlotante =  float(1 +2)  #Entero a flotante
print(sumaFlotante)

sumaEntera = int( 3.3 + 2.8) #Flotant a entero
print(sumaEntera)

sumaCadenas = "hola" + " "+ "mundo"  #Para conversiones a partir de strings si contienen valores compatibles.
print(sumaCadenas)


""" funcionan ok
sumaCadenas = float("hola") + float("mundo") 
print(sumaCadenas)

sumaCadenas = float("1") + float("2") 
print(sumaCadenas)

sumaCadenas = int("1") + int("2") 
print(sumaCadenas)

"""

enteroCadena = str(1) # Conversion de entero a cadena
print(enteroCadena)


floatCadena = str(1.5) # Conversion de flotante a cadena
print(floatCadena)






# Operadores Aritméticos
# Los operadores de suma, resta, multiplicación y división pueden ser usadas con números.

#| Operación | Resultado       |
#| --------- | --------------- |
#|    +      | Suma            |
#|    -      | Resta           |
#|    *      | Multiplicación  |
#|    /      | División        |
#|    //     | División entera |
#|    \*\*   | Potencia        |


## 5. Operadores aritméticos basicos
numeroUno = 2
numeroDos = 4

#suma
suma = numeroUno + numeroDos
print(suma)

#resta
resta = numeroDos - numeroUno
print(resta)

#negacion
negacionResta = -resta
print(negacionResta)

#División
division = numeroDos/numeroUno
print(division)

#Exponente
expo = numeroDos ** numeroUno
print(expo)

#Módulo
modulo = numeroDos % numeroUno
print(modulo)

cociente = numeroDos // numeroUno
print(cociente)

#Raiz Cuadrada
sqrt = numeroDos**(1/2) # raiz cuadrada


#Que pasa si opero una cadena de caracteres y un numero
suma = 10 + "a" #Error de type





## 8. Operadores relacionales. Evaluan expresiones de verdad.


valorBooleano = (4 == 3) # == El operador == evalua que los valores sean iguales.
print(valorBooleano)

valorBooleano = (4 != 3) # != El operador != evalua si los valores son distintos.
print(valorBooleano)

valorBooleano = (4 > 3) # Operadores de comparación <,>,<=,>=
print(valorBooleano)

valorBooleano = (4 < 3) # Operadores de comparación <,>,<=,>=
print(valorBooleano)

valorBooleano = (4 >= 3) # Operadores de comparación <,>,<=,>=
print(valorBooleano)

valorBooleano = (4 <= 3) # Operadores de comparación <,>,<=,>=
print(valorBooleano)



valorBooleano = ("Amigo" == 5)

valorBooleano = ("Amigo" == "Panas")


type("Amigo") == str

# != El operador != evalua si los valores son distintos.
5 != 3
5 != 5

# Operadores de comparación <,>,<=,>=
5 < 3
5 > 3
5 <= 3
5 >= 3


#sumaNotas = notaUno + notaDos +notaTres
#print(sumaNotas)

# precedencia de operadores
#1. ()
#2. **
#3. *, /, //, %
#4. +, -

operacion =  4 + 2 * (3 -1)
          =  4 +2*(2)

print(operacion)

