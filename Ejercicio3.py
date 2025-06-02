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
            print(f"───────Registro de ganancias del stand {stand}──────")
            print(f"                    DIA {dia+1}")
            for j in range(3):
                ganancia = int(input(f"Ingrese el monto de venta del producto {j+1}: "))
                totalGananciaDia += ganancia
            gananciasPorDia.append(totalGananciaDia)
            totalAcumulado += totalGananciaDia
        stands.append([stand, gananciasPorDia, totalAcumulado])

        totalPorDia = [0] * len(stands [0][1])
        for stand in stands:
            for i in range(len(totalPorDia)):
                totalPorDia[i] += stand [1][i]

        totalGeneral = sum(totalPorDia)

    print("\n╔════════════════════════════════════════════════════╗")
    print("║            RESUMEN GANANCIAS - FERIA UAM           ║")
    print("╚════════════════════════════════════════════════════╝")
    print("──────────────────────────────────────────────────────")
    print("Stand      | Día 1  | Día 2  | Día 3  | Total")
    for standInfo in stands:
        nombre = standInfo[0]
        ganancias = standInfo[1]
        total = standInfo[2]
        salida = f"{nombre}: "
        for i in range(len(ganancias)):
             salida += f"| C${ganancias [i]}"
        salida += f"| C${total}\n"
        print(salida)
    print("──────────────────────────────────────────────────────")

    salidaTotal = f"{'TOTAL POR DÍA: '}"
    for monto in totalPorDia:
        salidaTotal += f"| C${monto}"
    salidaTotal += f"| C$ {totalGeneral}"
    print(salidaTotal)
    print("──────────────────────────────────────────────────────")

infoStands()