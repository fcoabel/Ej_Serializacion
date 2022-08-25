import os
from tkinter import messagebox
import Interfaz
import pickle


# ------ Clase Contacto ------
class Contacto:
    def __init__(self, n, a, t):
        self.nombre = n
        self.apellidos = a
        self.numero = t

    def __str__(self):
        print(self.nombre, self.apellidos, self.numero)


# -----------------------------
# variable estática con el nombre del archivo que vamos a manejar
__archivo__ = 'ej_s_contactos'

# método que escribe la información el el fichero
def escribirFichero(x):
    ar = open(__archivo__, "wb")
    pickle.dump(x, ar)
    ar.close()
    del ar


# método para abrir el fichero y devolver la información contenida
def abrirFichero():
    try:
        if os.stat(__archivo__).st_size != 0:
            with open(__archivo__, "rb") as f:
                x = pickle.load(f)
                return x
        else:
            messagebox.showinfo("Archivo Vacío", "El archivo está vacío.")
    except:
        messagebox.showerror("Error", "Error al leer el archivo")


if __name__ == '__main__':
    Interfaz.mainloop()
