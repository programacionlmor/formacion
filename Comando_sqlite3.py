"""
  Comandos sqlite3

  Autor :  Formador
|
  Creación/ Actualización  Observaciones
     Junio-07-2021          Versión inicial del programa
     
"""
#########################################################################################
# Tipos de bases de datos
# Lectura: https://www.matillion.com/resources/blog/the-types-of-databases-with-examples 
########################################################################################## 


#########################
# Crear una base datos
# ########################

# .open nombrebase.db

##########################################
# Crear tabla en la base de datos
#
# CREATE TABLE table_name (
#     column1 datatype,
#     column2 datatype,
#     column3 datatype,
#    ....
# );
##########################################


# create table triangulo(
#     id_triangulo  text primary key,
#     lado_uno_triangulo Text,
#     lado_dos_triangulo text,
#     lado_tres_triangulo text
# );


# ####################################################
# insertar registro en tabla  de la base de datos
#
# INSERT INTO table_name (column1, column2, column3, ...)
# VALUES (value1, value2, value3, ...);
#########################################################

#  insert into triangulo VALUES ("1","20","30","40");


####################################################
# consultar registro en tabla de la base de datos
# SELECT column1, column2, ...
# FROM table_name;
#
# SELECT column1, column2, ...
# FROM table_name
# WHERE condition;
####################################################

# select * from triangulo;

# select * from triangulo where lado_uno_triangulo ="20";

# ##################################################
# actualizar registro en tabla de la base de datos
# UPDATE table_name
# SET column1 = value1, column2 = value2, ...
# WHERE condition;
#####################################################

#update triangulo set lado_uno_triangulo ="50";

#################################################
#  borrar registro en tabla de la base de datos
#  DELETE FROM table_name WHERE condition;
##################################################

#delete from triangulo;

