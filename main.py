# Sistema básico de registro de estudiantes

estudiantes = []


def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    carrera = input("Ingrese la carrera: ")

    # MEJORA: Validación para evitar ingresar una edad incorrecta
    try:
        edad = int(input("Ingrese la edad: "))

        if edad <= 0:
            print("La edad debe ser mayor que cero.")
            return

    except ValueError:
        print("Error: la edad debe ser un número.")
        return

    estudiante = {
        "nombre": nombre,
        "carrera": carrera,
        "edad": edad
    }

    estudiantes.append(estudiante)
    print("Estudiante registrado correctamente.")


def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        print("\n--- LISTA DE ESTUDIANTES ---")

        for estudiante in estudiantes:
            print("Nombre:", estudiante["nombre"])
            print("Carrera:", estudiante["carrera"])
            print("Edad:", estudiante["edad"])
            print("------------------------")


# MEJORA: Nueva función para buscar un estudiante por su nombre
def buscar_estudiante():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")

    for estudiante in estudiantes:

        # MEJORA: lower() permite buscar sin importar mayúsculas o minúsculas
        if estudiante["nombre"].lower() == nombre_buscar.lower():
            print("\n--- ESTUDIANTE ENCONTRADO ---")
            print("Nombre:", estudiante["nombre"])
            print("Carrera:", estudiante["carrera"])
            print("Edad:", estudiante["edad"])
            return

    print("Estudiante no encontrado.")


def menu():
    while True:
        print("\n=== SISTEMA DE ESTUDIANTES ===")
        print("1. Registrar estudiante")
        print("2. Mostrar estudiantes")

        # MEJORA: Se agregó una nueva opción al menú
        print("3. Buscar estudiante")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_estudiante()

        elif opcion == "2":
            mostrar_estudiantes()

        # MEJORA: Llamamos a la nueva función de búsqueda
        elif opcion == "3":
            buscar_estudiante()

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Opción incorrecta.")


menu()