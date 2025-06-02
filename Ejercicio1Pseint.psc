Algoritmo ejer2
	
		Definir asistencia, seccion, dia, estudiante  Como Entero
		Dimension asistencia[3, 5, 6]  // 3 secciones, 5 d�as, 6 estudiantes
		
		Definir totalSeccion Como Entero
		Dimension totalSeccion[3]  // Contador por secci�n
		
		Definir totalGeneral Como Entero
		totalGeneral = 0  // Contador total de asistencia en la semana
		
		// Registro de asistencia
		Para seccion <- 0 Hasta 2 Hacer
			totalSeccion[seccion] = 0  // Inicializar contador por secci�n
			Para dia <- 0 Hasta 4 Hacer
				Escribir "Registro de asistencia - Secci�n ", seccion+1, ", D�a ", dia+1
				Para estudiante <- 0 Hasta 5 Hacer
					Escribir "Estudiante ", estudiante+1, " presente (1) o ausente (0):"
					Leer asistencia[seccion, dia, estudiante]
					totalSeccion[seccion] = totalSeccion[seccion] + asistencia[seccion, dia, estudiante]
				FinPara
			FinPara
			totalGeneral = totalGeneral + totalSeccion[seccion]
		FinPara
		
		// Mostrar resultados de asistencia
		Escribir "Bienvenido al registro de asistencia UAM: "
		Para seccion <- 0 Hasta 2 Hacer
			Escribir "Secci�n ", seccion+1, ": ", totalSeccion[seccion], " asistencias en la semana."
		FinPara
		
		Escribir "Total general de asistencias en la semana: ", totalGeneral
		

	
	
FinAlgoritmo
