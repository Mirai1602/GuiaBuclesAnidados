Algoritmo numero4
	// Registro del consumo energético en cuatro edificios del campus
	Definir consumo_total, consumo_dia, consumo_general, consumo_turno, promedio_semana Como Real  
	Definir i, j, k Como Entero  
	
	consumo_general <- 0  // Inicializamos el consumo total del campus
	
	Para i <- 1 Hasta 4 Hacer  // Hay 4 edificios en el campus
		Escribir "?? Registro de consumo para Edificio ", i
		consumo_total <- 0  // Inicializar el consumo total del edificio
		
		Para j <- 1 Hasta 7 Hacer  // Consumo energético durante 7 días de la semana
			Escribir "?? Día ", j
			consumo_dia <- 0  // Inicializar consumo diario
			
			Para k <- 1 Hasta 3 Hacer  // Se registran los 3 turnos: mañana, tarde y noche
				Si k = 1 Entonces
					Escribir "?? Ingrese el consumo en turno Mañana:"
				SiNo
					Si k = 2 Entonces
						Escribir "?? Ingrese el consumo en turno Tarde:"
					SiNo
						Escribir "?? Ingrese el consumo en turno Noche:"
					FinSi
				FinSi
				
				// Leer y validar que el consumo sea positivo
				Repetir
					Leer consumo_turno
					Si consumo_turno < 0 Entonces
						Escribir "? Error: El consumo debe ser positivo. Intente nuevamente."
					FinSi
				Hasta Que consumo_turno >= 0
				
				consumo_dia <- consumo_dia + consumo_turno  // Acumular consumo diario
			FinPara  // Fin de los turnos
			
			Escribir "? Consumo total del Día ", j, ": ", consumo_dia
			consumo_total <- consumo_total + consumo_dia  // Acumular el consumo del edificio
		FinPara  // Fin de los días
		
		promedio_semana <- consumo_total / 7  // Calcular promedio semanal del edificio
		Escribir "?? Total de consumo del Edificio ", i, ": ", consumo_total
		Escribir "?? Promedio semanal de consumo: ", promedio_semana
		consumo_general <- consumo_general + consumo_total  // Acumular el consumo del campus
	FinPara  // Fin de los edificios
	
	Escribir "?? **Total de consumo energético en el campus:** ", consumo_general
	
FinAlgoritmo
