"""
  Manejo de Archivos

  Autor :  Formador
|
  Creación/ Actualización  Observaciones
     Junio-08-2021          Versión inicial del programa
"""



####################################################################################################
# Leer un archivo de texto en python # 
# "r" - Read -  Valor por defecto. Abre el archivo para lectura. Saca error si el archivo no existe
# "x" - Create - Creará un archivo retornará un error si el archivo existe
# "a" - Append - Creará una arhivo si el archivo especificado no existe
# "w" - Write -  Creará un archivo si el archivo especificado no existe
#####################################################################################################

# try:
#     archivo = open("archivo_prueba.txt")  # Abre el archivo
#     #print(archivo.read())      # Lee todo el contenido del archivo.
#     #print(archivo.read(5))     # Lee cinco caracteres del archivo.
#     #print(archivo.readline())  # Lee la primera línea del archivo.
#     #print(archivo.readline())  # Lee la segunda línea del archivo.

#     for linea in archivo:       # Recorrer linea a linea el archivo por un for
#         print(linea,end="") 
#     archivo.close()             # Cerrar el archivo
#     archivo.readline()          # Genera excepción al no encontrarse el archivo abierto

# except:
#     print("\n Error procesando el archivo")


######################################
# Escribir en un archivo existente   # 
######################################

#try:
    # archivo = open("archivo_prueba.txt","a")             # Abre el archivo en modo append. Añade al final del archivo
    # archivo.write("Esta es una cuarta línea de prueba")  # Escribir en el archivo.
    # archivo.close()                                      # Cerrar el archivo

    # archivo = open("archivo_prueba.txt","r")             # Abre el archivo en modo lectura.
    # print(archivo.read() )

    # ------------------------------------------
    
    # archivo = open("archivo_prueba.txt","w") 
    # archivo.write("Vamos a sobreescribir todo el archivo")  #  Sobreescribir el archivo.
    # archivo.close()                                      # Cerrar el archivo
    # archivo = open("archivo_prueba.txt","r")             # Abre el archivo en modo lectura.
    # print(archivo.read() )


# except:
#     print("Error procesando el archivo")


#########################################################################
# Crear un archivo 
# 
# "x" - Create - Creará un archivo retornará un error si el archivo existe
# "a" - Append - Creará una arhivo si el archivo especificado no existe
# "w" - Write -  Creará un archivo si el archivo especificado no existe
#########################################################################

##########
# Caso 1
##########
# try:
#     archivo = open("archivo_prueba.txt","x") # Genera excepción porque el archivo ya existe
# except:
#     print("Error procesando el archivo")


##########
# Caso 2
##########
# try:
#     archivo = open("archivo_prueba.txt","w") # El archivo existe pero no genera excepción
#     archivoDos = open("archivo_prueba_dos.txt","w") #El archivo no existe y lo crea
# except:
#     print("Error procesando el archivo")


##########
# Caso 3
##########
# try:
#     archivo = open("archivo_prueba.txt","a") # El archivo existe pero no genera excepción
#     archivoTres = open("archivo_prueba_tres.txt","a") # El archivo no existe y lo crea
# except:
#     print("Error procesando el archivo")




#########################################################################
# Borrar un archivo 
# Se debe importar el modulo OS  y llamar el metodo remove 
#########################################################################

##########
# CASO 1
##########
# from os import remove
# try:
#    remove("archivo_prueba.txt")
# except:
#    print("Error procesando el archivo")

##########
# CASO 2
##########

# import os 
# if os.path.exists("archivo_prueba.txt"):
#    os.remove("archivo_prueba.txt")
# else:
#   print("The file does not exist")





