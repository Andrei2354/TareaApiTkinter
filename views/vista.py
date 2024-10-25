import tkinter as tk
from functools import wraps
from itertools import product
from shutil import which
from tkinter import ttk
from tkinter import *
import random
from typing import List
from tkinter import messagebox as alert

from PIL import ImageTk, Image
import requests
from models.Main import product_list
from models.ProductApi import Product
from models.empresa import Empresa

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
        categoria.set(f"{product_list.products[indice].category}")
        precio.set(f"Precio: {product_list.products[indice].price}")
        descuento.set(f"Descuento: {product_list.products[indice].discountPercentage}")
        marca.set(f"Marca: {product_list.products[indice].brand}")
        etiquetas.set(f"Etiquetas: {product_list.products[indice].tags[0]}")
        unidades.set(f"Cantidad en stock:{product_list.products[indice].stock}")
        valoracion.set(f"Valoración: {product_list.products[indice].rating}")


def indice_derecha():
    global indice
    indice += 1
    if indice < len(product_list.products):
        carrusel()
    else:
        indice = -1

def indice_izquierda():
    global indice
    indice -= 1
    if indice < len(product_list.products):
        carrusel()
    else:
        indice = 0

def buscar_indice():
    global entry_buscar, indice
    texto = entry_buscar.get().lower()
    for i in range(len(product_list.products)):
        if texto in product_list.products[i].title.lower():
            indice = i
            carrusel()
            break

def buscar_listado():
    global product_list
    texto = entry_buscar.get().lower()
    productos_busqueda = list(filter(lambda producto: texto in producto.title.lower(), product_list.products))
    productos_busqueda.sort(key=lambda producto: producto.title)
    mostrar_listado(productos_busqueda)

def mostrar_listado(productos: List[Product]):
    global entry_buscar, indice
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana secundaria")
    ventana_secundaria.config(width=300, height=200, background="#dff5f0")

    ttk.Label(ventana_secundaria, text="Productos", font=("Arial", 18, "bold"), background="#dff5f0").pack()
    for producto in productos:
        ttk.Label(ventana_secundaria, text=producto.title, background="#dff5f0", justify="left").pack()

    boton_buscar = ttk.Button(ventana_secundaria, text="Generar PDF", command="")
    boton_buscar.pack(padx=(0, 0))
    boton_cerrar = ttk.Button(ventana_secundaria,text="Cerrar ventana",command=ventana_secundaria.destroy)
    boton_cerrar.pack(padx=(0, 0))

def generarpdf(productos: List[Product]):
    empresa: Empresa = Empresa (
        nombre="Alvarikola Soft S.L",
        titular= "Alvarotech Industries López",
        cif="123456789",
        direccion="Calel",
        email="hola@alvarikola.com",
    )
    # Genero PDF (nombre=bsuqueda_resultado_202410241344SS.pdf)
    alert.showinfo("PDF generado", "Se ha generado el PDF correctamente")


def modelo_principal():
    global root, indice, contenido, label_imagen_producto, titulo1, descripcion, categoria, precio, descuento, marca, etiquetas, unidades, valoracion, entry_buscar

    style = ttk.Style()
    style.configure("1.TLabel", background="#fc9403")
    style.configure("2.TLabel", background="#8cd0d1")
    style.configure("3.TLabel", background="#dff5f0")

    titulo = ttk.Frame(root, style="1.TLabel",  width=800, height=100)
    titulo.pack(side="top", fill=X)

    buscadorArriba = ttk.Frame(root, style="2.TLabel", width=800, height=50)
    buscadorArriba.pack(side="top", fill=X, ipady="10")


    buscadorAbajo = ttk.Frame(root, style="2.TLabel", width=800, height=50)
    buscadorAbajo.pack(side="bottom", fill=X,  ipady="1")

    contenido = ttk.Frame(root, style="3.TLabel", width=800, height=750)
    contenido.pack(side="top", expand=True, fill=BOTH)

    contenido2 = ttk.Frame(contenido, style="3.TLabel", width=800, height=350)
    contenido2.pack(side="top", expand=True, fill=BOTH)

    contenidoDer = ttk.Frame(contenido2, style="3.TLabel", width=400, height=350)
    contenidoDer.pack(side="left", expand=True, fill=BOTH)

    contenidoIzq = ttk.Frame(contenido2, style="3.TLabel", width=400, height=350)
    contenidoIzq.pack(side="right", expand=True, fill=BOTH)

    imagenFrame = ttk.Frame(contenido, style="3.TLabel", width=800, height=400)
    imagenFrame.pack(side="top", expand=True, fill=BOTH)

    # Elementos dentro de los frames

    label1 = Label(titulo, text="Productos", background="#fc9403", font=("Times New Roman", 20, "bold"))
    label1.pack(side="top")

    label1 = Label(buscadorArriba, text="Buscar producto:", background="#8cd0d1")
    label1.pack(side="left", padx="10")


    entry_buscar = ttk.Entry(buscadorArriba, width=15)
    entry_buscar.pack(side="left", padx="10")

    boton_buscar = ttk.Button(buscadorArriba,text="Buscar",  command=buscar_indice)
    boton_buscar.pack(side="left", padx="10")

    boton_listado = ttk.Button(buscadorArriba,text="Listado",  command=buscar_listado)
    boton_listado.pack(side="left", padx="10")


    boton_izquierda = ttk.Button(buscadorAbajo, text="Anterior", command=indice_izquierda)
    boton_izquierda.pack(fill=NONE)
    boton_izquierda.place(x=300, y=10, anchor="nw")

    boton_derecha = ttk.Button(buscadorAbajo,text="Siguiente",  command=indice_derecha)
    boton_derecha.pack(fill=NONE)
    boton_derecha.place(x=400, y=10, anchor="nw")

    label_imagen_producto = ttk.Label(imagenFrame,background="#dff5f0", text="Jugar")
    label_imagen_producto.pack(side="bottom", ipady="2", ipadx="20")

    label_titulo = Label(contenidoDer, textvariable=titulo1 , background="#dff5f0", font=("Times New Roman", 15, "bold"))
    label_titulo.pack(ipady="12", ipadx="20")

    label_descripcion = Label(contenidoDer, textvariable=descripcion , background="#dff5f0", font=10, wraplength=400)
    label_descripcion.pack(ipady="12", ipadx="20")

    label_categoria = Label(contenidoDer, textvariable=categoria , background="#dff5f0")
    label_categoria.pack(ipady="12", ipadx="20")

    label_precio = Label(contenidoIzq, textvariable=precio , background="#dff5f0")
    label_precio.pack(ipady="12", ipadx="20")

    label_descuento = Label(contenidoIzq, textvariable=descuento , background="#dff5f0")
    label_descuento.pack(ipady="12", ipadx="20")

    label_valoracion = Label(contenidoIzq, textvariable=valoracion , background="#dff5f0")
    label_valoracion.pack(ipady="12", ipadx="20")

    label_unidades = Label(contenidoIzq, textvariable=unidades , background="#dff5f0")
    label_unidades.pack(ipady="12", ipadx="20")

    label_etiquetas = Label(contenidoIzq, textvariable=etiquetas, background="#dff5f0")
    label_etiquetas.pack(ipady="12", ipadx="20")

    label_brand = Label(contenidoIzq, textvariable=marca , background="#dff5f0")
    label_brand.pack(ipady="12", ipadx="20")

    carrusel()
    canvas.mainloop()



modelo_principal()