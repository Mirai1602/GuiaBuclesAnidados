"""
Autores: Mayrin Tellez, Melani, Maria Alejandra Sarante
Fecha:
Descripcion: Registro de asistencia académica 
Desarrolle un programa que registre la asistencia de estudiantes en tres secciones distintas de 
la UAM, durante cinco días de clases. Cada día se tomará asistencia a seis estudiantes por 
sección. El programa deberá contabilizar y mostrar el total de asistencias registradas por 
sección, así como el total general de la semana.
"""
from datetime import datetime
def Registrar_Asistencia():
    Asistencia=[] #Lo vamos a trabajar como un arreglo tridimensional por las tres aulas. 
    secciones = 3
    dias = 5 
    estudiantesPorAula= 6 #Recuerda! Tres variables para control 
    for i in range(secciones):
        dias_lista=[] #Lista temporal para poder pasarselo a Asistencia
        for j in range(dias):
            estudianteLista= [0] * estudiantesPorAula #Todos los alumnos esta como ausentes hasta que se marque lo contrario
            m=0 
            while m < estudiantesPorAula:
                print(f"Estado estudiante {m+1}  *1 es presente 0 es ausente")
                dias_lista.append(estudianteLista)
    Asistencia.append(dias_lista)
    return Asistencia


    print("\nResgistro de asistencia:")
    print(Asistencia)
def SalidaFinal(Asistencia):
    print("Bienvenido al registro de asistencia UAM: ")
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"El dia de hoy es: {fecha} ")
    
    for a , seccion in enumerate(Asistencia): #For para control general
         print(f" Sección {a+1}")
         for b, dias in enumerate(seccion):
           estado_dia = " | ".join(["✅" if estudiante == 1 else "❌" for estudiante in dias])
        #Resulta que la consola soporta mostrar emojis wow, por que c no lo haria jajajaj
        #Usamos .join como simulando la peticion de colocar el emoji que queremos para que 
         print(f"   Día {b+1}: {estado_dia}")
         print("-" * 40) #Version rapida de imprimir el -----  

Registrar_Asistencia()
SalidaFinal()




            
