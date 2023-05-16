# -*- coding: utf-8 -*-
"""
Ejemplo Nivel 4: Visor de imágenes

Temas:

* Matrices

@author: Cupi2
"""
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def cargar_imagen(ruta_imagen: str)-> list:
    """ Carga la imagen que se encuentra en la ruta dada.
    Parámetros:
        ruta_imagen (str) Ruta donde se encuentra la imagen a cargar.
    Retorno:
        list: Matriz de MxN con tuplas (R,G,B).
    """
    matriz = mpimg.imread(ruta_imagen).tolist()
    alto = len(matriz)
    ancho = len(matriz[0])
    imagen = []
    for i in range(alto):
        fila = []
        for j in range(ancho):
            r = matriz[i][j][0]
            g = matriz[i][j][1]
            b = matriz[i][j][2]
            tupla = (r, g, b)
            fila.append(tupla)
        imagen.append(fila)
    return imagen


def visualizar_imagen(imagen: list) -> None:
    """ Muestra la imagen recibida
    Parámetros:
        imagen (list): Matriz de MxN con tuplas (R,G,B) que representan la imagen a visualizar.
    """
    alto = len(imagen)
    ancho = len(imagen[0])
    matriz = []
    for i in range(alto):
        fila = []
        for j in range(ancho):
            r, g, b = imagen[i][j]
            fila.append([r, g, b])
        matriz.append(fila)
    plt.imshow(matriz)
    plt.show()


def convertir_negativo(imagen: list) -> list:
    """  Convierte la imagen en negativo.
    El negativo se calcula cambiando cada componente RGB, tomando el valor absoluto de restarle al componente 1.0.
    Parámetros:
        imagen (list) Matriz de MxN con tuplas (R,G,B) que representan la imagen a convertir a negativo.
    """
    matriz = []
    for i in range(len(imagen)):
        fila = []
        for j in range(len(imagen[0])):
            r, g, b = imagen[i][j]
            fila.append([abs(r-1), abs(g-1), abs(b-1)])
        matriz.append(fila)
    plt.imshow(matriz)
    plt.show()
    return matriz


def reflejar_imagen(imagen: list)->list:
    """Refleja la imagen.
    Consiste en intercambiar las columnas enteras de la imagen, de las finales a la iniciales.
    Parámetros:
        imagen (list) Matriz de MxN con tuplas (R,G,B) que representan la imagen a reflejar.
    """
    matriz = []
    for i in range(len(imagen)):
        fila = []
        fila = []
        for j in range(len(imagen[0])):
            r, g, b = imagen[i][j]
            fila.append([r, g, b])
        matriz.append(fila[::-1])
    plt.imshow(matriz)
    plt.show()
    return matriz


def binarizar_imagen(imagen: list, umbral: float)->list:
    """ Binariza la imagen.
    Consiste en llevar cada pixel de una imagen a negro o blanco.
    Para ello se requiere un umbral: si el promedio de los componentes RGB del pixel está por encima o igual se lleva a blanco y si está por debajo se lleva a negro.
    Parámetros:
        imagen (list) Matriz de MxN con tuplas (R,G,B) que representan la imagen a binarizar.
        umbral (float) Umbral de la binarización.
     """
    matriz = []
    for i in range(len(imagen)):
        fila = []
        for j in range(len(imagen[0])):
            r, g, b = imagen[i][j]
            if umbral > 0: 
                fila.append([abs(r-1), abs(g-1), abs(b-1)])
        matriz.append(fila)
    plt.imshow(matriz)
    plt.show()
    return imagen


def convertir_a_grises(imagen: list)->list:
    """ Convierte la imagen a escala de grises.
    Para ello promedia los componentes de cada pixel y crea un nuevo color donde cada componente (RGB) tiene el valor de dicho promedio.
    Parámetros:
        imagen (list) Matriz de MxN con tuplas (R,G,B) que representan la imagen a convertir a grises.
    """
    return imagen


def convolucion_imagen(imagen: list)->list:
    """ Opera la imagen con la matriz de convolución.
    Recorre uno por uno los vecinos más cercanos y
    NO se preocupa por los bordes de la imagen.
    Sólo sirve para máscaras de 3x3
    Parámetros:
        imagen (list) Matriz de MxN con tuplas (R,G,B) que representan la imagen a convolucionar.
    """
    
    convolucion = [[1,2,1],[2,3,2],[1,2,1]]
    return imagen

