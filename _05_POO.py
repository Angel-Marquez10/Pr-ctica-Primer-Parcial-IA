"""
Gestión de una Biblioteca de Libros

En esta práctica se implementan los siguientes temas:
1. Programación Orientada a Objetos (POO)
2. Clases y objetos
3. El método __init__
4. Cambiar valores de objetos y el uso de self
5. Clases vacías con pass y eliminar objetos
6. Herencia de clases
7. Heredar propiedades __init__

Descripción del programa:
Este programa permite gestionar una biblioteca, donde el usuario puede agregar y eliminar libros y autores. 
Demuestra la creación de clases, el uso de métodos, y cómo interactuar con la biblioteca de forma sencilla.
"""

# Clase para representar un Autor
class Autor:
    """Representa un autor de libros."""
    
    def __init__(self, nombre, nacionalidad):
        """Inicializa los atributos del autor."""
        self.nombre = nombre           # Nombre del autor
        self.nacionalidad = nacionalidad # Nacionalidad del autor

    def __str__(self):
        """Devuelve una representación en cadena del autor."""
        return f"{self.nombre} ({self.nacionalidad})"

# Clase para representar un Libro
class Libro:
    """Representa un libro en la biblioteca."""
    
    def __init__(self, titulo, autor, anio):
        """Inicializa los atributos del libro."""
        self.titulo = titulo           # Título del libro
        self.autor = autor             # Autor del libro (objeto de la clase Autor)
        self.anio = anio               # Año de publicación del libro

    def __str__(self):
        """Devuelve una representación en cadena del libro."""
        return f"'{self.titulo}' por {self.autor.nombre} ({self.anio})"

# Clase para gestionar la Biblioteca
class Biblioteca:
    """Representa una biblioteca que contiene libros y autores."""
    
    def __init__(self):
        """Inicializa la biblioteca con listas vacías."""
        self.libros = []               # Lista para almacenar libros
        self.autores = []              # Lista para almacenar autores

    def agregar_libro(self, libro):
        """Agrega un libro a la biblioteca."""
        self.libros.append(libro)      # Añade el libro a la lista
        print(f"Libro '{libro.titulo}' agregado.")

    def eliminar_libro(self, titulo):
        """Elimina un libro de la biblioteca por su título."""
        for libro in self.libros:      # Recorre la lista de libros
            if libro.titulo == titulo:  # Busca el libro por título
                self.libros.remove(libro) # Lo elimina de la lista
                print(f"Libro '{titulo}' eliminado.")
                return
        print(f"Libro '{titulo}' no encontrado.") # Mensaje si no se encuentra

    def agregar_autor(self, autor):
        """Agrega un autor a la biblioteca."""
        self.autores.append(autor)     # Añade el autor a la lista
        print(f"Autor '{autor.nombre}' agregado.")

    def eliminar_autor(self, nombre):
        """Elimina un autor de la biblioteca por su nombre."""
        for autor in self.autores:      # Recorre la lista de autores
            if autor.nombre == nombre:   # Busca el autor por nombre
                self.autores.remove(autor) # Lo elimina de la lista
                print(f"Autor '{nombre}' eliminado.")
                return
        print(f"Autor '{nombre}' no encontrado.") # Mensaje si no se encuentra

    def mostrar_libros(self):
        """Muestra todos los libros en la biblioteca."""
        if self.libros:                 # Comprueba si hay libros
            print("\nLibros en la biblioteca:")
            for libro in self.libros:   # Imprime cada libro
                print(libro)
        else:
            print("No hay libros en la biblioteca.")

    def mostrar_autores(self):
        """Muestra todos los autores en la biblioteca."""
        if self.autores:                # Comprueba si hay autores
            print("\nAutores en la biblioteca:")
            for autor in self.autores:   # Imprime cada autor
                print(autor)
        else:
            print("No hay autores en la biblioteca.")

# Función principal para interactuar con la biblioteca
def main():
    """Función principal que gestiona la biblioteca."""
    print("¡Bienvenido a la Biblioteca!")
    print("Este programa permite gestionar una biblioteca de libros y autores.")
    print("Podrás agregar, eliminar y mostrar libros y autores.")

    # Crear instancia de la biblioteca
    biblioteca = Biblioteca()

    # Agregar 3 libros y sus autores al inicio
    autor1 = Autor("Gabriel García Márquez", "Colombiano")
    libro1 = Libro("Cien años de soledad", autor1, 1967)
    biblioteca.agregar_libro(libro1)

    autor2 = Autor("J.K. Rowling", "Británica")
    libro2 = Libro("Harry Potter y la piedra filosofal", autor2, 1997)
    biblioteca.agregar_libro(libro2)

    autor3 = Autor("George Orwell", "Británico")
    libro3 = Libro("1984", autor3, 1949)
    biblioteca.agregar_libro(libro3)

    # Menú de opciones
    while True:
        print("\n--- Menú de la Biblioteca ---")
        print("1. Agregar autor")
        print("2. Agregar libro")
        print("3. Eliminar libro")
        print("4. Eliminar autor")
        print("5. Mostrar libros")
        print("6. Mostrar autores")
        print("7. Salir")
        opcion = input("Selecciona una opción (1-7): ")

        if opcion == '1':  # Opción para agregar autor
            nombre = input("Nombre del autor: ")
            nacionalidad = input("Nacionalidad del autor: ")
            autor = Autor(nombre, nacionalidad)  # Crea un nuevo autor
            biblioteca.agregar_autor(autor)      # Agrega el autor a la biblioteca

        elif opcion == '2':  # Opción para agregar libro
            titulo = input("Título del libro: ")
            autor_nombre = input("Nombre del autor: ")
            anio = input("Año de publicación: ")
            autor = Autor(autor_nombre, "Desconocido")  # Crea un nuevo autor, se puede mejorar
            libro = Libro(titulo, autor, anio)  # Crea un nuevo libro
            biblioteca.agregar_libro(libro)      # Agrega el libro a la biblioteca

        elif opcion == '3':  # Opción para eliminar libro
            titulo = input("Título del libro a eliminar: ")
            biblioteca.eliminar_libro(titulo)  # Elimina el libro

        elif opcion == '4':  # Opción para eliminar autor
            nombre = input("Nombre del autor a eliminar: ")
            biblioteca.eliminar_autor(nombre)  # Elimina el autor

        elif opcion == '5':  # Opción para mostrar libros
            biblioteca.mostrar_libros()  # Muestra los libros

        elif opcion == '6':  # Opción para mostrar autores
            biblioteca.mostrar_autores()  # Muestra los autores

        elif opcion == '7':  # Opción para salir
            print("¡Gracias por usar la biblioteca! Hasta luego.")
            break  # Sale del bucle

        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 7.")  # Mensaje para opción inválida

# Llamada a la función principal
main()  # Ejecuta el programa
