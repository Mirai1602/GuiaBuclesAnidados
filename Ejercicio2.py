"""
Autor: Mayrin Tellez
Fecha: 17-05-2025
Descripcion: Es programa que simule el estado de uso de computadoras en dos laboratorios del 
campus. Cada laboratorio contiene cinco filas de cuatro computadoras. Por cada computadora 
se debe registrar si está ocupada o libre (puede ingresarse manualmente o simularse con 
valores aleatorios). Al finalizar, el programa debe mostrar el resumen de computadoras ocupadas o libres
por el labotarotio.
"""
import os

#Se crean dos laboratorios con todas las computadoras disponibles, para que el usuario solo tenga
#que marcar las ocupadas
def labVacio():
   return [[True for i in range(4)] for j in range(5)]

#Según yo, de esta forma es más práctico, así no hay que estar marcando 400 líneas
def marcar(labs):
   print("Introduce las computadoras ocupadas en el formato L-F-C(laboratorio-fila-computadora) utilizando números enteros")
   print("Para introducir varias serpare por comas, eje: 1-2-3,1-4-5,2-2-1")
   estado=input("Computadoras ocupadas: ")
   #primero divide [1-2-3,1-4-5] en [1-2-3][1-4-5] para después tomar cada número y asignarlo según
   #el orden (lab, fila, compu) y convierte las variables a enteros (lab=1, fila=1, compu=1)
   estadoGeneral=estado.split(",")
   for coordenadas in estadoGeneral:
         lab, fila, compu=map(int, coordenadas.split("-"))
         if 1<= lab <=2 and 1 <= fila <=5 and 1<= compu <=4:
            labs[lab - 1][fila - 1][compu - 1] = False

def EstadoLab(labAsignado,laboratorio):
    libres=0
    ocupadas=0
    print(f"\nEstado de {labAsignado}:")
    for i in range(5):
      filas=[]
      for j in range(4):
         if laboratorio[i][j]:
            filas.append("[🟢]")
            libres+=1
         else:
            filas.append("[🔴]")
            ocupadas+=1
      print(f"Fila {i + 1}): {filas}")
    print(f"Libres: {libres} | Ocupadas: {ocupadas}\n")

lab1 = labVacio()
lab2 = labVacio()
labs = [lab1, lab2]

marcar(labs)

EstadoLab("Laboratorio 1", lab1)
EstadoLab("Laboratorio 2", lab2)