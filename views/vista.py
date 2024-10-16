import tkinter as tk
from itertools import product
from shutil import which
from tkinter import ttk
from tkinter import *
import random
from PIL import ImageTk, Image
import requests
from models.Main import product_list

root = tk.Tk()  # Ventana principal
canvas = tk.Canvas(root)
root.geometry("800x800")

label_imagen_producto = ""
indice = 0
categoria = tk.StringVar()
descuento = tk.StringVar()
marca = tk.StringVar()
unidades = tk.StringVar()
valoracion = tk.StringVar()
precio = tk.StringVar()
descripcion = tk.StringVar()
titulo = tk.StringVar()
etiquetas = tk.StringVar()
resultado = tk.StringVar()
titulo1 = tk.StringVar()

def carrusel():
    global root, indice, contenido, label_imagen_producto, titulo1, descripcion, categoria, precio, descuento, marca, etiquetas, unidades, valoracion
    if indice < len(product_list.products):
        bits_imagen = requests.get(product_list.products[indice].thumbnail, stream=True)
        imagen = Image.open(bits_imagen.raw)
        imagen_tk = ImageTk.PhotoImage(imagen)
        label_imagen_producto.config(image=imagen_tk)
        label_imagen_producto.image = imagen_tk

        titulo1.set(product_list.products[indice].title)
        descripcion.set(product_list.products[indice].description)
        categoria.set(product_list.products[indice].category)
        precio.set(product_list.products[indice].price)
        descuento.set(product_list.products[indice].discountPercentage)
        marca.set(product_list.products[indice].brand)
        etiquetas.set(product_list.products[indice].tags[0])
        unidades.set(product_list.products[indice].stock)
        valoracion.set(product_list.products[indice].rating)


def modelo_principal():
    global root, indice, contenido, label_imagen_producto, titulo1, descripcion, categoria, precio, descuento, marca, etiquetas, unidades, valoracion

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

    boton_resultado = ttk.Button(contenido, textvariable=resultado)
    boton_resultado.pack(side="bottom", fill=NONE)

    label_imagen_producto = ttk.Label(contenido,background="#dff5f0", text="Jugar")
    label_imagen_producto.pack(side="bottom", ipady="2", ipadx="20")

    label_titulo = Label(contenido, textvariable=titulo1 , background="#dff5f0")
    label_titulo.pack(ipady="12", ipadx="20")

    label_descripcion = Label(contenido, textvariable=descripcion , background="#dff5f0")
    label_descripcion.pack(ipady="12", ipadx="20")

    label_categoria = Label(contenido, textvariable=categoria , background="#dff5f0")
    label_categoria.pack(ipady="12", ipadx="20")

    label_precio = Label(contenido, textvariable=precio , background="#dff5f0")
    label_precio.pack(ipady="12", ipadx="20")

    label_descuento = Label(contenido, textvariable=descuento , background="#dff5f0")
    label_descuento.pack(ipady="12", ipadx="20")

    label_valoracion = Label(contenido, textvariable=valoracion , background="#dff5f0")
    label_valoracion.pack(ipady="12", ipadx="20")

    label_unidades = Label(contenido, textvariable=unidades , background="#dff5f0")
    label_unidades.pack(ipady="12", ipadx="20")

    label_etiquetas = Label(contenido, textvariable=etiquetas, background="#dff5f0")
    label_etiquetas.pack(ipady="12", ipadx="20")

    label_brand = Label(contenido, textvariable=marca , background="#dff5f0")
    label_brand.pack(ipady="12", ipadx="20")

    carrusel()
    canvas.mainloop()



modelo_principal()