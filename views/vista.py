import tkinter as tk
from itertools import product
from shutil import which
from tkinter import ttk
from tkinter import *
import random
from models.Main import product_list

def modelo_principal():
    root = tk.Tk()  # Ventana principal
    canvas = tk.Canvas(root)
    root.geometry("800x800")

    style = ttk.Style()
    style.configure("1.TLabel", background="#fc9403")
    style.configure("2.TLabel", background="#8cd0d1")
    style.configure("3.TLabel", background="#dff5f0")

    titulo = ttk.Frame(root, style="1.TLabel",  width=800, height=100)
    titulo.pack(side="top", fill=X)

    label1 = Label(titulo, text="Productos").pack(ipady="12", ipadx="20")
    label1.config(bg="green")

    buscador = ttk.Frame(root, style="2.TLabel", width=800, height=50)
    buscador.pack(side="top", fill=X)

    contenido = ttk.Frame(root, style="3.TLabel", width=800, height=750)
    contenido.pack(side="top", expand=True, fill=BOTH)

    resultado = tk.StringVar()
    for product in product_list.products:
        resultado.set(product.title)


    boton_resultado = ttk.Button(contenido, textvariable=resultado)
    boton_resultado.pack(side="bottom", fill=NONE)
    canvas.mainloop()

modelo_principal()