"""
Ejercicio nivel 4: Rendimiento de cultivos en Colombia
Modulo de funciones.

@author: Cupi2
"""

import pandas as pd
import matplotlib.pyplot as plt

def cargar_datos(archivo)-> pd.DataFrame:
    df = pd.read_csv(archivo)
    return df

def piechart_tipo_cultivo(df: pd.DataFrame, dep: str)-> None:

    f = df[df["Departamento"] == dep]
    d = f.groupby("Tipo_Cultivo")["Toneladas"].sum()
    plt.title("Distribucion de toneladas por tipo de cultivo en "+str(dep))
    plt.pie(d, autopct='%.1f%%', labels = d.index)
    #plt.pie(f["Toneladas"], autopct='%.1f%%', labels = f["Tipo_Cultivo"])
    plt.show()
    
def diagrama_barras(df: pd.DataFrame)-> None:
    d = df[["Cultivo","Toneladas","Hectareas_cosechadas"]]
    f = d.groupby("Cultivo").sum()
    f["Promedio"] = f["Toneladas"]/f["Hectareas_cosechadas"]
    top = f["Promedio"].sort_values(ascending = False).head(10)
    plt.title("Top 10 de cultivos con mayor cantidad de toneladas cosechas por hectaria")
    plt.ylabel("Toneladas cosechadas x Hectaria")
    top.plot(kind = "bar")
    plt.show()
def diagrama_caja(df: pd.DataFrame)-> None:
    plt.show()
    
#Parte 2
#Requerimiento 4
def crear_matriz(dataframe: pd.DataFrame)->list:

    deptos =  sorted(dataframe["Departamento"].unique())
    dept_dict = dict(list(enumerate(deptos)))
    tipos_cultivos =  sorted(dataframe["Tipo_Cultivo"].unique())
    tipos_cultivos_dict = dict(list(enumerate(tipos_cultivos)))
    
    matriz = []
    for _ in range(len(deptos)):
        fila = [0 for _ in range(len(tipos_cultivos))]
        matriz.append(fila)
        
    pivot_df = dataframe.pivot_table(index = "Departamento", columns = "Tipo_Cultivo", values = "Toneladas", aggfunc='sum', fill_value=0)
 
    for i, depto in enumerate(deptos):
        for j, cultivo in enumerate(tipos_cultivos):
            if depto in pivot_df.index and cultivo in pivot_df.columns:
                matriz[i][j] = pivot_df.loc[depto, cultivo]
            else:
                matriz[i][j] = 0
    return (matriz, tipos_cultivos_dict, dept_dict)

def cantidad_toneladas_departamento(m: tuple, dep: str)-> int:
    x = 0
    total = 0
    for k, v in m[2].items():
        if v == dep:
            x = k
    for i in m[0][x]:
        total += i
    return total

def depto_mayor_o_menor_productor(m: tuple, t: bool, c: str)-> str:
    dep = ""
    x = 0
    
    for k, v in m[1].items():
        if v == c:
            x = k
    d = {}
    c = 0
    for k, v in m[2].items():
        d[v] = m[0][c][x]
        c += 1
    if t == True:
        p = 0
        for k, i in d.items():
            if i > p:
                p = i
                dep = k
    if t == False:
        p = 1000000000000000
        for k, i in d.items():
            if i != 0 and i < p:
                p = i
                dep = k
    
    return dep
    

def departamento_estrella(t)->None:
    pass

def mapa(t)->None:
    pass


