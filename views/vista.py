import tkinter as tk
from itertools import product
from shutil import which
from tkinter import ttk
from tkinter import *
import random
from PIL import ImageTk, Image
import requests

from models.Main import product_list
label_imagen_producto = ""
def carrusel():
    global indice, contenido, label_imagen_producto
    if indice < len(product_list.products):
         bits_imagen = requests.get(product_list.products[indice].thumbnail, stream=True)
         imagen = Image.open(bits_imagen.raw)
         imagen_tk = ImageTk.PhotoImage(imagen)
         label_imagen_producto.config(image=imagen_tk)
         label_imagen_producto.image = imagen_tk


def modelo_principal():
    global indice, contenido, label_imagen_producto
    root = tk.Tk()  # Ventana principal
    canvas = tk.Canvas(root)
    root.geometry("800x800")

    style = ttk.Style()
    style.configure("1.TLabel", background="#fc9403")
    style.configure("2.TLabel", background="#8cd0d1")
    style.configure("3.TLabel", background="#dff5f0")

    titulo = ttk.Frame(root, style="1.TLabel",  width=800, height=100)
    titulo.pack(side="top", fill=X)

    label1 = Label(titulo, text="Productos", background="#fc9403")
    label1.pack(ipady="12", ipadx="20")

    buscador = ttk.Frame(root, style="2.TLabel", width=800, height=50)
    buscador.pack(side="top", fill=X)

    contenido = ttk.Frame(root, style="3.TLabel", width=800, height=750)
    contenido.pack(side="top", expand=True, fill=BOTH)

    resultado = tk.StringVar()
    indice = 1


    boton_resultado = ttk.Button(contenido, textvariable=resultado)
    boton_resultado.pack(side="bottom", fill=NONE)

    label_imagen_producto = ttk.Label(contenido,background="#dff5f0", text="Jugar")
    label_imagen_producto.pack(side="bottom", ipady="2", ipadx="20")

    carrusel()
    canvas.mainloop()



modelo_principal()