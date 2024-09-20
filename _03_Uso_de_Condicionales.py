
""""
Practica 3: Programa para gestionar calificaciones de estudiantes en 3 materias
 Esta práctica implementa los siguientes temas: 
 - Condicionales (IF, IF ELSE, IF ELIF ELSE)
 - Comprobación de datos en listas y tuplas
 - Múltiples condiciones IF
 - Tips para condicionales

 Explicación:
 Este programa evalúa las calificaciones de 3 estudiantes en 3 materias predeterminadas,
 además de permitir la adición de más estudiantes. Se utilizan las calificaciones de 3 parciales
 para cada materia, y se determina si cada estudiante aprueba o reprueba según la suma total
 de sus calificaciones.
"""
# Función para capturar calificaciones de los estudiantes
def capturar_calificaciones():
    """Captura las calificaciones de los estudiantes para 3 materias."""
    estudiantes = []  # Lista para almacenar los datos de los estudiantes

    # Definición de 3 estudiantes con materias y calificaciones
    datos_estudiantes = [
        ("Juan", [("Matemáticas", [80, 90, 85]), ("Historia", [70, 75, 80]), ("Ciencias", [60, 65, 70])]),
        ("María", [("Matemáticas", [95, 100, 90]), ("Historia", [85, 90, 92]), ("Ciencias", [80, 78, 85])]),
        ("Pedro", [("Matemáticas", [50, 60, 55]), ("Historia", [45, 50, 55]), ("Ciencias", [40, 38, 42])])
    ]

    # Agrega los estudiantes predeterminados a la lista
    for nombre, materias in datos_estudiantes:  
        print(f"\nIngresando datos para el estudiante: {nombre}")  # Mensaje para el usuario
        calificaciones = []  # Lista para almacenar las calificaciones de las materias
        
        # Bucle para las materias del estudiante
        for materia, parciales in materias:  
            suma_total = sum(parciales)  # Suma las calificaciones de los parciales
            calificaciones.append((materia, suma_total))  # Guarda la materia y su suma total

        estudiantes.append((nombre, calificaciones))  # Guarda el nombre y las calificaciones del estudiante

    return estudiantes  # Devuelve la lista de estudiantes y sus calificaciones

# Función para evaluar las calificaciones
def evaluar_calificaciones(estudiantes):
    """Evalúa las calificaciones de los estudiantes y muestra sus estados."""
    print("\nEvaluación de Calificaciones:")
    
    # Itera sobre la lista de estudiantes
    for nombre, calificaciones in estudiantes:  
        print(f"\nEstudiante: {nombre}")  # Muestra el nombre del estudiante
        
        # Evalúa cada materia y muestra su estado
        for materia, suma_total in calificaciones:  
            # Condicional para determinar el estado del estudiante
            if suma_total >= 270:  # Si la suma total es mayor o igual a 270
                estado = "Aprobado"  # Estado aprobado
            elif suma_total >= 240:  # Si la suma total es entre 240 y 269
                estado = "Aprobado con condiciones"  # Estado aprobado con condiciones
            else:  # Si la suma total es menor a 240
                estado = "Reprobado"  # Estado reprobado
            
            # Muestra el resultado de la materia
            print(f"Materia: {materia}, Suma Total: {suma_total}, Estado: {estado}")  

# Función principal con menú de opciones
def menu():
    """Muestra el menú principal."""
    estudiantes = capturar_calificaciones()  # Captura las calificaciones de los estudiantes
    evaluar_calificaciones(estudiantes)  # Muestra la evaluación de calificaciones

    while True:  # Ciclo infinito para mostrar el menú
        print("\n--- Menú de Opciones ---")  # Mensaje del menú
        print("1. Ver calificaciones de los estudiantes")
        print("2. Agregar un nuevo estudiante")
        print("3. Salir")
        
        opcion = input("Selecciona una opción (1/2/3): ")  # Captura la opción del usuario
        
        if opcion == '1':  # Si el usuario elige ver calificaciones
            evaluar_calificaciones(estudiantes)  # Muestra las calificaciones
        elif opcion == '2':  # Si el usuario elige agregar un estudiante
            nombre = input("Ingresa el nombre del nuevo estudiante: ")  # Captura el nombre del nuevo estudiante
            calificaciones = []  # Lista para las calificaciones del nuevo estudiante
            
            for i in range(3):  # Bucle para 3 materias
                materia = input(f"Ingrese el nombre de la materia {i + 1}: ")  # Nombre de la materia
                parciales = []  # Lista para almacenar calificaciones de los parciales
                
                # Captura las calificaciones de los 3 parciales
                for j in range(3):  # Bucle para los parciales
                    calificacion = float(input(f"Ingresa la calificación del parcial {j + 1}: "))  # Calificación
                    parciales.append(calificacion)  # Agrega la calificación a la lista
                
                # Calcula la suma total de las calificaciones
                suma_total = sum(parciales)  # Suma las calificaciones de los parciales
                calificaciones.append((materia, suma_total))  # Guarda la materia y su suma total

            estudiantes.append((nombre, calificaciones))  # Guarda el nuevo estudiante y sus calificaciones
        elif opcion == '3':  # Si el usuario elige salir
            print("Saliendo del programa...")  # Mensaje de salida
            break  # Sale del ciclo
        else:  # Si la entrada no es válida
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")  # Mensaje de error

# Llama a la función del menú para iniciar el programa
menu()  # Inicia el programa
