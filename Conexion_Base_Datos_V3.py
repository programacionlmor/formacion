"""
  Interfaz gráfica y Conexión a Base de Datos

  Autor :  Formador
|
  Creación/ Actualización  Observaciones
     Junio-07-2021          Versión inicial del programa
     
"""


###############################
# VERSION 0 : Interfaz gráfica
###############################

# from tkinter import Tk
# # Crear la ventana Principal
# ventanaPrincipal = Tk()

# # Mostrar la ventana
# ventanaPrincipal.mainloop()



###############################
# VERSION 1 : Interfaz gráfica
###############################

# from tkinter import Button, Entry, Label,Tk,messagebox,Menu



# def crearCampos():
    
#     labelNumeroTriangulo = Label(ventanaPrincipal,text="No Triángulo",bg = "cyan")
#     labelNumeroTriangulo.grid(padx=30,pady=30, column=4,row=0)
#     idTriangulo        = Entry(ventanaPrincipal,width=20)
#     idTriangulo.grid(column=5,row=0)

#     labelLadoUno         = Label(ventanaPrincipal,text="Lado Uno",bg = "cyan")
#     labelLadoUno.grid(padx=30, column=2,row=1)
#     ladoUnoTriangulo   = Entry(ventanaPrincipal,width=15)
#     ladoUnoTriangulo.grid(column=3,row=1)

#     labelLadoDos         = Label(ventanaPrincipal,text="Lado Dos",bg = "cyan")
#     labelLadoDos.grid(padx=30, column=4,row=1)
#     ladoDosTriangulo   = Entry(ventanaPrincipal,width=15)
#     ladoDosTriangulo.grid(column=5,row=1)

#     labelLadoTres        = Label(ventanaPrincipal,text="Lado Tres",bg = "cyan")
#     labelLadoTres.grid(padx=30,column=6,row=1)
#     ladoTresTriangulo  = Entry(ventanaPrincipal,width=15)
#     ladoTresTriangulo.grid(column=7,row=1)

#     return idTriangulo, ladoUnoTriangulo,ladoDosTriangulo,ladoTresTriangulo

# def crearBotones():
#     botonInsertar   = Button(ventanaPrincipal,text="Crear Δ ",bg = "pink")
#     botonInsertar.grid(pady=50,column=3,row=10)
#     botonBorrar     = Button(ventanaPrincipal,text="Consultar Δ ",bg = "pink")
#     botonBorrar.grid(column= 5,row=10)
#     botonConsultar  = Button(ventanaPrincipal,text="Borrar Δ ",bg = "pink")
#     botonConsultar.grid(column=7,row=10)

#     return botonInsertar,botonBorrar,botonConsultar

# def salirAplicacion():
#     if messagebox.askyesno(message="¿Desea Salir de la Aplicación?",title="Advertencia"):
#        ventanaPrincipal.destroy()



# # Crear la ventana Principal
# ventanaPrincipal = Tk()
# ventanaPrincipal.title("Triángulos")
# ventanaPrincipal.geometry("800x500")


# # Crear campos de captura para el identificador y los lados del triángulo
# idTriangulo, ladoUnoTriangulo,ladoDosTriangulo,ladoTresTriangulo = crearCampos()

# # Crear los botones de crear, consultar y borrar un triángulo
# botonInsertar,botonBorrar,botonConsultar = crearBotones()



# # Crear el menu principal
# menuBarra = Menu(ventanaPrincipal)
# menuBarra.add_command(label="Salir", command=salirAplicacion)


# # Mostrar el menu
# ventanaPrincipal.config(menu=menuBarra)


# # Mostrar la ventana
# ventanaPrincipal.mainloop()





#############################################
# VERSION 2 - CONECTIVIDAD CON BASE DE DATOS
#############################################


# from sqlite3.dbapi2 import Cursor
# from tkinter import Button, Entry, Label, ttk, Tk,messagebox
# from tkinter import Menu

# import sqlite3



# def crearCampos():
    
#     labelNumeroTriangulo = Label(ventanaPrincipal,text="No Triángulo",bg = "cyan")
#     labelNumeroTriangulo.grid(padx=30,pady=30, column=4,row=0)
#     idTriangulo        = Entry(ventanaPrincipal,width=20)
#     idTriangulo.grid(column=5,row=0)

#     labelLadoUno         = Label(ventanaPrincipal,text="Lado Uno",bg = "cyan")
#     labelLadoUno.grid(padx=30, column=2,row=1)
#     ladoUnoTriangulo   = Entry(ventanaPrincipal,width=15)
#     ladoUnoTriangulo.grid(column=3,row=1)

#     labelLadoDos         = Label(ventanaPrincipal,text="Lado Dos",bg = "cyan")
#     labelLadoDos.grid(padx=30, column=4,row=1)
#     ladoDosTriangulo   = Entry(ventanaPrincipal,width=15)
#     ladoDosTriangulo.grid(column=5,row=1)

#     labelLadoTres        = Label(ventanaPrincipal,text="Lado Tres",bg = "cyan")
#     labelLadoTres.grid(padx=30,column=6,row=1)
#     ladoTresTriangulo  = Entry(ventanaPrincipal,width=15)
#     ladoTresTriangulo.grid(column=7,row=1)

#     return idTriangulo, ladoUnoTriangulo,ladoDosTriangulo,ladoTresTriangulo

# def crearBotones():
#     botonInsertar   = Button(ventanaPrincipal,text="Crear Δ ",bg="pink",command=insertarTriangulo)
#     botonInsertar.grid(pady=50,column=3,row=10)
#     botonBorrar     = Button(ventanaPrincipal,text="Consultar Δ ",bg="pink",command=consultarTriangulo)
#     botonBorrar.grid(column= 5,row=10)
#     botonConsultar  = Button(ventanaPrincipal,text="Borrar Δ ",bg = "pink",command=borrarTriangulo)
#     botonConsultar.grid(column=7,row=10)

#     return botonInsertar,botonBorrar,botonConsultar



# def conectarBD():
#     conexion = sqlite3.connect('C:\database\geometria.db')
#     cursor   = conexion.cursor()
#     return conexion,cursor


# def insertarTriangulo():
#     datos    = idTriangulo.get(),ladoUnoTriangulo.get(),ladoDosTriangulo.get(),ladoTresTriangulo.get()
#     try:
#           cursor.execute("INSERT INTO triangulo VALUES (?,?,?,?)",(datos))
#           conexion.commit()
#           messagebox.showinfo('Base de Datos','Triángulo insertado exitosamente')
#     except: 
#           messagebox.showwarning('ADVERTENCIA','Fallo en la inserción del triángulo')



# def borrarTriangulo():
#     if messagebox.askyesno(message="Los datos se perderán definitivamente. ¿Desea Continuar",title="Advertencia"):
#        sql = "DELETE FROM triangulo"
#     else:
#         pass
#     try: 
#      cursor.execute(sql)
#      conexion.commit()
#      messagebox.showinfo('Base de Datos','Los triángulos fueron borrados con éxito')

#     except:
#         messagebox.showwarning('ADVERTENCIA','Fallo borrando triángulos')

#     conexion.close()

# def consultarTriangulo():
#     registros = tablaConsulta.get_children()
#     for elemento in registros:
#         tablaConsulta.delete(elemento)
#     sql = "SELECT * from triangulo"
#     try:
#         cursor.execute(sql)
#         for row in cursor:
# #            tablaConsulta.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3]))
#             tablaConsulta.insert("",'end',text=row[0],values=(row[0],row[1],row[2],row[3]))
#     except:
#         messagebox.showwarning('ADVERTENCIA','Su consulta no arrojó resultados')

# def actualizarTriangulo():
#     pass

# def mostrarConsulta():

#     tablaConsulta= ttk.Treeview(height=10,columns=(0,1,2,3),show='headings')
#     tablaConsulta.heading (0,text ="No")
#     tablaConsulta.heading (1,text ="Lado Uno")
#     tablaConsulta.heading (2,text="Lado Dos")
#     tablaConsulta.heading (3,text="Lado Tres")
#     tablaConsulta.place(x=0,y=200)

#     return tablaConsulta


# def salirAplicacion():
#     if messagebox.askyesno(message="¿Desea Salir de la Aplicación?",title="Advertencia"):
#         conexion.close()
#         ventanaPrincipal.destroy()


# # Crear la ventana Principal
# ventanaPrincipal = Tk()
# ventanaPrincipal.title("Triángulos")
# ventanaPrincipal.geometry("800x500")


# # Crear campos de captura para el identificador y los lados del triángulo
# idTriangulo, ladoUnoTriangulo,ladoDosTriangulo,ladoTresTriangulo= crearCampos()

# # Crear los botones de crear, consultar y borrar un triángulo
# botonInsertar,botonBorrar,botonConsultar= crearBotones()

# # Conectarse a la base de datos
# conexion,cursor = conectarBD()


# # Crear tabla para la consulta de registros
# tablaConsulta =mostrarConsulta()



# # Crear el menu principal
# menuBarra = Menu(ventanaPrincipal)
# menuBarra.add_command(label="Salir", command=salirAplicacion)


# # Mostrar el menu
# ventanaPrincipal.config(menu=menuBarra)


# # Mostrar la ventana
# ventanaPrincipal.mainloop()
