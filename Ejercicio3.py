"""
Autor: Melani Espinoza
Fecha: 1/6/25
Versión: 1.0
Descripción: Es un programa que permite llevar un registro de ventas en una feria estudiantil organizada
por la UAM. La feria se desarrollará durante tres días, con cuatro stands por día. Cada stand
ofrecerá tres productos distintos. El sistema permite ingresar el monto de venta por
producto y muestra un resumen por stand, por día, y un total general de la feria.
"""

def infoStands():
    stands = []

    for i in range(4):
        stand = input(f"Ingrese el nombre del stand {i+1}: ")
        gananciasPorDia = []
        totalAcumulado = 0

        for dia in range(3):
            totalGananciaDia = 0
            print(f"------Registro de ganancias del stand {stand}------")
            print(f"                    DIA {dia+1}")
            for j in range(3):
                ganancia = int(input(f"Ingrese el monto de venta del producto {j+1}: "))
                totalGananciaDia += ganancia
            gananciasPorDia.append(totalGananciaDia)
            totalAcumulado += totalGananciaDia
    stands.append([stand, gananciasPorDia, totalAcumulado])

    print("Resumen ganancias por stand: ")
    for standInfo in stands:
        nombre = standInfo[0]
        ganancias = standInfo[1]
        total = standInfo[2]
        print(f"Stand: {nombre}")
        for i in range(len(ganancias)):
            print(f"Día {i+1}: {ganancias [i]}")
        print(f"    Total acumulado: {total}\n")

infoStands()