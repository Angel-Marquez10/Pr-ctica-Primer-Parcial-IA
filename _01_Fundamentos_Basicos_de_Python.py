"""
Práctica 1: Fundamentos Básicos de Python
sta práctica está diseñada para cubrir los siguientes temas:

 1. Variables: 
 2. Variables globales, locales y funciones
 3. Strings: 
 4. Concatenar: 
 5. Métodos upper(), lower() y title(): 
 6. Saltos de línea y tabulaciones: 
 7. Operaciones Matemáticas
 8. Floats y el método round(): 
 
 Explicación:
 El objetivo de esta práctica es ofrecer una experiencia práctica con los fundamentos de Python. Se cubren temas como variables, manipulación de texto,
 y operaciones matemáticas básicas, utilizando tanto variables locales como globales. A través de este ejercicio, el usuario puede interactuar con el programa
 ingresando datos y observando cómo se procesan y presentan de diversas maneras.
"""

# Definir variables globales
resultado = 0  # Variable global para almacenar el resultado de operaciones matemáticas

# Función para mostrar el menú
def mostrar_menu():
    """
    Muestra el menú de opciones para el usuario.
    """
    # Imprime las opciones disponibles en el menú
    print("\nMenú de Opciones:")
    print("1. Formatear nombre")
    print("2. Realizar operaciones matemáticas")
    print("3. Manejar texto proporcionado")
    print("4. Salir")

# Función para darle formato al nombre hace uso de los STRINGS
def formatear_nombre():
    """
    Solicita un nombre al usuario y muestra diferentes formatos del nombre.
    """
    nombre = input("Ingresa tu nombre completo: ")  # Solicita al usuario que ingrese su nombre

    # Muestra el nombre en diferentes formatos
    print(f"\nNombre en mayúsculas: {nombre.upper()}")  # Nombre en mayúsculas (Strings, upper())
    print(f"Nombre en minúsculas: {nombre.lower()}")  # Nombre en minúsculas (Strings, lower())
    print(f"Nombre en formato título: {nombre.title()}")  # Nombre en formato título (Strings, title())
    print(f"Nombre con saltos de línea:\n{nombre}")  # Ejemplo de salto de línea (Strings, \n)
    print(f"Nombre con tabulación:\t{nombre}")  # Ejemplo de tabulación (Strings, \t)

# Función para realizar operaciones matemáticas básicas 
def realizar_operaciones_matematicas():
    """
    Solicita dos números al usuario y realiza operaciones matemáticas básicas con ellos.
    """
    global resultado  # Usamos la variable global 'resultado' para almacenar los resultados

    try:
        # Solicita al usuario que ingrese dos números
        num1 = float(input("Ingresa el primer número: "))  # Solicita el primer número (Floats)
        num2 = float(input("Ingresa el segundo número: "))  # Solicita el segundo número (Floats)

        # Realiza y muestra operaciones matemáticas básicas
        resultado = num1 + num2  # Suma de los dos números
        print(f"Suma: {resultado}")

        resultado = num1 - num2  # Resta de los dos números
        print(f"Resta: {resultado}")

        resultado = num1 * num2  # Multiplicación de los dos números
        print(f"Multiplicación: {resultado}")

        resultado = num1 / num2  # División de los dos números
        print(f"División: {resultado:.2f}")  # Muestra el resultado con 2 decimales

        resultado = num1 ** num2  # Exponente (num1 elevado a num2)
        print(f"Exponente (num1^num2): {resultado}")

        resultado = round(num1 ** 0.5, 2)  # Raíz cuadrada del primer número, redondeada a 2 decimales
        print(f"Raíz cuadrada del primer número: {resultado}")

        resultado = round(num2 ** 0.5, 2)  # Raíz cuadrada del segundo número, redondeada a 2 decimales
        print(f"Raíz cuadrada del segundo número: {resultado}")

        # Cálculo de temperaturas
        celsius = float(input("Ingresa la temperatura en Celsius: "))  # Solicita la temperatura en Celsius
        fahrenheit = celsius * 9/5 + 32  # Convierte Celsius a Fahrenheit
        print(f"Temperatura en Fahrenheit: {fahrenheit:.2f}")

        fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))  # Solicita la temperatura en Fahrenheit
        celsius = (fahrenheit - 32) * 5/9  # Convierte Fahrenheit a Celsius
        print(f"Temperatura en Celsius: {celsius:.2f}")

    except ValueError:
        print("Por favor, ingresa números válidos.")  # Manejo de errores para entradas no numéricas
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")  # Manejo de errores para división por cero

# Función para manejar un texto y utilizar los temas como: (upper, lower, title, saltos de línea, tabulación y len)
def manejar_texto_proporcionado():
    """
    Solicita un texto al usuario y muestra diferentes operaciones relacionadas con ese texto.
    """
    texto = input("Ingresa un texto para procesar: ")  # Solicita al usuario que ingrese un texto

    # Muestra el texto en diferentes formatos
    print(f"\nTexto en mayúsculas: {texto.upper()}")  # Texto en mayúsculas (Strings, upper())
    print(f"Texto en minúsculas: {texto.lower()}")  # Texto en minúsculas (Strings, lower())
    print(f"Texto en formato título: {texto.title()}")  # Texto en formato título (Strings, title())
    print(f"Texto con saltos de línea:\n{texto}")  # Ejemplo de salto de línea (Strings, \n)
    print(f"Texto con tabulación:\t{texto}")  # Ejemplo de tabulación (Strings, \t)
    print(f"Longitud del texto: {len(texto)} caracteres.")  # Longitud del texto (Strings, len())
    
    palabras = texto.split()  # Divide el texto en palabras (Strings, split())
    print(f"Cantidad de palabras en el texto: {len(palabras)}")  # Cantidad de palabras (Strings, len())
    print(f"Primera letra de cada palabra: {' '.join([palabra[0] for palabra in palabras])}")  # Primera letra de cada palabra (Strings, list comprehension)

# Función principal que controla el flujo del programa
def main():
    """
    Función principal que controla el flujo del programa.
    """
    print("\nBienvenido a la práctica de Fundamentos Básicos de Python.")  # Mensaje de bienvenida
    print("Esta práctica cubre los siguientes temas:\n")
    print("1. Variables globales y locales")
    print("2. Manipulación de strings")
    print("3. Operaciones matemáticas básicas")
    print("4. Conversión de temperaturas\n")
    print("A través de diferentes opciones en el menú, podrás experimentar con cada uno de estos conceptos.\n")

    while True:  # Bucle infinito para mostrar el menú continuamente
        mostrar_menu()  # Muestra el menú de opciones
        opcion = input("\nSelecciona una opción (1-4): ")  # Solicita al usuario que seleccione una opción

        if opcion == "1":
            print("Opción 1: Formatear nombre. Utiliza temas como variables, strings, concatenación, métodos upper(), lower(), title(), saltos de línea y tabulación.")  # Mensaje de temas
            formatear_nombre()  # Llama a la función para formatear el nombre
        elif opcion == "2":
            print("Opción 2: Realizar operaciones matemáticas. Utiliza temas como variables, floats, suma, resta, multiplicación, división, exponentes y el método round().")  # Mensaje de temas
            realizar_operaciones_matematicas()  # Llama a la función para realizar operaciones matemáticas
        elif opcion == "3":
            print("Opción 3: Manejar texto proporcionado. Utiliza temas como variables, strings, métodos upper(), lower(), title(), saltos de línea, tabulación, longitud y división de texto.")  # Mensaje de temas
            manejar_texto_proporcionado()  # Llama a la función para manejar el texto proporcionado
        elif opcion == "4":
            print("Gracias por usar el programa. ¡Hasta la próxima!")  # Mensaje de despedida
            break  # Sale del bucle y termina el programa
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")  # Manejo de opciones inválidas

# Inicia el programa llamando a la función main
main()
