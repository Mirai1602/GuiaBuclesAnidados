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
def Estadolab():
    Computadoras= []
    for i in range(5):
      filas=[]
      for j in range(4):
         while True: #Para poder saber el estado de la computadora
            Estado= input(f"Ingrese el estado de la computadora {i+1} {j+1} (O/ocupada) (L/libre)").strip().upper()
            if Estado in ["O" , "L"]:
               filas.append("Ocupada" if Estado == "O" else "Libre")
               break
            else:
             print("Entrada invalida, intente de nuevo. O para ocupada y L para libre")
             Computadoras.append(filas)
             return Computadoras
            
print("Ingrese el Estado de las computadoras del laboratorio 1: ") #Los valores del lab 1
Laboratorio1 = Estadolab() #Le doy a la variable el valor de la funcion para que se mande a llamar
print("Ingrese el estado de las computadoras del segundo laboratorio: ")
Laboratario2 = Estadolab() #Podria considerarse recursividad?, porque la funcion para llenar estos datos esta antes

def ContarCompus(Compuatadoras):
   CompusOcupadas= sum(filas.count("Ocupada") for filas in Compuatadoras) 
   #Me tuve que investigar que hacia esa cosa jajajaja, espara que cuente cuantas veces aparece el Ocupada
   CompusLibres= sum(filas.count("Libre") for filas in Compuatadoras)
   #El for ahi es para que recorra el arreglo recolectando esos datos que dije arriba de ocupada o libre
   return CompusOcupadas, CompusLibres

OcupadasLab1 , LibresLab1 = ContarCompus(Laboratorio1)
OcupadasLab2, LibresLab2 = ContarCompus(Laboratario2)

print("\nEl estado del laboratorio numero 1 es:")
#Recorremos una vez mas el arreglo. 
for filas in Laboratorio1:
   print(f"Computadoras ocupadas: {OcupadasLab1}, Libres: {LibresLab1}")
print("\nEl estado del laboratorio numero 2 es: ")
for filas in Laboratario2:
   print(f"Computadoras ocupadas: {OcupadasLab2}, Libres: {LibresLab2}")


               
               
               

