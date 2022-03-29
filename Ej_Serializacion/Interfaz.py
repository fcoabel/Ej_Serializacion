import os
from tkinter import *
from tkinter import messagebox

import ejecutable
from ejecutable import Contacto
# lista estática de contactos
__contactos__ = ejecutable.abrirFichero()
# volcamos los datos del fichero a la lista
__contactos__ = []


# Funciones

# método para añadir el objeto a la lista de contactos y añadirlo al fichero
def alta():
    # strip quita los espacios en blanco de los entries
    if len(nombreE.get().strip()) != 0 and len(apellidosE.get().strip()) != 0 and len(numeroE.get().strip()) != 0:
        # Creamos el objeto
        contactox = Contacto(nombreE.get(), apellidosE.get(), numeroE.get())
        if contactox in __contactos__:
            messagebox.showinfo("Existe", "Este contacto ya está creado.")
        else:
            __contactos__.append(contactox)
        # llamamos al metodo de añadir al fichero el objeto creado
        ejecutable.escribirFichero(__contactos__)
        messagebox.showinfo("Alta", "Contacto Añadido.")
    else:
        messagebox.showerror("Error", "Compruebe que los campos estén completos.")

# método para borrar el objeto indicado
def borrar():
    if len(nombreE.get().strip()) != 0 and len(apellidosE.get().strip()) != 0 and len(numeroE.get().strip()) != 0:
        objAquitar = Contacto(nombreE.get(), apellidosE.get(), numeroE.get())
        for x in __contactos__:
            if objAquitar.nombre == x.nombre:
                __contactos__.remove(x)
                break
        ejecutable.escribirFichero(__contactos__)
        messagebox.showinfo("Eliminar", "Eliminado correctamente")
    else:
        messagebox.showerror("Error", "Faltan campos por rellenar")


# método para mostrar los objetos del archivo
def listar():
    __contactos__ = ejecutable.abrirFichero()
    ventanaAux = Toplevel()
    ventanaAux.title(os.path.dirname(os.path.abspath(ejecutable.__archivo__)))
    mostrar = Text(ventanaAux, width=55, height=20)
    if len(__contactos__) != 0:
        for i in range(len(__contactos__)):
            mostrar.insert(INSERT,
                           "NOMBRE -> " + __contactos__[i].nombre +
                           " APELLIDO -> " + __contactos__[i].apellidos +
                           " NÚMERO -> " + __contactos__[i].numero + "\n")
    else:
        messagebox.showinfo("Info", "El archivo está vacío.")
    mostrar.grid(row=1, column=1)


def modificar():
    # para modificar introduciremos el nombre del contacto que queremos modificar
    # solo podremos modificar el número de telefono del contacto y el apellido de este.
    if len(nombreE.get().strip()) != 0:
        for x in __contactos__:
            if x.nombre == nombreE.get():
                x.apellidos = apellidosE.get()
                x.numero = numeroE.get()
                ejecutable.escribirFichero(x)
    else:
        messagebox.showinfo("Atención", "Escriba el nombre del contacto que quiera modificar.")


# método para mostrar la ruta donde se encuentra el fichero
def mostrarRuta():
    directorio = os.path.dirname(os.path.abspath(ejecutable.__archivo__))
    eArchivo.insert(0, directorio)


raiz = Tk()

# Características de la ventana
raiz.title("Ej Serialización - tkinter")
raiz.resizable(1, 1)
raiz.config(bg="#565656")

# Frame Datos
frameD = LabelFrame(
    raiz,
    text="Datos",
    font=50,
    fg="white"
)
frameD.grid(padx=10, sticky="e")
frameD.config(
    bg="#2B2B2B",
    width="600",
    height="400"
)

# Labels Datos
nombreL = Label(frameD, text="Nombre: ", font=20)
nombreL.config(bg="#2B2B2B", fg="#ffffff", justify="right")
nombreL.grid(row=0, column=0, padx=5, pady=5)

apellidosL = Label(frameD, text="Apellidos: ", font=20)
apellidosL.config(bg="#2B2B2B", fg="#ffffff", justify="right")
apellidosL.grid(row=1, column=0, padx=5, pady=5)

numeroL = Label(frameD, text="Número: ", font=20)
numeroL.config(bg="#2B2B2B", fg="#ffffff", justify="right")
numeroL.grid(row=2, column=0, padx=5, pady=5)

# Cuadros de texto
nombreE = Entry(frameD)
nombreE.grid(row=0, column=1, padx=5, pady=5)

apellidosE = Entry(frameD)
apellidosE.grid(row=1, column=1, padx=5, pady=5)

numeroE = Entry(frameD)
numeroE.grid(row=2, column=1, padx=5, pady=5)

# Frame Botones
frameB = Frame(raiz)
frameB.grid(padx="10", pady="10", sticky="s")

# Botones
bAnadir = Button(
    frameB,
    text="Añadir",
    bg="#527957",
    command=lambda: alta()
)
bAnadir.pack(side="left")

bBorrar = Button(
    frameB,
    text="Borrar",
    bg="#FF7B82",
    command=lambda: borrar()
)
bBorrar.pack(side="left")

bListar = Button(
    frameB,
    text="Listar",
    bg="#2175C8",
    command=lambda: listar()
)
bListar.pack(side="left")

bModificar = Button(
    frameB,
    text="Modificar",
    bg="#F0A732",
    command=lambda: modificar()
)
bModificar.pack(side="left")

# frame seleccionar fichero
frameMR = LabelFrame(
    raiz,
    text="Mostrar Ruta",
    font=50,
    fg="white")
frameMR.grid(padx="10", pady="10", sticky="w")
frameMR.config(
    bg="#2B2B2B",
    width="200",
    height="50"
)

# elemenentos frame SF
eArchivo = Entry(frameMR)
eArchivo.grid(
    row=0,
    column=0
)

bMostrarRuta = Button(
    frameMR,
    text="Mostrar Directorio",
    command=lambda: mostrarRuta()
)
bMostrarRuta.grid()

raiz.mainloop()
