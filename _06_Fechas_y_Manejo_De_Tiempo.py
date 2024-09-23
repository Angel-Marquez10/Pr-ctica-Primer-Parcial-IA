""""
Práctica 6: Fechas y Manejo de Tiempo 
Los temas utilizados en el código incluyen:
1. Manejo de fechas y horas con el módulo datetime.
2. Uso de clases y objetos para modelar eventos.
3. Control de flujo mediante bucles y estructuras condicionales.
4. Manejo del método strftime


Descripción del programa:
Este código permite al usuario agregar eventos, ver los próximos eventos, 
calcular el tiempo restante para un evento específico y recibir recordatorios 
para eventos que ocurren en menos de 5 días.

"""
import datetime  # Importa el módulo datetime para trabajar con fechas y horas

# Clase Evento que guarda el nombre y fecha del evento
class Evento:
    def __init__(self, nombre, fecha):
        self.nombre = nombre  # Inicializa el nombre del evento
        self.fecha = fecha    # Inicializa la fecha/hora del evento

#Funcion string (str) en la clase Evento nos sirve para imprimir en este caso el objeto de nombre y fecha darle un formato
    def __str__(self):
        # Darle formato a la fecha
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        
        dia_semana = dias_semana[self.fecha.weekday()]  
        mes = meses[self.fecha.month - 1]               
        
        # Devuelve una cadena formateada que describe el evento en español
        return f"Evento: {self.nombre} en {dia_semana}, {self.fecha.day} de {mes} de {self.fecha.year} a las {self.fecha.strftime('%I:%M %p')}"

# Función para agregar un evento a la lista de eventos
def agregar_evento(eventos):
    while True:
        try:
            # Solicita al usuario el nombre del evento
            nombre = input("Ingrese el nombre del evento: ")
            
            # Solicita al usuario la fecha y hora del evento en el formato específico
            fecha_str = input("Ingrese la fecha y hora del evento (dd/mm/yyyy hh:mm): ")
            
            # Convierte la cadena de entrada en un objeto datetime
            fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
            
            # Crea un objeto Evento con el nombre y la fecha ingresada
            evento = Evento(nombre, fecha)
            
            # Agrega el evento a la lista de eventos
            eventos.append(evento)
            
            # Muestra un mensaje confirmando que el evento ha sido agregado
            print(f"Evento '{nombre}' agregado para {evento}")
            break
        except ValueError:
            # Muestra un mensaje de error y vuelve a solicitar la entrada si hay un error de formato
            print("Formato de fecha/hora inválido. Inténtalo de nuevo.")

# Función para mostrar los próximos eventos en orden cronológico
def mostrar_eventos_proximos(eventos):
    # Ordena la lista de eventos por fecha/hora usando la función sorted()
    eventos_ordenados = sorted(eventos, key=lambda evento: evento.fecha)
    
    # Imprime el encabezado de la lista de eventos
    print("\nPróximos Eventos:")
    
    # Recorre la lista de eventos ordenados y los imprime
    for evento in eventos_ordenados:
        print(evento)

# Función para calcular el tiempo restante hasta un evento específico
def tiempo_restante_evento(eventos):
    # Solicita al usuario el nombre del evento del que desea calcular el tiempo restante
    nombre_evento = input("Ingrese el nombre del evento para calcular el tiempo restante: ")
    
    # Busca el evento en la lista de eventos
    evento = next((e for e in eventos if e.nombre.lower() == nombre_evento.lower()), None)
    
    if evento:
        # Calcula el tiempo restante restando la fecha actual de la fecha del evento
        tiempo_restante = evento.fecha - datetime.datetime.now()
        
        # Calcula la cantidad de días, horas y minutos restantes
        dias = tiempo_restante.days
        horas, resto = divmod(tiempo_restante.seconds, 3600)
        minutos = resto // 60
        
        # Muestra el tiempo restante en un formato legible
        print(f"Tiempo restante para '{evento.nombre}': {dias} días, {horas} horas, {minutos} minutos")
    else:
        # Muestra un mensaje si el evento no fue encontrado
        print("Evento no encontrado.")

# Función para enviar recordatorios de eventos que ocurren en menos de 5 días
def enviar_recordatorios(eventos):
    # Obtiene la fecha y hora actual
    ahora = datetime.datetime.now()
    
    # Recorre la lista de eventos para comprobar si hay alguno que ocurra en menos de 5 días
    for evento in eventos:
        if 0 <= (evento.fecha - ahora).days <= 5:

            dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
            meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
            dia_semana = dias_semana[evento.fecha.weekday()]
            mes = meses[evento.fecha.month - 1]
            
            # Si el evento está a 5 días o menos, envía un recordatorio
            print(f"¡Recordatorio! El evento '{evento.nombre}' es en {dia_semana}, {evento.fecha.day} de {mes} de {evento.fecha.year} a las {evento.fecha.strftime('%I:%M %p')}")

# Función principal del menú de opciones que el usuario puede realizar
def menu():
    # Inicializa una lista con 5 eventos predeterminados
    eventos = [
        Evento("Reunión de trabajo", datetime.datetime(2024, 10, 1, 14, 30)),#La matriz  en () esta dada por año-mes-dia-hora-min2
        Evento("Cumpleaños de papa", datetime.datetime(2024, 11, 15, 18, 0)),
        Evento("Reta de futbol", datetime.datetime(2024, 9, 25, 9, 0)),
        Evento("Consulta médica", datetime.datetime(2024, 10, 5, 11, 15)),
        Evento("Cena familiar", datetime.datetime(2024, 12, 24, 20, 0))
    ]
    
    while True:
        # Muestra el menú de opciones
        print("\nAgenda Personalizada")
        print("1. Agregar evento")
        print("2. Mostrar próximos eventos")
        print("3. Calcular tiempo restante para un evento")
        print("4. Enviar recordatorios")
        print("5. Salir")

        # Solicita al usuario seleccionar una opción del menú
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Llama a la función para agregar un evento
            agregar_evento(eventos)
        elif opcion == "2":
            # Llama a la función para mostrar los próximos eventos
            mostrar_eventos_proximos(eventos)
        elif opcion == "3":
            # Llama a la función para calcular el tiempo restante hasta un evento
            tiempo_restante_evento(eventos)
        elif opcion == "4":
            # Llama a la función para enviar recordatorios de eventos
            enviar_recordatorios(eventos)
        elif opcion == "5":
            # Muestra un mensaje y sale del programa
            print("Saliendo de la agenda...")
            break
        else:
            # Muestra un mensaje si la opción ingresada no es válida
            print("Opción no válida, por favor intente de nuevo.")

# Ejecuta el menú principal
menu()
