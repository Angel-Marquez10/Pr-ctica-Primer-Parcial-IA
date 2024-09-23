"""""
Practica 7: Gestión de Contactos
 Temas implementados: 
-Expresiones regulares 1 - search()
-Expresiones regulares 2 - findall()
-Expresiones regulares 3 - split() y sub()
-Secuencias especiales, metacaracteres y sets
-Manejo de excepciones

 Esta práctica consiste en crear un gestor de contactos donde se pueden agregar, buscar,
 modificar y eliminar contactos, validando entradas como correos y números de teléfono
 mediante expresiones regulares y manejando excepciones para entradas no válidas.

"""

import re  # Importa el módulo de expresiones regulares

# Clase para gestionar un contacto
class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre  # Nombre del contacto
        self.telefono = telefono  # Teléfono del contacto
        self.correo = correo  # Correo del contacto

    def __str__(self):
        return f"{self.nombre} - Tel: {self.telefono} - Correo: {self.correo}"

# Función para validar un correo electrónico
def validar_correo(correo):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # Patrón para validar correos
    return bool(re.search(patron, correo))  # Retorna True si el correo es válido

# Función para validar un número de teléfono
def validar_telefono(telefono):
    patron = r'^\+?[0-9]{7,15}$'  # Permite números de 7 a 15 dígitos
    return bool(re.search(patron, telefono))  # Retorna True si el teléfono es válido

# Función para agregar un contacto
def agregar_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el teléfono del contacto: ")
    correo = input("Ingrese el correo del contacto: ")

    # Validaciones de entradas
    if not validar_telefono(telefono):
        print("Número de teléfono no válido.")
        return
    if not validar_correo(correo):
        print("Correo electrónico no válido.")
        return

    # Crear y agregar contacto a la lista
    contacto = Contacto(nombre, telefono, correo)
    contactos.append(contacto)
    print("Contacto agregado con éxito.")

# Función para buscar un contacto por nombre, teléfono o correo
def buscar_contacto(contactos):
    criterio = input("Ingrese el nombre, teléfono o correo del contacto a buscar: ")
    encontrados = [c for c in contactos if re.search(criterio, c.nombre, re.IGNORECASE) or 
                   re.search(criterio, c.telefono) or re.search(criterio, c.correo)]
    
    if encontrados:
        print("Contactos encontrados:")
        for contacto in encontrados:
            print(contacto)
    else:
        print("No se encontraron contactos.")

# Función para mostrar todos los contactos
def mostrar_contactos(contactos):
    if contactos:
        print("\nLista de contactos:")
        for contacto in contactos:
            print(contacto)
    else:
        print("No hay contactos en la lista.")

# Función para modificar un contacto
def modificar_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto a modificar: ")
    for contacto in contactos:
        if re.search(nombre, contacto.nombre, re.IGNORECASE):
            nuevo_telefono = input("Ingrese el nuevo teléfono: ")
            nuevo_correo = input("Ingrese el nuevo correo: ")

            # Validaciones de entradas
            if not validar_telefono(nuevo_telefono):
                print("Número de teléfono no válido.")
                return
            if not validar_correo(nuevo_correo):
                print("Correo electrónico no válido.")
                return

            # Actualizar contacto
            contacto.telefono = nuevo_telefono
            contacto.correo = nuevo_correo
            print("Contacto modificado con éxito.")
            return
    print("Contacto no encontrado.")

# Función para eliminar un contacto
def eliminar_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    contactos[:] = [c for c in contactos if not re.search(nombre, c.nombre, re.IGNORECASE)]
    print("Contacto eliminado si existía.")

# Función para mostrar un menú y manejar las opciones
def mostrar_menu():
    contactos = []  # Lista para almacenar los contactos

    while True:
        print("\n--- Gestor de Contactos ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Mostrar contactos")
        print("4. Modificar contacto")
        print("5. Eliminar contacto")
        print("6. Salir")

        try:
            opcion = int(input("Seleccione una opción (1-6): "))

            # Manejar las opciones del menú
            if opcion == 1:
                agregar_contacto(contactos)
            elif opcion == 2:
                buscar_contacto(contactos)
            elif opcion == 3:
                mostrar_contactos(contactos)
            elif opcion == 4:
                modificar_contacto(contactos)
            elif opcion == 5:
                eliminar_contacto(contactos)
            elif opcion == 6:
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

# Llama a la función para mostrar el menú
mostrar_menu()
