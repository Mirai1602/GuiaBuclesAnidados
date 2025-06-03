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
        print(f" Registrando asistencia para Sección {i+1}")
        dias_lista=[] #Lista temporal para poder pasarselo a Asistencia

        for j in range(dias):
            fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Capturar fecha y hora
            print(f"Día {j+1} ({fecha_actual})")
            estudianteLista= [0] * estudiantesPorAula #Todos los alumnos esta como ausentes hasta que se marque lo contrario
            for m in range(estudiantesPorAula):
                estudianteLista[m] =int( input(f"Estudiante {m+1} presente (1) o ausente (0): "))
            dias_lista.append(estudianteLista)
        Asistencia.append(dias_lista)
    return Asistencia

def Calcular_Totales(Asistencia):
    totales_por_seccion = []
    total_general = 0

    for a, seccion in enumerate(Asistencia):
        total_seccion = sum(sum(dia) for dia in seccion)  # Suma de asistentes en la sección
        totales_por_seccion.append(total_seccion)
        total_general += total_seccion

    return totales_por_seccion,total_general
 
def SalidaFinal(Asistencia):
    print("Bienvenido al registro de asistencia UAM: ")
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"El dia de hoy es: {fecha} ")
    totales_por_seccion= Calcular_Totales(Asistencia)
    total_general = Calcular_Totales(Asistencia)
    
    for a , seccion in enumerate(Asistencia): #For para control general
        print(f" Sección {a+1}")
        for b, dias in enumerate(seccion):
            estado_dia = " | ".join(["✅" if estudiante == 1 else "❌" for estudiante in dias])
            #Resulta que la consola soporta mostrar emojis wow, por que c no lo haria jajajaj
            #Usamos .join como simulando la peticion de colocar el emoji que queremos para que 
            print(f"   Día {b+1}: {estado_dia}")
            print(f"🔢 Total de asistencias en Sección {a+1}: {totales_por_seccion}")
            print("-" * 40) #Version rapida de imprimir el -----  
    print(f"📊 **Total general de asistencias en la semana: {total_general}") 


asistencia_registrada = Registrar_Asistencia()
SalidaFinal(asistencia_registrada)






            
