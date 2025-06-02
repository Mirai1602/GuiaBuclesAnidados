"""
Autores: Mayrin Tellez, Melani, Maria Alejandra Sarante
Fecha:
Version:0.1
Descripcion: Monitoreo del consumo energético 
Desarrolle un programa que registre el consumo energético de cuatro edificios del campus 
universitario a lo largo de una semana. Por cada día se ingresarán los kilovatios consumidos en 
tres turnos: mañana, tarde y noche. El programa debe calcular el consumo total por edificio y 
generar el promedio semanal correspondiente.
"""
edificios = 4
diasSemana = 7
turnos = ["Mañana", "Tarde", "Noche"]
print("********** Bienvenido al sistema de registro energetico **********")
print("-------------------- Universidad Americana UAM --------------------")
def ConsumoEnergetico():
    #Registrar el consumo de cada edificio en una lista
    consumoEdificios = [[0 for _ in range(diasSemana)] for _ in range(edificios)]

    for i in range(edificios):
        print(f"\n--- Edificio {i + 1} ---")
        for j in range(diasSemana):
            total_dia = 0
            print(f"\nDía {j + 1}:")
            for turno in turnos:
                while True:
                    try:
                        consumo = float(input(f"  Ingrese consumo en {turno} (kWh): "))
                        if consumo < 0:
                            print("El consumo no puede ser negativo.")
                            continue
                        break
                    except ValueError:
                        print("Entrada no válida. Intente de nuevo.")
                total_dia += consumo
            consumoEdificios[i][j] = total_dia
    return consumoEdificios

def mostrarReporte(consumoEdificios):
    """Muestra el total y promedio semanal de consumo por edificio."""
    print("\n--- Reporte de Consumo ---")
    for i in range(edificios):
        totalSemana = sum(consumoEdificios[i])
        promedio = totalSemana / diasSemana
        print(f"Edificio {i + 1}: Total = {totalSemana:.2f} kWh, Promedio diario = {promedio:.2f} kWh")

consumos = ConsumoEnergetico()
mostrarReporte(consumos)